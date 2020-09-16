import sys
import time
import telepot
import pyautogui
import threading
from telepot.loop import MessageLoop
from tokens import *

class MyBot(telepot.Bot):
	def __init__(self, *args, **kwargs):
		super(MyBot, self).__init__(*args, **kwargs)
		self.answerer = telepot.helper.Answerer(self)
		self._message_with_inline_keyboard = None
		

	def autocapt(self,msg):
		content_type, chat_type, chat_id = telepot.glance(msg)
		# For debugging and get admin id
		print(content_type, chat_type, chat_id)

		bot.sendChatAction(chat_id, 'typing')
		bot.sendMessage(chat_id, "Capturing image")
		self.capture_img()
		bot.sendPhoto(chat_id, photo=open('img\\screenshot.png', 'rb'))
		
	def on_chat_message(self, msg):
		content_type, chat_type, chat_id = telepot.glance(msg)

		if chat_id:
			if content_type == 'text':
				if msg['text'] == '/start':
					global eventStarted
					eventStarted = False
					if not eventStarted:
						eventStarted = True
						def each_time():
							self.autocapt(msg)
							time.sleep(900)
							each_time()

						each_time()
					else:
						print("event is running")
				else:
					print("i wont send anything")

		else:
			bot.sendMessage(chat_id, "Not admin")

	def capture_img(self):
		pic = pyautogui.screenshot()
		pic.save('img\\screenshot.png')
		return
	
TOKEN = telegrambot

bot = MyBot(TOKEN)
MessageLoop(bot).run_as_thread()
# Umcomment for debugging
print('Listening ...')

while 1:
	time.sleep(1)