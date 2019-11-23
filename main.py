from thread import ThreadGame
from Crawler import *


t1 = ThreadGame(1)
t2 = ThreadGame(2)
t3 = ThreadGame(3)

t1.start()
t2.start()
t3.start()