"""Lambda function file for sending scheduled message to a connected Telegram chat via Chat ID."""

import os
import random
import telegram

SRC_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
MESSAGE_TEXT_FILE_PATH = os.path.join(SRC_FOLDER_PATH, 'messages.txt')

# Load environment variables
TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

# Get messages from file and put it into list
try:
    with open(MESSAGE_TEXT_FILE_PATH, encoding='utf8') as file:
        lines = file.readlines()
        messages = [line.rstrip() for line in lines]
except FileNotFoundError:
    messages = ['見字飲水！']

def send_message(event, context):
    """Lambda function handler to send text message."""
    bot = telegram.Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=random.choice(messages))
