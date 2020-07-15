# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	st = str(abs(n))
	if(len(st) == 1):
		return False
	elif(len(st) == 2):
		if(st[0] == st[1]):
			return True
		else:
			return False
		var = -1
		for i in range(len(st)):
			if (st[i] == var):
				return True
			var = st[i]
		return False

		
