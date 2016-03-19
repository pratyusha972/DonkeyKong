import os 
import kon
from kon import *
import con
from con import *
import random
import threading
from threading import Thread
import time
from time import sleep
from multiprocessing import Process
class person(object):
     	def __init__(self,x,y,score,plaflag,donflag):
		self.x=x
		self.y=y
		self.score=score
		self.plaflag=plaflag
		self.donflag=donflag

	def life(self):
		self.life=3

	def prin(self):
		 for i in range(0,30):
			for j in range(0,79):
			        sys.stdout.write(matrix[i][j])
			print
		 print "SCORE =", self.score 
		 print "LIFES =", self.life

	def checkwall(self,inp):
		if inp == "a" :
			if self.y == 1:
				return 1
			return 0
		elif inp == "d" :
			if self.y == 77:
				return 1
			return 0

	def getcoin(self,a,b):
		if matrix[a][b]=="C":
			self.score = self.score+5
	def firedon(self,a,b,inp):
		o=matrix[a][b]
		if self.donflag==1:
			matrix[a][b]=matrix[self.x][self.y]
			matrix[self.x][self.y]="C"
			self.donflag=0
			self.y=b
		elif self.donflag==0:
			self.getposition(inp,a,b,self.plaflag)
		if o=="C":
			self.donflag=1
		if o=="H":
			self.plaflag=1

	def jumpmain(self,i,j,a,b):
		r=matrix[i][j]
		matrix[i][j]=matrix[a][b]
		if self.plaflag==1:
			matrix[self.x][self.y]="H"
			self.plaflag=0
		else:
			matrix[self.x][self.y]=" "
		if r=="H":
			self.plaflag=1;
		self.x=i
		self.y=j
	def getsub(self,j,h,a,b):
		self.jumpmain(j,h,a,b)
		os.system("clear")
		self.prin()
		time.sleep(0.4)
	def getposition(self,inp,x,y,plaflag):
		if (matrix[self.x+1][self.y]=="X" or matrix[self.x+1][self.y]=="H"):
			if self.checkwall(inp)!=1:
				if inp=="a":
					if matrix[self.x+1][self.y-1]=="X" or matrix[self.x+1][self.y-1]=="H": 
						self.jumpmain(self.x,self.y-1,self.x,self.y)
				elif inp=="d":
					if matrix[self.x+1][self.y+1]=="X" or matrix[self.x+1][self.y+1]=="H": 
						self.jumpmain(self.x,self.y+1,self.x,self.y)

	def updown(self,inp,x,y,plaflag):
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

class player(person):
	def __init__(self,x,y,score,plaflag,donflag):
		person.__init__(self,x,y,score,plaflag,donflag)
	def jumpmain(self,i,j,a,b):
		r=matrix[i][j]
		matrix[i][j]=matrix[a][b]
		if self.plaflag==1:
			matrix[self.x][self.y]="H"
			self.plaflag=0
		else:
			matrix[self.x][self.y]=" "
		if r=="H":
			self.plaflag=1;
		self.x=i
		self.y=j
		if r=="O" or r=="D":
			self.chill(r)
	def chill(self,cha):
		if cha=="D":
			matrix[self.x][self.y]="D"
		else:
			matrix[self.x][self.y]="O"
		self.x=28
	 	self.y=1
	 	matrix[28][1]="P"
	 	self.life=self.life-1
	 	os.system("clear")
 		self.prin()
	 	print "PLAYER DIED!"
class donkey(person):
     	def __init__(self,x,y,score,plaflag,donflag):
		person.__init__(self,x,y,score,plaflag,donflag)

	def position(self,x,y,plaflag,donflag):
			if harry.x==self.x and harry.y-1==self.y:
		 		harry.score=harry.score-25
		 		if harry.plaflag==1:
		 			matrix[harry.x][harry.y]="H"
		 			harry.plaflag=0
		 		else:	
		 			matrix[harry.x][harry.y]=" "
		 		harry.x=28
		 		harry.y=1
		 		matrix[28][1]="P"
		 		matrix[self.x][self.y]="D"
		 		harry.life=harry.life-1
		 		harry.prin()
		 		print "PLAYER DIED!"
			else:
				h=random.randint(18,59)
				if h < self.y:
					if self.checkwall("a")!=1:
						self.firedon(self.x,self.y-1,"a")
				elif h >= self.y:
					if self.checkwall("d")!=1:
						self.firedon(self.x,self.y+1,"d")
