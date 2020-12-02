#from _ import *
import random

class Game:
	def __init__(self, AI_Count = 0):
		if(AI_Count == 0):
			#if not input randomly decide AI_Count
			AI_Count = randrange(2,6,1);
