# 🤖 Budget Bot
Бот для контроля финансов. Помогает записывать расходы и доходы прямо в Telegram.

## 🚀 Функционал
* Логирование транзакций
* Отчеты за месяц и за год
* Категории расходов

## 🛠 Стек технологий
* Docker
* Python 3.10+
* aiogram.2.25
* PostgreSQ
* PgAdmin 

## 📦 Установка
1. Linux:
	creating environment variables: 
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

2. Клонируйте репозиторий:
	`git clone https://github.com/ne6esisbka/Budget_bot.git
2. Install :
	$ cd /$HOME/Mybot
	$ sudo chmod +x ./install_bot.sh
	$ sudo ./install_bot.sh
3. Запустите бота:
	The bot starts automatically.
