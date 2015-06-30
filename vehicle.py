class Vehicle(object):
	def __init__(self,name,number_of_wheels,engine_type):
		self.name=name
		self.number_of_wheels=number_of_wheels
		self.engine_type=engine_type


class Truck(Vehicle):
 	def __init__(self):
 		super(Truck,self).__init__("truck","6","diesel")

class Car(Vehicle):
	def __init__(self):
		super(Car,self).__init__("car","4","gasoline")


