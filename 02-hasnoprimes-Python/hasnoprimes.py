# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
	if(len(l) > 1):
		for i in l:
			for j in range(2, len(i)):
				if(j > 1 or j %i != 0):
					return True
		return False 
	return False

