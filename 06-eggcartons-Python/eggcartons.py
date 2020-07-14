# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# your code goes here
	x = 1
	if eggs == 0:
		return 0
	elif eggs%x == 0:
		return 0
	elif eggs%x == 1:
		return 1
	return 1
