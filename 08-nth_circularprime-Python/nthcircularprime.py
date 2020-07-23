# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isPrime(n):
	if n > 1:
		for i in range(2,n):
			if(n%i ==0):
				return False
		return True
	return False

def rotate(n):
	c = 0
	t = n
	while t!=0:
		t = t//10
		c=c+1
	r = n % 10
	r1 = n // 10
	return r *(10 ** (c-1))+ r1

def circularprime(n):
	if n == 0:
		return False
	c = 0
	t = n
	while t != 0:
		t = t // 10
		c = c + 1
	for i in range(c):
		if not isPrime(n):
			return False
		n = rotate(n)
	return True

def nthcircularprime(n):
	li = []
	for i in range(200000):
		if circularprime(i):
			li.append(i)
	return li[n]
	