# AutoCapt_Bot
A telegram bot use to monitor and screenshot windows desktop
Original: https://github.com/shafiqsaaidin/monbot

## Requirement
Before this bot can be use, please make sure you have this following requirement:
- Python 3 download [here](https://www.python.org/downloads/)
- Pyautogui
- Telepot

## Installation
#### Linux
- pip3 install pyautogui
- pip3 install telepot

#### Windows 
- pip install pyautogui
- pip install telepot

## Usage
#### Setup bot Token
You have to setup a bot and get the bot api from bot Father
- Read [this](https://core.telegram.org/bots#6-botfather) before you can start
#### Setup an Admin id / chat_id
You have to set a variable adminId in tokens.py to be equal your chat_id or multiple chat_id (if more people will use your bot). For example:
- `adminId = [443355]`
- `adminId = [443355, -55667788, 99884433]`

#### How to get Admin id / chat_id
- Invite the bot into group
- Make it admin
- Mention (@) the bot
- Open this: https://api.telegram.org/bot(YOUR_BOT_TOKEN)/getUpdates
- Find `chat` key, and get the `id` value. usually its negative (example: -12345)

#### Change the period
- open mon.py, search `time.sleep(900)` into desired seconds.

#### Run the code
`python mon.py`

#### Capture desktop image
use this command in your bot to screenshot desktop image each 15 minutes`/start` Example:
![Imgur](https://i.imgur.com/RAUHEJb.png)


