# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def ishappynumber(n):
	def sumofsquares(num1):
		add = 0
		while(num1 > 0):
			r = num1 % 10
			add = add + (r**2)
			num1 = num1 // 10
		return add
	l = []
	while sumofsquares(n) not in l:
		res = sumofsquares(n)
		if res == 1:
			return True
		else:
			l.append(res)
			n = res
	return False
def isPrime(n):
	for i in range(2,n):
		if(n%i ==0):
			return False
		else:
			return True

def fun_nth_happy_prime(n):
	li = []
	for i in range(60):
		if ishappynumber(i) and isPrime(i):
			li.append(i)
	return li[n]
