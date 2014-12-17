#Exercise 2.1:
#Write a procedure that takes a list of numbers, nums, and a limit, limit,
#and returns a list which is the shortest prefix of nums the sum of whose
#values is greater than limit. Use for. Try to avoid using explicit indexing
#into the list. (Hint: consider the strategy we used in member.) 


#None is returned if no sublist can be found whose sum is greater than the limit 
#(ie the sum of each number in the list is less than the limit)
#Iterative Solution
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



##################################################################################

#Exercise 2.2	
#Write a procedure that takes n as an argument and returns the sum of the
#squares of the integers from 1 to n-1. It should use for and range. 


#Iterative Defintion:
def sumOfSquaresIterative(n):
	rangeOfNums = range(n)
	sum = 0
	for x in rangeOfNums:
		sum = sum + x**2
	return sum
	
#Recursive Definition: 
# No need for "for" or "range"
def sumOfSquaresRecursive(n):
	if n == 1:
		return 1
	return n*n + sumOfSquares(n-1)
	
##################################################################################


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


#Recursive Solution: 
#isInSet checks if a number is in in set.
#isSubset checks if list a is a subset of b. 

def isSubset(a,b):
	if len(a) == 0:
		return True
	elif isInSet(a[0],b):
		return isSubset(a[1:], b)
	return False
		
		
def isInSet(a,b):
	if len(b) == 0:
		return False
	elif a == b[0]:
		return True
	return isInSet(a,b[1:])
	
		