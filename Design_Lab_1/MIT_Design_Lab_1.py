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
		return "V2" + str(self.coords)
		
	def __repr__(self):
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

class Polynomial(object):
	
	def __init__(self, coefficients):
		self.coeffs = [float(i) for i in coefficients]
				
	def __repr__(self):
		return str(self.coeffs)
		
	@staticmethod
	def exponent(n):
		return -(n+1)
	
	def coeff(self, i):
		return self.coeffs[exponent(i)]	
			
	def mul(a,b):
		return Polynomial(self.listMul(self.coeffs, other.coeffs))
	
	@staticmethod
	def listMul(a, b):
		zeros = abs(len(a)- len(b))
		if (len(a) > len(b)):
			return [i*j for i,j in zip(a,[0]*zeros+b)] 
		else: 
			return [i*j for i,j in zip(b,[0]*zeros+a)]
		
	def add(self, other):
		return Polynomial(self.listAdd(self.coeffs, other.coeffs))
		
	@staticmethod
	def listAdd(a, b):
		zeros = abs(len(a)- len(b))
		if (len(a) > len(b)):
			return [i+j for i,j in zip(a,[0]*zeros+b)] 
		else: 
			return [i+j for i,j in zip(b,[0]*zeros+a)]
	
	def val(self, x):
		return self.valRecurse(self.coeffs, x)
	
	#Recursive Solution using Horner's Rule 
	@staticmethod
	def valRecurse(poly, x):
		if len(poly) == 1:
			return poly[0]
		else:
			return poly[-1] + x*Polynomial.valRecurse(poly[0:len(poly)-1], x)
			
	def roots(self):
		length = len(self.coeffs)
		if length > 3:
			return []
		else
			b = self.coeffs[1]
			c = self.coeffs[-1]
		
		if len(self.coeffs) == 3:
			a = self.coeffs[0]
			discriminant = b**2 - 4*a*c
			plusroot = (-b + complex(discriminant)**0.5)/2*a
			minusroot = (-b - complex(discriminant)**0.5)/2*a
			return [plusroot, minusroot]
		else: 
			return [-c/b]
		
		
a = Polynomial([1, 2, 3])
b = Polynomial([1, 2, 3, 4])
print a.add(b)
print a.roots()

	
		


	
