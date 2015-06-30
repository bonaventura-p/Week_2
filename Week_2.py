
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

