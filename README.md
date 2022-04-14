# Library Telegram Bot
  Telegram bot with books for upgrading soft skills.
### 1. Installation

```sh
$ git clone https://github.com/feispy/library_bot.git
$ cd library_bot
$ pip install -r requirements.txt
```
- Open ```bot.py``` file and change variable ```token``` (create a bot using @BotFather, and get the Telegram API token.). And change ```admin_id``` - your chat_id.
- Open ```database.py``` file and change variable ```DATABASE_URL``` (if you need using database).
This project uses a database ```Postgresql```, but you can choose another by changing the variable ```engine```.

- Run
    ```
    python bot.py
    ```
- You can add your books by adding them to the folder ```books``` (to path ```books/<category>/<book.pdf>```).
### 2. Bot Commands
Command | Description
:--- | :---
/start | Start page.
/help | List of all commands.
/category | List of all categories.
/feedback | Give feedback.

### 3. Telegram

    [ааа](https://t.me/North_Library_bot)

 
