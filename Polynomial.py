#From MIT.601SC Design Lab 1
#Class Polynomial is a class representing a polynomial of degree n
#For more information regarding this problem, see
#http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011unit-1-software-engineering/object-oriented-programming/MIT6_01SCS11_designLab01.pdf


class Polynomial(object):
	
	#Polynomial initialized with a list of coefficients 
	#(coefficient of the nth degree corresponds to coefficients[0])
	def __init__(self, coefficients):
		self.coeffs = [float(i) for i in coefficients]
			
	def __repr__(self):
		return str(self.coeffs)
	
	def __str__(self):
		polyString = ""
		for index,term in enumerate(self.coeffs):
			if term != 0:
				if index != 0:
					polyString = polyString + " + "
				polyString = polyString + str(term)
				if index < len(self.coeffs) - 1:
					polyString = polyString + "x"
				if index < len(self.coeffs) - 2:
					polyString = polyString + "**" + str(self.exponent(index)-1)
		return polyString
	
	#Coefficient at index i
	def coeff(self, i):
		return self.coeffs[-i]	
	
	#Exponent corresponding to index n
	def exponent(self, n):
		return len(self.coeffs) - n
			
	#Multiplies two polynomials
	def mul(self, other):
		a, b = self.coeffs, other.coeffs
		ab = (len(a)+len(b)-1) * [0]
		for indexb, termb in enumerate(b):
			for indexa, terma in enumerate(a):
				ab[indexa+indexb] += terma*termb
		return Polynomial(ab)	
		
	def __mul__(self, other):	
		return self.mul(other)
		
	#Adds two polynomials
	def add(self, other):
		a, b = self.coeffs, other.coeffs
		zeros = abs(len(a)- len(b))
		if (len(a) > len(b)):
			return Polynomial([i+j for i,j in zip(a,[0]*zeros+b)])
		else: 
			return Polynomial([i+j for i,j in zip(b,[0]*zeros+a)])
			
	def __add__(self,other):
		return self.add(other)
	
	#Evaluates polynomial at f(x) 
	#Recursive Solution using Horner's Rule 
	def val(self, x):
		return self.valRecurse(self.coeffs, x)
	
	@staticmethod
	def valRecurse(poly, x):
		if len(poly) == 1:
			return poly[0]
		else:
			return poly[-1] + x*Polynomial.valRecurse(poly[0:len(poly)-1], x)
	
	def __call__(self, x):
		return self.val(x)
			
	#Returns the root(s) of 1st and 2nd degree polynomials
	def roots(self):
		length = len(self.coeffs)
		if length > 3:
			return "Error: Degree too high for root computation"
		elif len(self.coeffs) == 3:
			a,b,c = self.coeffs[0], self.coeffs[1], self.coeffs[2]
			discriminant = complex(b**2 - 4*a*c)**0.5
			plusroot = (-b + discriminant)/2*a
			minusroot = (-b - discriminant)/2*a
			return [plusroot, minusroot]
		else: 
			b,c = self.coeffs[0], self.coeffs[1], 
			return [-c/b]

		
#Tests
#I should probably round the complex roots, but oooooohhhh well	
print "Testing Class Polynomial:"	
a = Polynomial([1, 2, 3])
print "Polynomial a(x): " + str(a)
b = Polynomial([1, 2, 3, 4])
print "Polynomial b(x): " + str(b)
c = Polynomial([1, 2])
print "Polynomial c(x): " + str(c)
print "a+b = "+ str(a+b)
print "a*b = " + str(a*b)
print "b(2) = " + str(b(2))
print "Coefficient of a(x) for 2nd Degree Term: " + str(a.coeff(2))
print "Roots a(x): " + str(a.roots())
print "Roots b(x): " + str(b.roots())
print "Roots c(x): " + str(c.roots())



	
		


	
