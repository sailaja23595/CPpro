# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.

import math
def fun_carrylessadd(x, y):
	res = 0
	mul = 1
	add = 0
	while(x or y):
		add = ((x%10) + (y%10))
		add = add % 10
		res = (add * mul) + res
		x = math.floor(x/10)
		y = math.floor(y/10)
		mul = mul * 10
	return res

