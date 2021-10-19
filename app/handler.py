"""Lambda function file for sending scheduled message to a connected Telegram chat via Chat ID."""

import os
import random
import telegram

SRC_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
MESSAGES_TEMPLATE_FILE_PATH = os.path.join(SRC_FOLDER_PATH, 'messages.txt')
STICKERS_TEMPLATE_FILE_PATH = os.path.join(SRC_FOLDER_PATH, 'stickers.txt')

# Load environment variables
TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

def convert_file_to_list(path, default_value):
    """Read lines from file and put them into a list"""
    try:
        with open(path, encoding='utf8') as file:
            lines = file.readlines()
            result = [line.rstrip() for line in lines]
    except FileNotFoundError:
        result = [default_value]

    return result

# Telegram bot messages and stickers template
messages=convert_file_to_list(
    path=MESSAGES_TEMPLATE_FILE_PATH,
    default_value='見字飲水！'
)
stickers=convert_file_to_list(
    path=STICKERS_TEMPLATE_FILE_PATH,
    default_value='CAACAgUAAxkBAAMIYW5oA1yXPqXGhsjJVOTutsuNA2UAAtwEAAIhGnFXAUGWMsy7GcQgBA'
)

def send_message(event, context):
    """Lambda function handler to send text message."""
    bot = telegram.Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=random.choice(messages))
    bot.send_sticker(chat_id=CHAT_ID, sticker=random.choice(stickers))
