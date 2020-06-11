#### Chat Wars Auto Fight
Automatically fights chat wars encounters

Note: Use at your own risk, you might get banned and I'm not responsible for that.


##### Installation
###### Getting authentication key from Telegram
1.) Visit [my.telegram.org](https://my.telegram.org) and login to your Telegram account with the phone number of the account to use.

2.) Click under API Development tools.

3.) A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.

4.) Click on Create application at the end. 

**Remember that your API hash gives full access to your account and Telegram won’t let you revoke it. Keep it a secret and don’t post it anywhere!**
###### Running the bot
1.) Clone this repo and enter it

`git clone https://github.com/oohwooh/cwautofight`

`cd cwautofight`

2.) Create a new virtual environment for the project

`python3 -m venv venv`

3.) Activate the virtual environment

MacOS/Linux: `source venv/bin/activate`

Windows: `venv\Scripts\activate`

You should now see your terminal prompt prefixed with `(venv)` 

4.)  Install required packages

`pip install -r requirements.txt`

5.) Run with required environment variables `API_ID` and `API_HASH`

MacOS/Linux: `export API_ID=API_ID_HERE; export API_HASH=API_HASH_HERE; python bot.py`

Windows: `set API_ID=API_ID_HERE & set API_HASH=API_HASH_HERE & python bot.py`

On first run, the program will prompt you for the phone number of your telegram account and login code.