# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	st = str(abs(n))
	if(len(st) == 1):
		return False
	if(st[0] == st[1]):
		return True
	else:
		return False