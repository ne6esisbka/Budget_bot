import os
import re
import aiogram
import datetime
from aiogram import Bot, Dispatcher, executor, types
from databasebot import start_load_base, select_report_year
from variables import HELP, month_read
from replykeyboards import *
from inlinekeyboards import *
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from functioncategoreis import checking_for_folders, get_list, sum_of_other, sum_money_box, sum_of_price_numexpr,\
    select_month, open_money_box, create_dir_reports, create_dir_money, path_categories, open_categories, check_on_number


async def on_startup(_):
    print("Семейный дворецкий запущен ...")


# FamilyBudgetBot
storage = MemoryStorage()

bot = Bot(token=os.environ.get('BOT_TOKEN'))

dp = Dispatcher(bot, storage=storage)

CHECK_USER_ID = [int(os.environ['USER_ID']), int(os.environ['USER_ID2'])]

# Класс для выбора категории
class FillingStateGroup(StatesGroup):

    category = State()
    number = State()


# команда старт
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):

    if message.from_user.id not in CHECK_USER_ID:
        await message.answer('Я Вас не знаю! До свидания!')
    else:
        await message.answer("Привет, добро пожаловать к боту!",
                             reply_markup=get_main_menu())
        await message.delete()


# команда хелп
@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message) -> None:
    if message.from_user.id not in CHECK_USER_ID:
        await message.answer('Я Вас не знаю! До свидания!')
    else:
        await message.answer(f"{HELP}")
        await message.delete()


# вывод главного меню
@dp.message_handler(commands=["budget"])
async def cmd_budget(message: types.Message) -> None:
    if message.from_user.id not in CHECK_USER_ID:
        await message.answer('Я Вас не знаю! До свидания!')
    else:
        await message.answer("Выберите действие", reply_markup=get_main_menu())
        await message.delete()


#  вывод клавиатуры выбора категории
@dp.message_handler(Text(equals=["Вести бюджет"]))
async def send_budget(message: types.Message):
    if message.from_user.id not in CHECK_USER_ID:
        await message.answer('Я Вас не знаю! До свидания!')
    else:
        checking_for_folders()
        await message.answer(text="Выберите категорию для добавления!",
                             reply_markup=ikb_category_selection)
        await message.delete()
        await message.answer(text=f"Либо выбираем иное ...", reply_markup=closing())
        await FillingStateGroup.category.set()


#  выбор категории
@dp.callback_query_handler(state=FillingStateGroup.category)
async def make_a_categories(callback: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['category'] = callback.data
        if data['category'] == "Other":
            await callback.message.answer(text=f"{open_categories(data['category'])}\n"
                                               f"Итог = {sum_of_other(data['category'])}")
            await callback.message.answer(text=f"Введите категорию и сумму {get_list(data['category'])}\n"
                                               f"например: море 25000", reply_markup=closing())
        elif data["category"] == "Money_box":
            await callback.message.answer(text=f"{open_money_box()}\n"
                                               f"Итог = {sum_money_box()}")
            await callback.message.answer(text=f"Введите сумму {get_list(data['category'])}\n"
                                               f"например:\n 45 или -55 или 25+33", reply_markup=closing())
        else:
            await callback.message.answer(text=f"{open_categories(data['category'])}\n"
                                               f"Итог = {sum_of_price_numexpr(data['category'])}")
            await callback.message.answer(text=f"Введите сумму {get_list(data['category'])}\n"
                                               f"например:\n 45 или -55 или 25+33", reply_markup=closing())
        await callback.message.delete()
        await FillingStateGroup.next()


# действие кнопки отмены
@dp.message_handler(Text(equals=["Отменить"]), state="*")
async def cmd_close(message: types.Message, state: FSMContext) -> None:
    if message.from_user.id not in CHECK_USER_ID:
        await message.answer('Я Вас не знаю! До свидания!')
    else:
        await message.delete()
        await message.answer(text="Ввод окончен, Ваше величество!", reply_markup=get_main_menu())
        await state.finish()


# проверка на число введении суммы
@dp.message_handler(lambda message: not re.search('\d', message.text),
                    state=FillingStateGroup.number)
async def check_number(message: types.Message):
    await message.answer("❌ Вы ввели не правильную сумму")


# введение суммы в категорию
@dp.message_handler(state=FillingStateGroup.number)
async def make_a_number(message: types.Message, state: FSMContext) -> None:
    # Проверка на правильность ввода
    check_number_message = message.text
    

    
    async with state.proxy() as data:
        if not check_on_number(check_number_message, data['category']):
            await message.answer(f"❌ Ваша сумма указана не верно!  = {check_number_message}")
            return

        data['number'] = message.text
        
    if data['category'] == "Other":
        with open(f"{path_categories(data['category'])}", "a+",
                encoding="UTF-8") as file:
            file.write(f"{message.text}\n")
        await message.answer(f"✅ Ваша сумма записана!  = {data['number']}", reply_markup=get_main_menu())

    elif data['category'] == "Money_box":
        with open(f"{create_dir_money()}", "a+", 
                encoding="UTF-8") as file:
            file.write(f"+{data['number']}")
        await message.answer(f"✅ Ваша сумма записана!  = {data['number']}", reply_markup=get_main_menu())

    else:
        with open(f"{path_categories(data['category'])}","a+",
                encoding="UTF-8") as file:
            file.write(f"+{data['number']}")
        await message.answer(f"✅ Ваша сумма записана!  = {data['number']}", reply_markup=get_main_menu())
    
    await message.delete()

    await state.finish()


# скинуть EXCEL  файл
@dp.callback_query_handler()
async def load_excel_file(callback: types.CallbackQuery):
    if callback.data == "excel_file":
        await bot.send_document(callback.from_user.id,
                                open(f"{create_dir_reports()}"
                                     f"/path_to_file_{select_month()}.xlsx",
                                     "rb"))
    elif callback.data == "excel_file_2":
        await bot.send_document(callback.from_user.id,
                                open(f"{create_dir_reports()}"
                                     f"/calculations_for_years.xlsx",
                                     "rb"))
    await callback.message.delete()


# вывод итогов
@dp.message_handler(Text(equals=["Вывести итоги"]))
async def display_totals(message: types.Message) -> None:
    if message.from_user.id not in CHECK_USER_ID:
        await message.answer('Я Вас не знаю! До свидания!')
    else:      
        await message.answer(text=f"{month_read()}"
                                  f"{start_load_base()}\n"
                                  f"Копилка = {sum_money_box()}\n"
                                  f"{select_report_year()}\n",
                                  reply_markup=ikb_document)

if __name__ == "__main__":

    try:
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

    # except  as tel:
    #     with open("Error/Error_Telegram.txt", 'a+', encoding='UTF-8') as rf:
    #         rf.write(f'{datetime.datetime.now()}\nПроизошла ошибка Telegram:\n{tel}\n*****************************\n')
    except aiogram.exceptions.TelegramAPIError as aet:
        with open("Error/Error_connect.txt", 'a+', encoding='UTF-8') as rf:
            rf.write(f'{datetime.datetime.now()}\nПроизошла ошибка Telegram:\n{aet}\n*****************************\n')
    except aiogram.exceptions as aio:
        with open('Error/ERROR_connect1.txt', 'a+', encoding='UTF-8') as aef:
            aef.write(f"{datetime.datetime.now()}\nПроизошла ошибка aiogram:\n {aio}\n******************\n")
    except Exception as ex:
        with open("Error/Error.txt", 'a+', encoding='UTF-8') as rf:
            rf.write(f'{datetime.datetime.now()}\nПроизошла ошибка ALL:\n{ex}\n*****************************\n')
