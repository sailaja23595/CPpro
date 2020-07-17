# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isPrime(n):
	for i in range(2,n):
		if(n%i == 0):
			return False
		else:
			return True

def fun_isadditive(n):
	add = 0
	if(isPrime(n)):
		while(n > 0):
			rem = n % 10
			add = add + rem
			n = n // 10
		if(isPrime(add)):
			return True
		else:
			return False

def fun_nth_additive_prime(n):
	lis = []
	for i in range(1000):
		if fun_isadditive(i):
			lis.append(i)
	return li[n]