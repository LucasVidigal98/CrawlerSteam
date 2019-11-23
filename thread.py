import threading
from Crawler import *

class ThreadGame(threading.Thread):

	def __init__(self, idThread):
		self.idThread = idThread
		threading.Thread.__init__(self)

	def run(self):

		if self.idThread == 1:
			crawler_init(self.idThread, 400000)

		if self.idThread == 2:
			crawler_init(self.idThread, 800000)

		if self.idThread == 3:
			crawler_init(self.idThread, 1200000)
