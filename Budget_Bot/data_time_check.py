import datetime
from databasebot import start_load_base, select_report_year
from DB_admin import create_new_table_for_year

print("\nСейчас будет запись\n")
create_new_table_for_year()
start_load_base()
select_report_year()
print(f"АвтоЗапись в Базу сделана в {datetime.datetime.now().strftime('%H:%M:%S')}\n")






