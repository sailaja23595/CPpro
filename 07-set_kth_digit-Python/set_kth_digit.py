# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def fun_set_kth_digit(n, k, d):
	number = abs(n)
	st = str(number) 
	if(k<len(st)):
		s = int(len(st) - k - 1)
		st1 = st[0:s] + str(d) + st[s + 1 : len(st)]
		return int(st1)
	else:
		if(n>0):
			st1 = str(d) + st
			return int(st1)
		else:
			st1 = abs(n)
			st1 = str(d) + str(st1)
			st1 = int(st1) * -1
			return st1ss