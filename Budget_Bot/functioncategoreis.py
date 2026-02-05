import os
import datetime
import numexpr as ne
from pathlib import Path

# months = datetime.datetime.now().month
# years = datetime.datetime.now().year

def get_list(catig):
    """ Возвращает название категории из словаря """

    dict_categories = {
        "Products": "Продукты",
        "Household": "Хозяйственные товары",
        "Apartment": "Квартира",
        "Pharmacy": "аптека или врач",
        "Kovrov": "Ковров",
        "Cloth": "Одежда",
        "Delivery": "Доставка",
        "Transport": "Транспорт",
        "Mobile_banks": "Мобильная связь или Банк",
        "Hobby": "Хобби",
        "Other": "Прочее",
        "Traveling": "Путешествие",
        "Salary": "Доход",
        "Money_box": "Копилка",
        'Sport': 'Спорт'
    }
    return dict_categories[f"{catig}"]


def month_selection():
    """ Вывод текущего месяца """
    return datetime.datetime.now().month


def month_now_word():
    """
    Docstring для month_now_word\n
    return datetime.datetime.now()
    """
    return datetime.datetime.now()


def select_month():
    """Текущий месяц словом"""
    month_list = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
    }
    return month_list[datetime.datetime.now().date().month]


def select_years():
    """ Вывод год  """
    years = datetime.datetime.now().year
    return f'{years}'


def create_dir_years_and_month():
    """
    Создает или проверяет путь к папке /Budget_Bot/Folders_for_bot/Categories/текущий_год/текущий_месяц 
    """
    path_dir = Path(f"./Folders_for_bot/Categories/{select_years()}/{select_month()}")
    
    if not path_dir.exists():
        path_dir.mkdir(parents=True, exist_ok=True)
        
        categories_all = ["Products", "Household", "Kovrov", "Apartment", "Pharmacy", "Transport", "Mobile_banks",
                                    "Delivery", "Hobby", "Other", "Traveling", "Salary", "Cloth", 'Sport']
        
        if path_dir.is_dir():
            for check_file in categories_all:
                chech_for_dirs = path_dir / f"{check_file}.txt"
                if not chech_for_dirs.is_file():   
                    chech_for_dirs.touch()
                    chech_for_dirs.write_text(f"{get_list(check_file)}\n0", encoding='UTF-8')

    return path_dir.absolute()


def create_dir_reports():
    """
    Выводит путь к папке /Budget_Bot/Folders_for_bot/REPORTS/REPORT_текущий_год
    \nparam: return report_dir.absolute()
    """
    report_dir = Path(f"./Folders_for_bot/REPORTS/REPORT_{select_years()}")
    
    report_dir.mkdir(parents=True, exist_ok=True)


    return report_dir.absolute()


def create_dir_money():
    """
        Creting or exists folder for Money_Box and file Money_Box.txt
        \nparam: return money_file.absolute()
    """
    path_dir = Path(f"./Folders_for_bot/Money_Box")
    money_file = Path(f"./Folders_for_bot/Money_Box/Money_Box.txt")
    path_dir.mkdir(parents=True, exist_ok=True)      

    if not money_file.is_file():
        # Создать файл и сразу открыть для записи
        money_file.touch()
        money_file.write_text(f"{get_list('Money_box')}\n0", encoding='UTF-8')
        
        return money_file.absolute()

    return money_file.absolute()


def checking_for_folders():
    """
        Проверка папок на существование или создание новых папок для категорий, отчетов и копилки
        \nparam: return f"Папки и Файлы созданы"
    """
    try:           
        create_dir_years_and_month()
        create_dir_money()
        create_dir_reports()
        return 0
    except Exception as e:
        return f"ERROR = ERROR {e}"
        


def path_categories(categore):
    """
    Путь до файлика категории
    \nparam: return new_pathdir.absolute()
    """
    pathdir = create_dir_years_and_month()
    new_pathdir = pathdir / f"{categore}.txt"

    return new_pathdir.absolute()


def open_categories(categore):    
    return path_categories(categore).read_text(encoding='UTF-8')


def sum_of_price_numexpr(prices):
    """ Подсчёт итоговой суммы категории """
    with open(f"{create_dir_years_and_month()}/{prices}.txt", "r",
              encoding="UTF-8") as file:
        read_file = file.read().split("\n")[1]
        res = ne.evaluate(read_file)
    return res


def sum_of_price(prices):
    """ Подсчёт итоговой суммы категории """
    with open(f"{create_dir_years_and_month()}/{prices}.txt", "r",
              encoding="UTF-8") as file:
        read_file = file.read().split("\n")
        sum_num = [int(i) for line2 in read_file for i in line2.split("+") if i.isdigit()]
    return sum(sum_num)


# Подсчёт суммы Прочее
def sum_of_other(other):
    with open(f"{create_dir_years_and_month()}/{other}.txt", "r",
              encoding="UTF-8") as file:
        read_file = file.read().split("\n")
        sum_num = [int(i) for line2 in read_file for i in line2.split(" ") if i.isdigit()]
    return sum(sum_num)


# Подсчёт Копилки
def sum_money_box():
    with open(f"{create_dir_money()}", "r", encoding="UTF-8") as file:
        read_file = file.read().split("\n")[1]
        if read_file == "0":
            return 0
        else:
            res = ne.evaluate(read_file)
            return res


def open_money_box():
    with open(f"{create_dir_money()}", "r", encoding="UTF-8") as rf:
        return rf.read()
    


def check_on_number(number, category):
   
    try:
        if number.isdigit() and category != "Other":
            return True
        elif '+' in number and all([n.isdigit() for n in  number.split('+')]) and category != "Other":
            return True
        elif number.split(" ")[-1].isdigit() and all([n.isalpha() for n in number.split(" ")[:-2]]) and category == "Other":
            return True

    except Exception as e:
        print("ERROR", e)
        
    return False



