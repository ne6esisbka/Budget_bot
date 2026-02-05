from config import name_db, host_db, user_name, pass_db
from variables import (razdel_all, month_read, sum_of_all_categories_result, categories_all, columns_cate)
from functioncategoreis import sum_money_box, month_selection
import psycopg2
import pandas as pd
import datetime
from DB_admin import create_new_table_for_year

# таблица за месяц
col_mounts = ["категория", "январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь",
              "октябрь", "ноябрь", "декабрь"]
# таблица за год
col_years = ["year", "Расходы", "Доходы", "Разница"]


#  запись в базу данных
def start_load_base():
    create_new_table_for_year()
    rachet_categ = razdel_all(month_read())
    time_is_ymd = datetime.datetime.now().date()
    time_is_now = datetime.datetime.now().strftime('%H:%M:%S')
    year_now = datetime.datetime.now().strftime('%Y')
    income = rachet_categ.get('Доходы')
    expenses = sum_of_all_categories_result(categories_all)
    difference = int(income) - int(expenses)
    month_now = columns_cate[month_selection()]
    name_table = f"annual_report_{year_now}"
    reading_in_mouth = []

# запрос к базе данных
    try:
        conn = psycopg2.connect(
            database=name_db,
            host=host_db,
            user=user_name,
            password=pass_db
        )
        with conn.cursor() as cursor:
            cursor.execute(
                f"""
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Продукты')}
                WHERE id = {1};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Хозтовары')}
                WHERE id = {2};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Кв. в Коврове')}
                WHERE id = {3};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Квартира')}
                WHERE id = {4};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Аптека/Врачи')}
                WHERE id = {5};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Транспорт')}
                WHERE id = {6};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Моб.связь/Банки')}
                WHERE id = {7};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Доставка')}
                WHERE id = {8};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Прочее')}
                WHERE id = {9};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Хобби')}
                WHERE id = {10};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Путешествие')}
                WHERE id = {11};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Одежда')}
                WHERE id = {12};
                UPDATE {name_table}
                SET {month_now} = {rachet_categ.get('Спорт')}
                WHERE id = {13};
                UPDATE {name_table}
                SET {month_now} = {sum_money_box()}
                WHERE id = {14};
                UPDATE {name_table}
                SET {month_now} = {income}
                WHERE id = {16};
                UPDATE {name_table}
                SET {month_now} = {expenses}
                WHERE id = {17};
                UPDATE {name_table}
                SET {month_now} = {difference}
                WHERE id = {19};    
                
                SELECT Категория,Январь,Февраль,Март,Апрель,Май, Июнь, Июль, Август, Сентябрь, Октябрь, Ноябрь,Декабрь
                FROM {name_table}
                WHERE id < 25
                ORDER BY id;
                
                """
            )
            reading_in_mouth = cursor.fetchall()
            print(f"Сэр, была сделана запись в Базу Данных!\n"
                f"{time_is_ymd} <*> {time_is_now}")

        # with conn.cursor() as cursor:
        #     cursor.execute(
        #         f"""
        #     UPDATE list_mounths
        #     SET Расход = {sum_of_all_categors_result(categors_all)}
        #     WHERE id = 6;
        #
        #     SELECT Название_месяца, Расход, Приход, Разница FROM list_mounths
        #     WHERE id < 14;
        #
        #     """
        #     )
        #     reading_in_years = cursor.fetchall()
        #     print(f"reading_in_years\n{reading_in_years}")
        conn.commit()
        conn.close()
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    finally:
        print("Close connect ...")
    print(f"Результат работы функции...")


# показ таблицы расходов в месяц
    df_mounts = pd.DataFrame(data=reading_in_mouth, columns=col_mounts)
    df_mounts.to_excel(f"./Folders_for_bot/REPORTS/REPORT_{year_now}/path_to_file_{month_now}.xlsx")
    #month_results = df_mounts.head(25)

    # df_years = pd.DataFrame(data=reading_in_years, columns=col_years)
    # df_years.to_excel("calculations_for_month.xlsx", index=False)
    # years_result = df_years.head(14)

    return "Запись в Базу Данных сделана, спасибо!"

# **********************************************************************************************


# создание Excel для отчёта за год
def select_report_year():
    create_new_table_for_year()
    year_now = datetime.datetime.now().strftime('%Y')
    name_table = f"annual_report_{year_now}"
    con = psycopg2.connect(
        database=name_db,
        host=host_db,
        user=user_name,
        password=pass_db
        )
   
    with con.cursor() as cur:
        cur.execute(f"""
            select Январь, Февраль, Март, Апрель, Май, Июнь, Июль, Август, Сентябрь,
              Октябрь, Ноябрь, Декабрь from {name_table}
            where Категория in ('Доходы', 'Расходы');
            """)
    
        count_income = 0
        count_expenses = 0
        res = cur.fetchall()

        for i in res[0]:
            count_income += int(i)
        for i in res[1]:
            count_expenses += int(i)
        difference = count_income - count_expenses

        cur.execute(f"""
            UPDATE years
            SET Расходы = {count_expenses}
            where year = {year_now};

            UPDATE years
            SET Доходы = {count_income}
            where year = {year_now};

            UPDATE years
            SET Разница = {difference}
            where year = {year_now};

            """)
    con.commit()

    with con.cursor() as cur:
        cur.execute(f"""
            SELECT year, Расходы, Доходы, Разница FROM years
            ORDER BY id ASC
            """)
        report_years = cur.fetchall()
    df_years = pd.DataFrame(data=report_years, columns=col_years)
    df_years.to_excel(f"./Folders_for_bot/REPORTS/REPORT_{year_now}/calculations_for_years.xlsx")
    df_years.head(25)

    con.commit()
    con.close()
   
    return "Сейчас вылетит птичка"

#  ####################################################################################################
# файлы для проверки записей в БД


    #with open("record.txt", "w+", encoding="UTF-8") as file:
    #    file.write(f"{month_results}")

# columns_cate_all = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь",
#                     7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

# categors_all2 = ["Products", "Household", "Kovrov", "Apartment", "Pharmacy", "Transport", "Mobile_banks", "Delivery",
#                  "Hobby", "Other", "Traveling", "Salary"]