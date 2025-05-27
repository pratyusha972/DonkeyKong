import os 
from kon import *
from con import *
import random
from threading import Thread
import time
from multiprocessing import Process

class Person(object):
     	def __init__(self, x, y, score, playerflag, donkeyflag):
		self.x = x
		self.y = y
		self.score = score
		self.playerflag = playerflag
		self.donkeyflag = donkeyflag

	def life(self):
		self.life = 3

	def display_info(self):
		 for i in range(0,30):
			for j in range(0,79):
			        sys.stdout.write(matrix[i][j])
			print
		 print "SCORE =", self.score 
		 print "LIFES =", self.life

	def checkwall(self, inp):
		if inp == "a" :
			if self.y == 1:
				return 1
			return 0
		elif inp == "d" :
			if self.y == 77:
				return 1
			return 0

	def getcoin(self, a, b):
		if matrix[a][b]=="C":
			self.score = self.score+5
			
	def firedon(self, a, b, inp):
		o = matrix[a][b]
		if self.donkeyflag == 1:
			matrix[a][b] = matrix[self.x][self.y]
			matrix[self.x][self.y] = "C"
			self.donkeyflag = 0
			self.y = b
		elif self.donkeyflag == 0:
			self.getposition(inp, a, b, self.playerflag)
		if o == "C":
			self.donkeyflag = 1
		if o == "H":
			self.playerflag = 1

	def jumpmain(self, i, j, a, b):
		r = matrix[i][j]
		matrix[i][j] = matrix[a][b]
		if self.playerflag == 1:
			matrix[self.x][self.y] = "H"
			self.playerflag = 0
		else:
			matrix[self.x][self.y] = " "
		if r=="H":
			self.playerflag = 1
		self.x = i
		self.y = j
		
	def getsub(self, j, h, a, b):
		self.jumpmain(j,h,a,b)
		os.system("clear")
		self.display_info()
		time.sleep(0.4)
		
	def getposition(self, inp, x, y, playerflag):
		if (matrix[self.x+1][self.y] == "X" or matrix[self.x+1][self.y] == "H"):
			if self.checkwall(inp) != 1:
				if inp == "a":
					if matrix[self.x+1][self.y-1] == "X" or matrix[self.x+1][self.y-1] == "H": 
						self.jumpmain(self.x,self.y-1,self.x,self.y)
				elif inp=="d":
					if matrix[self.x+1][self.y+1]=="X" or matrix[self.x+1][self.y+1]=="H": 
						self.jumpmain(self.x,self.y+1,self.x,self.y)

	def updown(self,inp,x,y,playerflag):
		if inp=="s":
			if matrix[self.x+1][self.y]=="H":
				self.jumpmain(self.x+1,self.y,self.x,self.y)
		elif inp=="w":
			if (matrix[self.x-1][self.y]==" " and (matrix[self.x][self.y+1]=="X" or matrix[self.x][self.y-1]=="X")) or (matrix[self.x-1][self.y]=="H"):
				self.jumpmain(self.x-1,self.y,self.x,self.y)

	def jump(self,x,y,inp):
		if (matrix[self.x+1][self.y]=="X" or matrix[self.x+1][self.y]=="H"):
			if inp=="d":
				if(matrix[self.x-1][self.y+1]!="X" and matrix[self.x-2][self.y+2]!="X" and matrix[self.x-1][self.y+3]!="X" and matrix[self.x][self.y+4]!="X"):
						if matrix[self.x+1][self.y+1]==" " or matrix[self.x+1][self.y+2]==" " or matrix[self.x+1][self.y+3]==" " or matrix[self.x+1][self.y+4]==" ":
							self.getsub(self.x-1,self.y+1,self.x,self.y)
							self.getsub(self.x-1,self.y+1,self.x,self.y)
							for i in range(1,7):
								self.getsub(self.x+1,self.y+1,self.x,self.y)
						else:
							self.getsub(self.x-1,self.y+1,self.x,self.y)
							self.getsub(self.x-1,self.y+1,self.x,self.y)
							self.getsub(self.x+1,self.y+1,self.x,self.y)
							self.getsub(self.x+1,self.y+1,self.x,self.y)
				else:
					if(matrix[self.x-1][self.y+1]!="X" and matrix[self.x-1][self.y+2]!="X" and matrix[self.x-1][self.y+3]!="X" and (matrix[self.x][self.y+4]=="X" )):
						self.getsub(self.x-1,self.y+1,self.x,self.y)
						self.getsub(self.x,self.y+1,self.x,self.y)
						self.getsub(self.x+1,self.y+1,self.x,self.y)
					elif(matrix[self.x-1][self.y+1]!="X" and matrix[self.x-2][self.y+2]!="X" and matrix[self.x+1][self.y+2]!=" " and (matrix[self.x-1][self.y+3]=="X")):
						self.getsub(self.x-1,self.y+1,self.x,self.y)
						self.getsub(self.x+1,self.y+1,self.x,self.y)
					elif(matrix[self.x-1][self.y+1]!="X" and (matrix[self.x-2][self.y+2]=="X")):
						self.getsub(self.x-1,self.y+1,self.x,self.y)
						self.getsub(self.x+1,self.y,self.x,self.y)
					elif(matrix[self.x-1][self.y+1]=="X"):
						self.getsub(self.x-1,self.y,self.x,self.y)
						self.getsub(self.x+1,self.y,self.x,self.y)
			elif inp=="a":
				if(matrix[self.x-1][self.y-1]!="X" and matrix[self.x-2][self.y-2]!="X" and matrix[self.x-1][self.y-3]!="X" and matrix[self.x][self.y-4]!="X"):
						if matrix[self.x+1][self.y-1]==" " or matrix[self.x+1][self.y-2]==" " or matrix[self.x+1][self.y-3]==" " or matrix[self.x+1][self.y-4]==" ":

							self.getsub(self.x-1,self.y-1,self.x,self.y)
							self.getsub(self.x-1,self.y-1,self.x,self.y)
							for i in range(1,7):
								self.getsub(self.x+1,self.y-1,self.x,self.y)
						else:
							self.getsub(self.x-1,self.y-1,self.x,self.y)
							self.getsub(self.x-1,self.y-1,self.x,self.y)
							self.getsub(self.x+1,self.y-1,self.x,self.y)
							self.getsub(self.x+1,self.y-1,self.x,self.y)
				else:
					if(matrix[self.x-1][self.y-1]!="X" and matrix[self.x-2][self.y-2]!="X" and matrix[self.x-1][self.y-3]!="X" and matrix[self.x][self.y-4]=="X"):
						self.getsub(self.x-1,self.y-1,self.x,self.y)
						self.getsub(self.x,self.y-1,self.x,self.y)
						self.getsub(self.x+1,self.y-1,self.x,self.y)
					elif(matrix[self.x-1][self.y-1]!="X" and matrix[self.x-2][self.y-2]!="X" and matrix[self.x-1][self.y-3]=="X"):
						self.getsub(self.x-1,self.y-1,self.x,self.y)
						self.getsub(self.x+1,self.y-1,self.x,self.y)
					elif(matrix[self.x-1][self.y-1]!="X" and matrix[self.x-2][self.y-2]=="X"):
						self.getsub(self.x-1,self.y-1,self.x,self.y)
						self.getsub(self.x+1,self.y,self.x,self.y)
					elif(matrix[self.x-1][self.y-1]=="X"):
						self.getsub(self.x-1,self.y,self.x,self.y)
						self.getsub(self.x+1,self.y,self.x,self.y)

