#From MIT.601SC Design Lab 1
#Class Vector2D is a class representing a 2D Vector
#For more information regarding this problem, see
#http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011unit-1-software-engineering/object-oriented-programming/MIT6_01SCS11_designLab01.pdf

class Vector2D(object): 
	
	def __init__(self, x = 0, y = 0):
		self.coords = [x , y]
		
	def __str__(self):
		return "Vector2D: " + str(self.coords)
		
	def __repr__(self):
		return str(self.coords)
		
	def getX(self):
		return self.coords[0]
	
	def getY(self):
		return self.coords[1]
	
	def __add__(self, v):
		return self.add(v)
	
	def add(self, v):
		return Vector2D(self.getX()+v.getX(), self.getY()+v.getY())	
	
	def __mul__(self, scalar):
		return self.mul(scalar)
	
	def __rmul__(self, scalar):
		return self.mul(scalar)

	def mul(self, scalar):
		return Vector2D(scalar * self.getX(), scalar * self.getY())		

#Tests
a = Vector2D(3,4)
b = Vector2D(7,12)
print "a: " + str(a)
print "b: " + str(b)
print "getX a:" + str(a.getX())
print "getY a:" + str(a.getY())
print "a + b: " + str(a+b)
print "a * 3: " + str(a*3)
print "3 * a: " + str(3*a)





