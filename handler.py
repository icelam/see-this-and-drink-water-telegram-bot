import telegram
import sys
import json
import os
import random

# Load environment variables
TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

with open('messages.txt') as file:
  lines = file.readlines()
  messages = [line.rstrip() for line in lines]

# Send a message
def send_message(event, context):
  bot = telegram.Bot(token = TOKEN)
  bot.sendMessage(chat_id = CHAT_ID, text = random.choice(messages))
