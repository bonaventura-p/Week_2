'''
#turtle basic
from turtle import *

color('red','yellow')
shape('turtle')


begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()

#
def hexagon(length):
	pd()
	fd(length)
	left(60)

for _ in range(6):
	hexagon(length)



#
class Girl(object):
	def __init__(self,sounds):
		self.sounds=sounds
	def cry_baby(self):
		for sound in self.sounds:
			print "{}eee".format(sound)

class Boy(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def cry_baby(self):
        for sound in self.sounds:
            print "{}m".format(sound)

    def play_with_toy(self):
        print "I'm going to play with a toy"#quite tedious process, we can speed it up

#
class Child(object):
    def __init__(self, sounds):
        self.sounds = sounds
	def cry_baby(self):
        for sound in self.sounds:
        	print "{}m".format(sound) 

class Boy(Child): # The Child class is the parent of the Boy class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Boy, self).__init__(["Twang", "Thrumb", "Bling", "mommy"])

class Girl(Child):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Girl, self).__init__(["Boink", "Bow", "Boom", "Mommy"])

    def drink_milk(self):
        print "I'm going to drink Milk"
        print "Twoning, sproing, splang splart... "

#linear search
x=[1,2,3,5,4,10]
target=5
def linear_search(x,target):
	position=-1
	count=0
	while count <len(x):
		if x[count]==target:
			position=count
		count +=1
	if position ==-1:
		print "Target {} hasn't been found".format(target)
	else:
		print "Target {} found at position{}",format(target,position)
   #the output is 3 and indeed 5 is at position 3
#recall we start counting from 0
'''
#binary search

def median(x):
	x=sorted(x)
	if len(x)%2==0:
		return float(sum(x[(len(x)/2)-1:(len(x)/2)+1]))/2.0
	else:
		return x[((len(x)+1)/2)-1]

target=5
x=[0,1,2,3,4,5,7,8]
def binary_search(x,target):
	midpoint=int(median(x))
	if x==[]:
		minx=0
	else:
		minx=min(x)
	if x==[]:
		maxx=0
	else:
		maxx=max(x)	
	if target >maxx or target <minx:
		return "Not in the list"
	if target<midpoint:
		x=x[minx:midpoint-1]
		binary_search(x,target)
	elif target > midpoint:
		x=x[midpoint+1:maxx]
		binary_search(x,target)
	elif target==midpoint:
		 position=midpoint
		 print position

def binary_search1(x,target):
	if x==[]:
		minx=0
	else:
		minx=min(x)
	if x==[]:
		maxx=0
	else:
		maxx=max(x)	
	while True:
    	if maxx < minx:
        	return -1
        midpoint = (minx + maxx) // 2
        if x[midpoint] < target:
            minx = midpoint + 1
        elif x[midpoint] > target:
            maxx = midpoint - 1
        else:
            return midpoint
			















