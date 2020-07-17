# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	if(len(str(x)) != len(str(y))):
		return False
	while(x == y):
		power = pow(10, len(str(x))-1)
		for i in range(len(str(x))-1):
			firstd = x//power
			left = (x*10+firstd - (firstd * power * 10))
		x = left
	return True
	# return False
