from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#  создание клавиатуры главного меню
def get_main_menu() -> ReplyKeyboardMarkup:
    kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_main_menu.add(KeyboardButton("Вести бюджет")).add(KeyboardButton("Вывести итоги"))
    return kb_main_menu


# создание клавиатуры выбора действий
def make_a_choice() -> ReplyKeyboardMarkup:
    kb_make_a_choice = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_make_a_choice.add("Добавить расходы").add(KeyboardButton("Вывести итоги"))
    return kb_make_a_choice


# кнопка отмены ввода
def closing() -> ReplyKeyboardMarkup:
    kb_close = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_close.add(KeyboardButton("Отменить"))
    return kb_close