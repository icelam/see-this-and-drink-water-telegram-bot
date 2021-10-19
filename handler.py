"""Lambda function file for sending scheduled message to a connected Telegram chat via Chat ID."""

import os
import random
import telegram

# Load environment variables
TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

with open('messages.txt', encoding='utf8') as file:
    lines = file.readlines()
    messages = [line.rstrip() for line in lines]

def send_message(event, context):
    """Lambda function handler to send text message."""
    bot = telegram.Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=random.choice(messages))
