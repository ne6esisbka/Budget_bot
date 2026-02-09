# 🤖 Budget Bot

A personal finance management bot for Telegram. It makes it easy to track and analyze your finances.

## 🚀 Features
* 📝 **Transaction Log** — quickly record expenses and income.
* 📊 **Analytics** — detailed monthly and annual reports.
* 🗂  **Categories** — flexible classification of all expenses.

## 🛠 Tech Stack
* **Docker** & **Docker Compose** — application containerization.
* **Python 3.10+** (`aiogram 2.25` library).
* **PostgreSQL** — reliable data storage.
* **PgAdmin** — graphical interface for database management.

---

## 📦 Installation and Launch
## 1. Setting environment variables (Linux)
To use the bot, you need to enter the settings into the system. Open the file `.bot_env`:

```bash
>$ nano /$HOME/.bot_env
export BOT_TOKEN="YOUR TOKEN BOT"
export USER_ID="NUMBER ADMIN USER"             # to gain access to the bot
export NAME_DB_WO="NAME YOUR DATA BASE"
export HOST_DB_WO="postgres_db"                # container named PostgreSQL
export USER_DB_WO="YOUR NAME ADMIN postgres"
export PASS_DB_WO="YOUR PASSWORD ADMIN postgres"
export MY_EMAIL="YOUR ADMIN pgadmin"
export PASS_EMAIL="YOUR PASSWORD ADMIN pgadmin"
```
## 2. Clone the repository:
```
	$ git clone https://github.com/ne6esisbka/Budget_bot.git
```
## 3. Install bot:
```
	$ cd /$HOME/Mybot
	$ sudo chmod +x ./install_bot.sh
	$ sudo ./install_bot.sh
```
## 4. Launching the bot:
	The bot starts automatically.
