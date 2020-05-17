from random import choice, randint
from . import text
import os



class RandomWordGenerator(object):
	def randomAdjective(self):
		'''
		Returns adjective at random
		'''
		return choice(text.adj.split("\n"))
			
	def randomNoun(self):
		'''
		Returns noun at random
		'''
		return choice(str(text.noun).split("\n"))
			
	def randomUserName(self, num=False):
		'''
		Returns a random username, much in the style of Xbox Randomly Generated Usernames.
		
		(optional) num: Decides if numbers are appended to end
		'''
		
		return f"{self.randomAdjective().title()}{self.randomNoun().title()}{randint(0, 9999)}"