class Player(Person):
	def __init__(self, x, y, score, playerflag, donkeyflag):
		Person.__init__(self, x, y, score, playerflag, donkeyflag)
	
	def jumpmain(self, i, j, a, b):
		r = matrix[i][j]
		matrix[i][j] = matrix[a][b]
		if self.playerflag == 1:
			matrix[self.x][self.y] = "H"
			self.playerflag = 0
		else:
			matrix[self.x][self.y] = " "
		if r == "H":
			self.playerflag = 1;
		self.x = i
		self.y = j
		if r == "O" or r == "D":
			self.chill(r)
			
	def chill(self, cha):
		if cha=="D":
			matrix[self.x][self.y]="D"
		else:
			matrix[self.x][self.y]="O"
		self.x=28
	 	self.y=1
	 	matrix[28][1]="P"
	 	self.life=self.life-1
	 	os.system("clear")
 		self.display_info()
	 	print "PLAYER DIED!"

class Donkey(Person):
     	def __init__(self,x,y,score,playerflag,donkeyflag):
		Person.__init__(self,x,y,score,playerflag,donkeyflag)

	def position(self,x,y,playerflag,donkeyflag):
			if player.x==self.x and player.y-1==self.y:
		 		player.score=player.score-25
		 		if player.playerflag==1:
		 			matrix[player.x][player.y]="H"
		 			player.playerflag=0
		 		else:	
		 			matrix[player.x][player.y]=" "
		 		player.x=28
		 		player.y=1
		 		matrix[28][1]="P"
		 		matrix[self.x][self.y]="D"
		 		player.life=player.life-1
		 		player.display_info()
		 		print "PLAYER DIED!"
			else:
				h=random.randint(18,59)
				if h < self.y:
					if self.checkwall("a")!=1:
						self.firedon(self.x,self.y-1,"a")
				elif h >= self.y:
					if self.checkwall("d")!=1:
						self.firedon(self.x,self.y+1,"d")
