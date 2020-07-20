# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.
def isPrime(n):
	for i in range(2,n):
		if(n%i ==0 ):
			return False
	return True
def fun_hasnoprimes(l):
	# li = [j for sub in l for j in sub]
	# for k in li: 
	# 	for j in range(2, int(k)): 
	# 		if(int(k)%j == 0 and int(k)%1 == 0):
	# 			pass
	# 	return False
	# return True
	li = sum(l,[])
	for i in li:
		if(isPrime(int(i))):
			return False
	return True