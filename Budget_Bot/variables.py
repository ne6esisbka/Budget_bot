from functioncategoreis import sum_of_other, sum_of_price_numexpr, month_selection

HELP = """
        здесь команды для помощи
    """
columns_cate = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь",
                7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

categories_all = ["Products", "Household", "Kovrov", "Apartment", "Pharmacy", "Transport", "Mobile_banks",
                  "Delivery", "Hobby", "Other", "Traveling", "Salary", "Cloth", 'Sport']

print(f"Текущий месяц : {columns_cate[month_selection()]}")


def month_read():
    month_collection = f"""
{columns_cate[month_selection()]}
Продукты_________{sum_of_price_numexpr(categories_all[0])}
Хозтовары________{sum_of_price_numexpr(categories_all[1])}
Кв. в Коврове______{sum_of_price_numexpr(categories_all[2])}
Квартира_________{sum_of_price_numexpr(categories_all[3])}
Аптека/Врачи_____{sum_of_price_numexpr(categories_all[4])}
Транспорт________{sum_of_price_numexpr(categories_all[5])}
Моб.связь/Банки___{sum_of_price_numexpr(categories_all[6])}
Доставка_________{sum_of_price_numexpr(categories_all[7])}
Хобби____________{sum_of_price_numexpr(categories_all[8])}
Прочее___________{sum_of_other(categories_all[9])}
Путешествие_______{sum_of_price_numexpr(categories_all[10])}
Одежда___________{sum_of_price_numexpr(categories_all[12])}
Спорт____________{sum_of_price_numexpr(categories_all[13])}
Доходы___________{sum_of_price_numexpr(categories_all[11])}
Расходы__________{sum_of_all_categories_result(categories_all)}
"""
    return month_collection


# словарь для подсчёта в Базу Данных
def razdel_all(raz):
    my_symbol = "/. "
    cate = raz.split('\n')[2:]
    res = [j for i in cate for j in i.split('_') if j.isalpha() or j.isdigit() or j not in my_symbol]
    result = {res[i]: res[i + 1] for i in range(0, len(res), 2)}

    return result


# подсчёт суммы за месяц
def sum_of_all_categories_result(categors):
    sum_cat = []
    for i in range(len(categors)):
        if i == 9:
            sum_cat.append(sum_of_other(categories_all[9]))
        elif i == 11:
            pass
        else:
            sum_cat.append(sum_of_price_numexpr(categories_all[i]))

    return sum(sum_cat)


# ############################### переменная для подсчёта за месяц ##########################################
# result_sum_categors = sum_of_all_categors_result(categors_all)  #
# ##############################################################################################################






# def sum_cate_def(categor):
#     result = []
#     for i in categor:
#
#         result.append()
# sum_cate_def(categors_all)
#
# for i in categors_all:
#     res = []
#     res.append(sum_of_all_categors_result(i))
#     print(f"res={res}\n")
# #
#

#


#

# print(f"result_sum_categors in variables\n{result_sum_categors}")
# print(f"{razdel_all(mounth_read())}\n {len(rachet_categ)}")
# print(f"rachet_categ in variables\n{rachet_categ}")
