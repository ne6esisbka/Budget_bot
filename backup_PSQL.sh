#!/bin/bash


# --- НАСТРОЙКИ (измените под себя) ---
USER=$(whoami)
CONTAINER_NAME="my_postgres"                    # Имя вашего Docker-контейнера
BACKUP_DIR_PSQL="/home/$USER/postgres_backup"   # Путь к папке на хост-машине
KEEP=3                                          # Количество хранимых копий
#PGPASSWORD=PASS                                # Раскомментируйте, если нужен пароль

# --- ЛОГИКА ---

# Текущая дата для имени файла
DATE=$(date +%Y-%m-%d_%H-%M-%S)
FILE_NAME="${NAME_DB_WO}_${DATE}.sql.gz"

# Создаем папку, если она не существует
mkdir -p "$BACKUP_DIR_PSQL"

echo "Starting backup of $NAME_DB_WO from container $CONTAINER_NAME..."

# Выполняем дамп, сжимаем и сохраняем на хост
docker exec -e PGPASSWORD="$PASS_DB_WO" $CONTAINER_NAME pg_dump -U $USER_DB_WO $NAME_DB_WO | gzip > "$BACKUP_DIR_PSQL/$FILE_NAME"

# Проверка успешности создания бэкапа
if [ $? -eq 0 ]; then
    echo "Backup successfully created: $BACKUP_DIR_PSQL/$FILE_NAME"
else
    echo "Error: Backup failed!"
    exit 1
fi

# --- РОТАЦИЯ (удаление старых копий) ---
echo "Cleaning up old backups (keeping only last $KEEP)..."

# Переходим в папку, сортируем файлы по дате (новые сверху), удаляем всё после $KEEP
cd "$BACKUP_DIR_PSQL" || exit
ls -t ${NAME_DB_WO}_*.sql.gz | tail -n +$((KEEP + 1)) | xargs -r rm --

echo "Done. Current backups in folder:"
ls -lh "$BACKUP_DIR_PSQL"