class Fireball(Person):
        def __init__(self,x,y,score,playerflag,donkeyflag):
		Person.__init__(self,x,y,score,playerflag,donkeyflag)
	def jumpmain(self,i,j,a,b):
		r=matrix[i][j]
		matrix[i][j]=matrix[a][b]
		if self.playerflag==1:
			matrix[self.x][self.y]="H"
			self.playerflag=0
		else:
			matrix[self.x][self.y]=" "
		if r=="H":
			self.playerflag=1
		elif r=="C":
			self.donkeyflag=1
		elif r=="P":
			player.x=28
			player.y=1
			matrix[28][1]="P"
			matrix[self.x][self.y]=" "
		self.x=i
		self.y=j
	def kill(self,x,y,playerflag,donkeyflag):
		flag=0
		if  player.x==self.x and (player.y==self.y  or player.y==self.y+1 or player.y==self.y-1) :
			matrix[self.x][self.y]="O"
			player.x=28
			player.y=1
			matrix[28][1]="P"
		while matrix[self.x+1][self.y+1]!=" ":
			if matrix[self.x+1][self.y+1]=="H" and matrix[self.x+2][self.y+1]=="H" and matrix[self.x+3][self.y+1]=="H" and matrix[self.x+4][self.y+1]=="H":
				flag=1
				time.sleep(0.1)
				self.firedon(self.x,self.y+1,"d")
				for i in range(1,5):
					time.sleep(0.2)
					self.updown("s",self.x,self.y,self.playerflag)
				break
			time.sleep(0.02)
			self.firedon(self.x,self.y+1,"d")
		if matrix[self.x+1][self.y+1]==" " and flag!=1:
			self.jump(self.x,self.y,"d")
		u=2
	 	limit=random.randint(50,150)
       		big=0		  
		while (u):
		   	flag=0
			gone=0
			if self.x=="28" and self.y=="1" :
				matrix[28][1]=" "
				return
			else:			  
				h=random.randint(1,3)
				if h==1:
			  		while matrix[self.x][self.y-1]!="X" and  matrix[self.x+1][self.y-1]!=" ":
						if matrix[self.x+1][self.y-1]=="H" and matrix[self.x+2][self.y-1]=="H" and matrix[self.x+3][self.y-1]=="H" and matrix[self.x+4][self.y-1]=="H":
							flag=1
							time.sleep(0.2)
							self.firedon(self.x,self.y-1,"a")
							for i in range(1,6):
								time.sleep(0.2)
								self.updown("s",self.x,self.y,self.playerflag)
							break
						time.sleep(0.2)		
						self.firedon(self.x,self.y-1,"a")
						big=big+1
						if big>limit:
						   return
					if flag!=1 and matrix[self.x][self.y-1]=="X":
						while matrix[self.x+1][self.y+1]!=" ":
							if matrix[self.x+1][self.y+1]=="H" and matrix[self.x+2][self.y+1]=="H" and matrix[self.x+3][self.y+1]=="H" and matrix[self.x+4][self.y+1]=="H":
								flag=1
								time.sleep(0.2)
								self.firedon(self.x,self.y+1,"d")
								for i in range(1,6):
									time.sleep(0.2)
									self.updown("s",self.x,self.y,self.playerflag)
								break
							time.sleep(0.2)
							self.firedon(self.x,self.y+1,"d")
							big=big+1
							if big>limit:
							  	 return
					elif matrix[self.x+1][self.y-1]==" " and flag!=1:
				    		self.jump(self.x,self.y,"a")
				elif h==2:	    
			  		while matrix[self.x][self.y+1]!="X" and  matrix[self.x+1][self.y+1]!=" ":
						if matrix[self.x+1][self.y+1]=="H" and matrix[self.x+2][self.y+1]=="H" and matrix[self.x+3][self.y+1]=="H" and matrix[self.x+4][self.y+1]=="H":
							flag=1
							time.sleep(0.2)
							self.firedon(self.x,self.y+1,"d")
					   		for i in range(1,6):
				   		        	time.sleep(0.1)
								self.updown("s",self.x,self.y,self.playerflag)
							break
						time.sleep(0.2)
						self.firedon(self.x,self.y+1,"d")
						big=big+1
						if big>limit:
							return
					if flag!=1 and matrix[self.x+1][self.y+1]=="X":
						while matrix[self.x+1][self.y-1]!=" ":
							if matrix[self.x+1][self.y-1]=="H" and matrix[self.x+2][self.y-1]=="H" and matrix[self.x+3][self.y-1]=="H" and matrix[self.x+4][self.y-1]=="H":
								flag=1
								time.sleep(0.2)
								self.firedon(self.x,self.y-1,"a")
								for i in range(1,6):
									time.sleep(0.2)
									self.updown("s",self.x,self.y,self.playerflag)
								break
							time.sleep(0.2)
						        self.firedon(self.x,self.y-1,"a")	
							big=big+1
							if big>limit:
								return
					elif matrix[self.x+1][self.y+1]==" " and flag!=1:
				    		self.jump(self.x,self.y,"d")


