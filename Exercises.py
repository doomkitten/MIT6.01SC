#MIT.601SC Exercises
#My answers to exercise questions from MIT 6.01SC
#Exercises were used as a python syntax refresher
#For more information regarding the problem set, see the exercise .pdf at
#http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/unit-1-software-engineering/object-oriented-programming/MIT6_01SCS11_chap02.pdf

#Typical Fibonacci Sequence Example	
#fib(n) returns the nth Fibonacci number.
def fib(n):
	if n <= 0: return 0
	elif n == 1: return 1
	return fib(n-1) + fib (n-2)

#Exercise 2.1:
#Write a procedure that takes a list of numbers (nums) and a limit (limit)
#and returns a list which is the shortest subset of nums whose
#sum is greater than limit. Use a for loop. 

#None is returned if the sum of the list is less than the limit
def sumToLimit(nums, limit):
	nums.sort()
	nums.reverse()
	sum = 0
	for index, x in enumerate(nums):
		if sum >= limit:
			return nums[:index]
		else:
			sum = sum + x
	return None;	



#Exercise 2.2	
#Write a procedure that takes n as an argument and returns the sum of the
#squares of the integers from 1 to n. It should use for and range. 

#Iterative Defintion of 2.2:
def sumOfSquaresIterative(n):
	sum = 0
	for x in range(n+1):
		sum += x**2
	return sum
	
#Recursive Definition of 2.2: 
# No need for "for" or "range"
def sumOfSquaresRecursive(n):
	if n == 1:
		return 1
	return n**2 + sumOfSquaresRecursive(n-1)
	

#Exercise 2.4. 
#Now, see if you can, first, explain, and then improve this example!
#def issubset(a,b):
#	i = 0
#	j = 0
#	while i < len(a):
#		c = False
#		while j < len(b):
#			if a[i] == b[j]:
#			c = True
#			j = j+1
#			if c:
#				c = False
#			else:
#				return False
#			j = 0
#		i = i+1
#		return True


#isSubset checks if list a is a subset of b. 
def isSubset(a,b):
	if len(a) == 0:
		return True
	elif isInSet(a[0],b):
		return isSubset(a[1:], b)
	return False
		
#isInSet checks if an item is in in set.		
def isInSet(a,b):
	if len(b) == 0:
		return False
	elif a == b[0]:
		return True
	return isInSet(a,b[1:])
	
			
			
#Test
a = [14, 62, 3, 1]
b = [14, 62]
c = [14, 13, 62]
print sumToLimit(a, 64)
print sumOfSquaresIterative(25)
print sumOfSquaresRecursive(25)
print isSubset(b,a)
print isSubset(c,b)
print fib(6)



