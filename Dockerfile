# Используем официальный образ Python (например, slim-версию)
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /Budget_Bot

# Копируем файл с зависимостями
COPY requirements.txt ./

# Устанавливаем зависимости
RUN apt update
RUN apt update -y
RUN pip install --no-cache-dir -r requirements.txt
# Set Moscow time and date
ENV TZ=Europe/Moscow
ENV UBUNTU_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt update && apt update -y && apt-get install -y procps coreutils && rm -rf /var/lib/apt/lists/*
# Копируем все файлы проекта в контейнер

COPY . .

# RUN groupadd -r botgroup && useradd -r -g botgroup -s /bin/false botser
# USER botser

CMD ["python3", "./Budget_Bot/main.py"]