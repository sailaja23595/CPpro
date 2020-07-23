# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def withproperty309(n):
	c = 0
	i = 0
	n = n ** 5
	t = n
	while n > 0:
		if i != n %10:
			n = n // 10
		elif i == n % 10:
			c = c+1
			n = t
			i = i+1
			if c > 9:
				return True
	return False

def nthwithproperty309(n):
	i = -1
	g = 0
	while i < n:
		g = g + 1
		if withproperty309(g):
			i = i+1
	return g
	