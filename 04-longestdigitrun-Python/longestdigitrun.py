# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# if not n:
	# 	return 0
	# longest =1
	# current = 1
	
	# n= str(n)
	# res = [int(x) for x in n]
	# for i in res:
	# 	if n[i] != n[i-1]:
	# 		if n[i] == n[i - 1] + 1:
	# 			current += 1
	# 		else:
	# 			longest = max(longest,current)
	# 			current = 1
	# return max(longest)

	pre = n
	c = 1
	best = pre
	bestcount = c
	while n>=0:
		current = n + 1
		if current == prev:
			c += 1
		else:
			prev = current
			c = 1
		if c > bestcount:
			bestcount = c
			best = current
	return (bestcount)