class fireball(person):
        def __init__(self,x,y,score,plaflag,donflag):
		person.__init__(self,x,y,score,plaflag,donflag)
	def jumpmain(self,i,j,a,b):
		r=matrix[i][j]
		matrix[i][j]=matrix[a][b]
		if self.plaflag==1:
			matrix[self.x][self.y]="H"
			self.plaflag=0
		else:
			matrix[self.x][self.y]=" "
		if r=="H":
			self.plaflag=1
		elif r=="C":
			self.donflag=1
		elif r=="P":
			harry.x=28
			harry.y=1
			matrix[28][1]="P"
			matrix[self.x][self.y]=" "
		self.x=i
		self.y=j
	def kill(self,x,y,plaflag,donflag):
		flag=0
		if  harry.x==self.x and (harry.y==self.y  or harry.y==self.y+1 or harry.y==self.y-1) :
			matrix[self.x][self.y]="O"
			harry.x=28
			harry.y=1
			matrix[28][1]="P"
		while matrix[self.x+1][self.y+1]!=" ":
			if matrix[self.x+1][self.y+1]=="H" and matrix[self.x+2][self.y+1]=="H" and matrix[self.x+3][self.y+1]=="H" and matrix[self.x+4][self.y+1]=="H":
				flag=1
				time.sleep(0.1)
				self.firedon(self.x,self.y+1,"d")
				for i in range(1,5):
					time.sleep(0.2)
					self.updown("s",self.x,self.y,self.plaflag)
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
								self.updown("s",self.x,self.y,self.plaflag)
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
									self.updown("s",self.x,self.y,self.plaflag)
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
								self.updown("s",self.x,self.y,self.plaflag)
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
									self.updown("s",self.x,self.y,self.plaflag)
								break
							time.sleep(0.2)
						        self.firedon(self.x,self.y-1,"a")	
							big=big+1
							if big>limit:
								return
					elif matrix[self.x+1][self.y+1]==" " and flag!=1:
				    		self.jump(self.x,self.y,"d")

jimmy=donkey(4,1,0,0,0)			
harry=player(28,1,0,0,0)
harry.life()
matrix[4][1]="D"
matrix[28][1]="P"
matrix[jimmy.x][jimmy.y+1]="O"
os.system("clear")
harry.prin()
def mulfire():
	u=8
	ellie=[fireball(jimmy.x,jimmy.y+1,0,0,0)]
	count=0
	while(u):
		ellie[count].kill(jimmy.x,jimmy.y+1,0,0)
		ellie=ellie + [fireball(jimmy.x,jimmy.y+1,0,0,0)]
		matrix[jimmy.x][jimmy.y+1]="O"
		count=count+1
def func():
	os.system("stty cbreak -echo")
	inp= sys.stdin.read(1)
	os.system("stty -cbreak echo")
	while(inp!="q" and harry.life>0):
		if matrix[harry.x][harry.y-1]=="Q":
			print "YOU WON"
			break
		if ((harry.x==jimmy.x and harry.y-1==jimmy.y) or (matrix[harry.x][harry.y+1]=="O" or matrix[harry.x][harry.y-1]=="O" or matrix[harry.x][harry.y]=="O")):
		 	harry.score=harry.score-25
		 	if harry.plaflag==1:
		 		matrix[harry.x][harry.y]="H"
		 		harry.plaflag=0
		 	else:	
		 		matrix[harry.x][harry.y]=" "
			harry.x=28
		 	harry.y=1
		 	matrix[28][1]="P"
		 	matrix[jimmy.x][jimmy.y]="D"
		 	harry.life=harry.life-1
			os.system("clear")
			jimmy.position(jimmy.x,jimmy.y,jimmy.plaflag,jimmy.donflag)
			harry.prin()
		 	print "PLAYER DIED!"
		else:
			if inp==" ":
				os.system("stty cbreak -echo")
				inp= sys.stdin.read(1)
				os.system("stty -cbreak echo")
				harry.jump(harry.x,harry.y,inp)	
			else:
				if inp=="a":
					harry.getcoin(harry.x,harry.y-1)
				elif inp=="d":	
					harry.getcoin(harry.x,harry.y+1)
				if inp=="a" or inp=="d":
					harry.getposition(inp,harry.x,harry.y,harry.plaflag)
				elif inp=="s" or inp=="w":
					harry.updown(inp,harry.x,harry.y,harry.plaflag)
				os.system("clear")
				jimmy.position(jimmy.x,jimmy.y,jimmy.plaflag,jimmy.donflag)
				harry.prin()
		os.system("stty cbreak -echo")
		inp= sys.stdin.read(1)
		os.system("stty -cbreak echo")
		if harry.life==0:
			print "YOU LOST"
			print "GAME OVER"
			break
if __name__ == "__main__": 
	Thread(target=func).start()
#Thread(target=die.kill(jimmy.x,jimmy.y+1,0,0)).start()
	Thread(target=mulfire).start()
