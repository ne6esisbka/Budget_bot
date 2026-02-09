#!/bin/bash
echo "The Docker container installation with the Budget bot for your family is starting."

USER=$(whoami)
FOLDER_FOR_PSQL="/home/$USER/postgres_backup"
FOLDER_FOR_PGAD="/home/$USER/pgadmin_backup"
FOLDER_FOR_LOG="/home/$USER/logs_save_in_db"

if  [ ! -d "$FOLDER_FOR_PSQL" ] && [ ! -d "$FOLDER_FOR_PGAD" ] && [ ! -d "$FOLDER_FOR_LOG" ]; then
    sudo mkdir -p $FOLDER_FOR_PSQL $FOLDER_FOR_PGAD $FOLDER_FOR_LOG
    sudo chown -R $USER:$USER $FOLDER_FOR_PSQL
    sudo chown -R $USER:$USER $FOLDER_FOR_PGAD
    sudo chown -R $USER:$USER $FOLDER_FOR_LOG
    chmod -R 755 $FOLDER_FOR_PSQL
    chmod -R 755 $FOLDER_FOR_PGAD
    chmod -R 755 $FOLDER_FOR_LOG
    
    echo "Folders for PostgreSQL and PgAdmin created"

else
    echo "Folders for PostgreSQL and PgAdmin exists"
fi

echo "Запуск сервисов Docker Compose в фоновом режиме..."

docker compose up -d --build

# Сохранение в базу из файлов 
SCRIPT_PATH_SAVE="/home/$USER/My_bot/save_in_db.sh"
SCRIPT_PATH_PSQL="/home/$USER/My_bot/backup_PSQL.sh"
LOG_SAVE="${FOLDER_FOR_LOG}/save_in_db.log"
LOG_PSQL="${SCRIPT_PATH_PSQL}/dump_db.log"


sudo chmod +x $SCRIPT_PATH_SAVE
sudo chmod +x $SCRIPT_PATH_PSQL

if [ ! -f "$SCRIPT_PATH_SAVE" ] && [ ! -f "$SCRIPT_PATH_PSQL" ]; then
    echo "Ошибка: Файлы $SCRIPT_PATH_SAVE * И * $SCRIPT_PATH_PSQL не найдены. Сначала создайте их."
    exit 1
fi

# 1. Формируем задачу для Cron: 6 раз в день (каждые 3 часа)
# "30 3-23.4 * * *" означает:  каждые 3 часа (3,7,11,15,19,23 и 30 минут)
CRON_SAVE="30 3-23/4 * * * /bin/bash $SCRIPT_PATH_SAVE >> $LOG_SAVE 2>&1"

# 1. Формируем задачу для Cron: Сохранение dump DB_WO
#  (запуск в 03:00 каждое воскресенье)
CRON_DUMP="0 3 * * 0 /bin/bash $SCRIPT_PATH_PSQL >> $LOG_PSQL 2>&1 "

# Проверяем, нет ли уже такой задачи в кроне, чтобы не дублировать
(crontab -l 2>/dev/null | grep -F "$SCRIPT_PATH_SAVE") > /dev/null
(crontab -l 2>/dev/null | grep -F "$SCRIPT_PATH_PSQL") > /dev/null

if [ $? -eq 0 ]; then
    echo "Запись уже существует в crontab. Ничего не изменено."
else
    # Добавляем новую задачу в текущий список cron
    (crontab -l 2>/dev/null; echo "$CRON_SAVE") | crontab -
    (crontab -l 2>/dev/null; echo "$CRON_DUMP") | crontab -
    echo "Задача успешно добавлена в crontab!"
    echo "Расписание: каждый день каждые 6 часов и в 03:00 каждое воскресенье сохранение БАЗЫ данных"
fi

# Проверка статуса (опционально)
if [ $? -eq 0 ]; then
    echo "Все сервисы успешно запущены."
else
    echo "Произошла ошибка при запуске сервисов."
fi