#startgame
donkey=Donkey(4,1,0,0,0)			
player=Player(28,1,0,0,0)
player.life()
matrix[4][1]="D"
matrix[28][1]="P"
matrix[donkey.x][donkey.y+1]="O"
os.system("clear")
player.display_info()

def mulfire():
	u=8
	fireball_list=[Fireball(donkey.x,donkey.y+1,0,0,0)]
	count=0
	while(u):
		fireball_list[count].kill(donkey.x,donkey.y+1,0,0)
		fireball_list=fireball_list + [Fireball(donkey.x,donkey.y+1,0,0,0)]
		matrix[donkey.x][donkey.y+1]="O"
		count=count+1

def func():
	os.system("stty cbreak -echo")
	inp= sys.stdin.read(1)
	os.system("stty -cbreak echo")
	while(inp!="q" and player.life>0):
		if matrix[player.x][player.y-1]=="Q":
			print "YOU WON"
			break
		if ((player.x==donkey.x and player.y-1==donkey.y) or (matrix[player.x][player.y+1]=="O" or matrix[player.x][player.y-1]=="O" or matrix[player.x][player.y]=="O")):
		 	player.score=player.score-25
		 	if player.playerflag==1:
		 		matrix[player.x][player.y]="H"
		 		player.playerflag=0
		 	else:	
		 		matrix[player.x][player.y]=" "
			player.x=28
		 	player.y=1
		 	matrix[28][1]="P"
		 	matrix[donkey.x][donkey.y]="D"
		 	player.life=player.life-1
			os.system("clear")
			donkey.position(donkey.x,donkey.y,donkey.playerflag,donkey.donkeyflag)
			player.display_info()
		 	print "PLAYER DIED!"
		else:
			if inp==" ":
				os.system("stty cbreak -echo")
				inp= sys.stdin.read(1)
				os.system("stty -cbreak echo")
				player.jump(player.x,player.y,inp)	
			else:
				if inp=="a":
					player.getcoin(player.x,player.y-1)
				elif inp=="d":	
					player.getcoin(player.x,player.y+1)
				if inp=="a" or inp=="d":
					player.getposition(inp,player.x,player.y,player.playerflag)
				elif inp=="s" or inp=="w":
					player.updown(inp,player.x,player.y,player.playerflag)
				os.system("clear")
				donkey.position(donkey.x,donkey.y,donkey.playerflag,donkey.donkeyflag)
				player.display_info()
		os.system("stty cbreak -echo")
		inp= sys.stdin.read(1)
		os.system("stty -cbreak echo")
		if player.life==0:
			print "YOU LOST"
			print "GAME OVER"
			break

if __name__ == "__main__": 
	Thread(target=func).start()
	#Thread(target=die.kill(donkey.x,donkey.y+1,0,0)).start()
	Thread(target=mulfire).start()
