# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def ishappynumber(n):
	def sumofsquares(num1):
		add = 0
		while(num1 > 0):
			r = num1 % 10
			add = add + (r**2)
			num1 = num1 // 10
		return add
	l =[]
	while sumofsquares(n) not in l:
		res = sumofsquares(n)
		if res == 1:
			return True
		else:
			l.append(res)
			n = res
	return False
def fun_nth_happy_number(n):
	li = []
	for i in range(60):
		if ishappynumber(i):
			li.append(i)
	return li[n]

