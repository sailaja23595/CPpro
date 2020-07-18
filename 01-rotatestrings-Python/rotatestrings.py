# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')

def isPositive(n):
	if(n < 0):
		return True
	return False

def fun_rotatestrings(s, n):
	st = ""
	if(isPositive(n)):
		n = abs(n)
		n = n%len(s)
		st = s[len(s) - n:] + s[:len(s) - n]
		return st
	if (not isPositive(n)):
		n = n % len(s)
		t = s[n:] + s[:n]
		return t


