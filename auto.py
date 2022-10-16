from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from time import sleep
from apscheduler.schedulers.background import BlockingScheduler
import requests
import json
import telegram


TELE_TOKEN = '5686234341:AAHdwKPVrqcQ7NWi-hAx0-qkzodVfcacN0M'#taipm_bot
CHAT_ID = '1133501778'

updater = Updater(TELE_TOKEN, use_context=True)

def notify_ending(message):
	
	bot = telegram.Bot(token=TELE_TOKEN)
	rs = bot.sendMessage(chat_id=CHAT_ID, text=message)
	file_path='./img.png'
	bot.send_photo(chat_id=CHAT_ID, photo=open(file_path, 'rb'))
	print(rs)

notify_ending(message="Hello, teo")
# Creates a default Background Scheduler
sched = BlockingScheduler()

def prompt():
	notify_ending(message="Tự động đây")
 
prompt()
sched.add_job(prompt,'interval', seconds=15) 
sched.start()