import random
import kon
import sys
from kon import *
class board(object):
	def __init__(self,x):
		self.x=x
		self.score=0

	def getcoin(self):
		while self.x<=29:
			j=0
			while j <4:	
				h=random.randint(1,77)
				if matrix[self.x+1][h] == "X" and matrix[self.x][h]!="H":
					matrix[self.x][h]="C"
					j=j+1
			self.x=self.x+4
coins=board(4)
coins.getcoin()	
	



