import datetime
from config import name_db, host_db, user_name, pass_db
import psycopg2

# Проверяет существование таблицы в указанной схеме.
def check_table_exists(cursor, table_name, schema_name='public'):
        """
        Проверяет существование таблицы в указанной схеме.

        Аргументы:
            cursor: Объект курсора psycopg2.
            table_name: Имя таблицы для проверки.
            schema_name: Имя схемы (по умолчанию 'public').
        Возвращает:
            True, если таблица существует, False в противном случае.
        """
        query = """
            SELECT EXISTS (
                SELECT 1
                FROM information_schema.tables
                WHERE table_schema = %s AND table_name = %s
            );
        """
        
        # Используем параметризированный запрос для предотвращения SQL-инъекций
        cursor.execute(query, (schema_name, table_name))
        exists = cursor.fetchone()[0]
       
        return exists


# Создание таблицы в схеме для нового года
def create_new_table_for_year():

    year_now = datetime.datetime.now().strftime('%Y')

    

# запрос к базе данных
    try:
        conn = psycopg2.connect(
            database=name_db,
            host=host_db,
            port="5432",
            user=user_name,
            password=pass_db
            
        )
        
        
        with conn.cursor() as cursor:
            if check_table_exists(cursor, f"annual_report_{year_now}"):
                return print(f"Таблица 'annual_report_{year_now}' уже существует.")

            else:
                categores = ('Продукты', 'Хозтовары', 'Кв. в Коврове', 'Квартира', 'Аптека/Врачи', 'Транспорт', 'Моб.связь/Банки',\
                  'Доставка', 'Прочее', 'Хобби', 'Путешествие', 'Одежда', 'Спорт', 'Копилка', '*', 'Доходы', 'Расходы', '*', 'Разница', '*', 'Other_full')
                
                cursor.execute(
                    f"""
                    CREATE TABLE IF NOT EXISTS years (
                    "id" bigint PRIMARY key GENERATED ALWAYS AS IDENTITY,
                    "year" integer NOT NULL,
                    "id_year" INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) UNIQUE,
                    "Доходы" integer,
                    "Расходы" integer,
                    "Разница" integer
                    );
                    """
                )
                
                cursor.execute(
                    f"""
                    INSERT INTO "years" ("year", "Доходы", "Расходы", "Разница") 
                    VALUES (%s, %s, %s, %s)
                    RETURNING id
                    """,
                    (year_now, 0, 0, 0)
                    )

                year_id_from_db = cursor.fetchone()[0]
                
                cursor.execute(
                    f"""
                    CREATE TABLE IF NOT EXISTS "annual_report_{year_now}"(
                    "id" bigint PRIMARY key GENERATED ALWAYS AS IDENTITY,
                    "id_year"	INTEGER NOT NULL,
                    "Категория"	TEXT,
                    "Январь"	INTEGER,
                    "Февраль"	INTEGER,
                    "Март"	INTEGER,
                    "Апрель"	INTEGER,
                    "Май"	INTEGER,
                    "Июнь"	INTEGER,
                    "Июль"	INTEGER,
                    "Август"	INTEGER,
                    "Сентябрь"	INTEGER,
                    "Октябрь"	INTEGER,
                    "Ноябрь"	INTEGER,
                    "Декабрь"	INTEGER,
                    FOREIGN KEY("id_year") REFERENCES "years"("id_year")
                ); """
                )
            
                data_to_insert = [
                    (year_id_from_db, 'Продукты', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Хозтовары', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Кв. в Коврове', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Квартира', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Аптека/Врачи', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Транспорт', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Моб.связь/Банки', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Доставка', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Прочее', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Хобби', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Путешествие', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Одежда', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Спорт', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Копилка', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, '***', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Доходы', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Расходы', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, '***',0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Разница', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, '***', 0,0,0,0,0,0,0,0,0,0,0,0),
                    (year_id_from_db, 'Other_full', 0,0,0,0,0,0,0,0,0,0,0,0)
                ]
                                 
                insert_query = f"""INSERT INTO "annual_report_{year_now}" (id_year, "Категория", "Январь", "Февраль", "Март", "Апрель", "Май", 
                "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
                cursor.executemany(insert_query, data_to_insert)
                conn.commit()
            conn.commit()
            conn.close()     
      
    except Exception as ex:
        return print("[INFO] Error while working with PostgreSQL", ex)

    finally:
        print("Close connect ...")
    return print("Создание таблицы для Базы Данных завершено, спасибо!")
