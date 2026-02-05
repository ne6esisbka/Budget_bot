# 🤖 Budget Bot

Бот для контроля личных финансов в Telegram. Позволяет удобно фиксировать движение средств и анализировать бюджет.

## 🚀 Функционал
* 📝 **Логирование транзакций** — быстрая запись расходов и доходов.
* 📊 **Аналитика** — детальные отчеты за месяц и за год.
* 🗂 **Категории** — гибкая классификация всех трат.

## 🛠 Стек технологий
* **Docker** & **Docker Compose** — контейнеризация приложения.
* **Python 3.10+** (библиотека `aiogram 2.25`).
* **PostgreSQL** — надежное хранение данных.
* **PgAdmin** — графический интерфейс для управления базой данных.

---

## 📦 Установка и запуск

## 1. Setting environment variables (Linux)
Для работы бота необходимо прописать настройки в систему. Откройте файл `.bashrc`:

```bash
>$ nano ~/.bashrc
export BOT_TOKEN="YOUR TOKEN BOT"
export USER_ID="NUMBER ADMIN USER"             # to gain access to the bot
export NAME_DB_WO="NAME YOUR DATA BASE"
export HOST_DB_WO="postgres_db"                # container named PostgreSQL
export USER_DB_WO="YOUR NAME ADMIN postgres"
export PASS_DB_WO="YOUR PASSWORD ADMIN postgres"
export MY_EMAIL="YOUR ADMIN pgadmin"
export PASS_EMAIL="YOUR PASSWORD ADMIN pgadmin"
>$ source ~/.bashrc 
	or reboot server

## 2. Clone the repository:
	`git clone https://github.com/ne6esisbka/Budget_bot.git
## 3. Install bot:
	$ cd /$HOME/Mybot
	$ sudo chmod +x ./install_bot.sh
	$ sudo ./install_bot.sh
## 4. Launching the bot:
	The bot starts automatically.
