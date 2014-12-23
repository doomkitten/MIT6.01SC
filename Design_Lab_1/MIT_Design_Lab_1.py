#Write the definition of a Python procedure fib, such that fib(n) returns
#the nth Fibonacci number.

def fib(n):
	if n < 0: return 0
	elif n == 0: return 0
	elif n == 1: return 1
	return fib(n-1) + fib (n-2)


class V2(object): 
	
	def __init__(self, x = 0, y = 0):
		self.coords = [x , y]
		
	def __str__(self):
		return str(self.coords)
		
	def getX(self):
		return self.coords[0]
	
	def getY(self):
		return self.coords[1]
	
	def __add__(self, v):
		return self.add(v)
	
	def add(self, v):
		return V2(self.getX()+v.getX(), self.getY()+v.getY())	
	
	def __mul__(self, scalar):
		return self.mul(scalar)
	
	def __rmul__(self, scalar):
		return self.mul(scalar)

	def mul(self, scalar):
		return V2(scalar * self.getX(), scalar * self.getY())		

v1 = V2(4,5)
v2 = V2(3,6)
print(v1)
print(v2)
v3 = v1 + v2
print(v3)
v3 = v1 * 4
v4 = 4 * v2
print(v3)
print(v4)

