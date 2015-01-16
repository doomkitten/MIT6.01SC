#MIT.601SC Exercises
#These are are my answers to exercise questions from MIT's 6.01SC
#These exercises helped me refresh on my python syntax
#For more information regarding these problems, see
#http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/unit-1-software-engineering/object-oriented-programming/MIT6_01SCS11_chap02.pdf


#Exercise 2.1:
#Write a procedure that takes a list of numbers (nums) and a limit (limit)
#and returns a list which is the shortest prefix of nums the sum of whose
#values is greater than limit. Use a for loop. 

#None is returned if the sum of the list is less than the limit
def numberList(nums, limit):
	nums.sort()
	nums.reverse()
	sum = 0
	i = 0
	for x in nums:
		if sum >= limit:
			return nums[:i]
		else:
			sum = sum + x
			i += 1
	return None;	



#Exercise 2.2	
#Write a procedure that takes n as an argument and returns the sum of the
#squares of the integers from 1 to n-1. It should use for and range. 

#Iterative Defintion of 2.2:
def sumOfSquaresIterative(n):
	rangeOfNums = range(n)
	sum = 0
	for x in rangeOfNums:
		sum = sum + x**2
	return sum
	
#Recursive Definition of 2.2: 
# No need for "for" or "range"
def sumOfSquaresRecursive(n):
	if n == 1:
		return 1
	return n*n + sumOfSquares(n-1)
	

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
	
#Typical Fibonacci Sequence Example	
#fib(n) returns the nth Fibonacci number.
def fib(n):
	if n <= 0: return 0
	elif n == 1: return 1
	return fib(n-1) + fib (n-2)


