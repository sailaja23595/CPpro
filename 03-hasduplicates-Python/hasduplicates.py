# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

[2,7,9,9,5,1,4,3,8]
def hasduplicates(L):
	lis = []
	c = 0
	li = [j for sub in L for j in sub]
	for i in li: 
		if i in lis:
			c = c + 1
		lis.append(i)
	if c <= 0:
		return False
	return True