# def select_calculation_FIXME(calcu):
#     """Проверка папок на существование или создание новых папок для категорий"""
#     dir_date = f"./Category/{select_years()}/"
#     check_file = f"./Category/{select_years()}/{calcu}.txt"
#     if os.path.exists(dir_date) and os.path.exists(check_file):
#         print(f"Папка существует")

#         with open(f"./Category/{select_years()}/{calcu}.txt", "r",
#                   encoding="UTF-8") as file:
#             open_file = file.read()
#     elif os.path.exists(dir_date) and not os.path.exists(check_file):
#         with open(f"./Category/{select_years()}/{calcu}.txt", "a",
#                   encoding="UTF-8") as file:
#             file.write(f"{get_list(calcu)}:\n0")
#     else:
#         print("Такой папки нет, сейчас создадим ...")

#         os.mkdir(f"./Category/{select_years()}")
#         categories_all = ["Products", "Household", "Kovrov", "Apartment", "Pharmacy", "Transport", "Mobile_banks",
#                           "Delivery", "Hobby", "Other", "Traveling", "Salary", "Cloth", 'Sport']
#         for i in categories_all:
#             with open(f"./Category/{select_years()}/{i}.txt", "a",
#                       encoding="UTF-8") as file:
#                 file.write(f"{get_list(i)}:\n0")
#         print(f"файлы созданы")
#         with open(f"./Category/{select_years()}/{calcu}.txt", "r",
#                   encoding="UTF-8") as file:
#             open_file = file.read()
#     return open_file
# C:/Users/Admin/Desktop/Bugget_Bot/./Category/

# Выбор категории
# def select_category(category):
#     if category == "Products":
#         text = "Введите сумму продуктов "

        # elif category == "Apartment":
        #
        #     text = "Введите сумму квартиры"
        #
        # elif category == "Household":
        #
        #     text="Введите сумму хозтоваров"
        #
        # elif category == "Pharmacy":
        #     text="Введите сумму Аптека/Врачи"
        #
        # elif category == "Kovrov":
        #     text="Введите сумму кв в Коврове"
        #
        # elif category == "Transport":
        #     text="Введите сумму транспорт"
        #
        # elif category == "Mobile_banks":
        #     text="Введите сумму мобильная связь или банка"
        #
        #
        # elif category == "Delivery":
        #     text="Введите сумму доставки"
        #
        # elif category == "Other":
        #     text="Введите сумму прочее"
        #
        #

    # return category


        # if callback.data == "Products":
        #     data['category'] = callback.data
        #     await callback.message.answer(text="Введите сумму продуктов ")
        #     await FillingStateGroup.next()
        # elif callback.data == "Apartment":
        #     data['category'] = callback.data
        #     await callback.message.answer(text="Введите сумму квартиры")
        #     await FillingStateGroup.next()
        # elif callback.data == "Household":
        #     data['category'] = callback.data
        #     await callback.message.answer(text="Введите сумму хозтоваров")
        #     await FillingStateGroup.next()
        # elif callback.data == "Pharmacy":
        #     data['category'] = callback.data
        #     await callback.message.answer(text="Введите сумму Аптека/Врачи")
        #     await FillingStateGroup.next()
        # elif callback.data == "Kovrov":
        #     data['category'] = callback.data
        #     await callback.message.answer(text="Введите сумму кв в Коврове")
        #     await FillingStateGroup.next()
        # elif callback.data == "Transport":
        #     data['category'] = callback.data
        #     await callback.message.answer(text="Введите сумму транспорт")
        #     await FillingStateGroup.next()
        # elif callback.data == "Mobile_banks":
        #     data['category'] = callback.data
        #     await callback.message.answer(text="Введите сумму мобильная связь или банка")
        #     await FillingStateGroup.next()
        #
        # elif callback.data == "Delivery":
        #     data['category'] = callback.data
        #     await callback.message.answer(text="Введите сумму доставки")
        #     await FillingStateGroup.next()
        # elif callback.data == "Other":
        #     data['category'] = callback.data
        #     await callback.message.answer(text="Введите сумму прочее")
        #     await FillingStateGroup.next()


# def select_calculation(calcu):
#     """
#         Проверка папок на существование или создание новых папок для категорий
#     """
#     try:
         
#         if dir_years_and_month().exists():
#             print("Папка существует")
#             with open(f"{dir_years_and_month()}/{calcu}.txt", 'r', encoding='UTF-8') as file:
#                 open_file = file.read()
#                 print("Запись в файл сделана")
#                 return open_file
#         else:
#             print("ELSE")       
#             dir_years_and_month().mkdir(parents=True, exist_ok=True)
#             print(f"Путь {dir_years_and_month().resolve()} успешно создан.")
            
#             for num_month in range(1, 13):
#                 os.mkdir(f"{dir_years_and_month()}")
#                 categories_all = ["Products", "Household", "Kovrov", "Apartment", "Pharmacy", "Transport", "Mobile_banks",
#                                 "Delivery", "Hobby", "Other", "Traveling", "Salary", "Cloth", 'Sport']
#                 for file in categories_all:
#                     with open(f"{dir_years_and_month()}/{file}.txt",
#                             'w', encoding='UTF-8') as f:
#                         f.write(f"{get_list(file)}\n0")

#         create_dir_money().mkdir(parents=True, exist_ok=True)
#         print("Папка Money_Box создана")

#         create_dir_reports().mkdir(parents=True, exist_ok=True)
#         print(f"Папка REPORT_{select_years()} создана")
 
#         print("Файлы созданы на весь год!")

#     except Exception as e:
#          print(f"Произошла ошибка при создании папки: {e}")

#     return select_calculation(calcu)