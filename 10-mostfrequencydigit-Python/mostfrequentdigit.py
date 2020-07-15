# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	count = 0
	number = str(n)
	for i in number:
		frequent = number.count(i)
		if(frequent > count):
			count = frequent
			number = i 
	return number
