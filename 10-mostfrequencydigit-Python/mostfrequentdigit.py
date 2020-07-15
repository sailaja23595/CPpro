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
		return int(number)
	else:
		var = -1
		for i in range(len(number) - 1):
			if(number[i] == number[i+1]):
				var = number[i]
				count = count + 1
		if count > 0:
			return int(var)

