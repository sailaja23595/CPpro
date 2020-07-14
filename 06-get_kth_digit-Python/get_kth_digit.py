# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	number = abs(digit)
	number1 = number % 10 ** (k + 1)
	number2 = number % 10 ** k
	num = (number2 - number1) / 10**k
	return abs(num)
