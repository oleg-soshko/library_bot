# Library Telegram Bot
  Telegram bot with books for upgrading soft skills.
### 1. Installation

```sh
$ git clone https://github.com/feispy/library_bot.git
$ cd library_bot
$ pip install -r requirements.txt
```
- Open ```bot.py``` file and change variable ```token``` (create a bot using @BotFather, and get the Telegram API token.).
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

### 3. Deploy on Heroku
    
- Clone this repository on your local system
    ```
    git clone https://github.com/feispy/library_bot.git
    ```
 - Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
 - Login to your account with the below command

     ```
    heroku login
    ```
 - Create a new heroku app:
     ```
     heroku create appname
    ```
- Go to Libgen-Telegram-Bot directory on your local system
    ```
    cd Libgen-Telegram-Bot
    ```
- Select This App in your Heroku-cli
    ```
    heroku git:remote -a appname
    ```
- Open ```common.py``` and add your Bot Token to ```TELEGRAM_ACCESS_TOKEN``` and Heroku app name to ```HEROKU_APP_NAME``` variables.

- Add Private Credentials and Config Stuff:
    ```
    git add . 
    ```
- Commit new changes:
    ```
    git commit -m "First Push"
    ```
- Push Code to Heroku:
    ```
    git push heroku master
    ```
- Enable Heroku Dyno
    ```
    heroku ps:scale web=1
    ```

