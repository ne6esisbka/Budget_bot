#!/bin/bash

# --- НАСТРОЙКИ (измените под себя) ---
USER=$(whoami)
CONTAINER_NAME="my_telegram_bot"                # Имя вашего Docker-контейнера
BACKUP_DIR_PSQL="/home/$USER/postgres_backup"   # Путь к папке на хост-машине
                                    
# --- ЛОГИКА ---

echo "Saving to database begins from container $CONTAINER_NAME ..."

# Выполняем дамп, сжимаем и сохраняем на хост
docker exec -t my_telegram_bot python3 Budget_Bot/data_time_check.py

# Проверка успешности создания бэкапа
if [ $? -eq 0 ]; then
    echo "Saving to the database was successful."
else
    echo "Error: Save failed!"
    exit 1
fi

echo "Done. Current save in database:"
