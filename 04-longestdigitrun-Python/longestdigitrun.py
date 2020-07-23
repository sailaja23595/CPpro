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

	if n < 0:
		n = -n
	d = {}
	c = 1
	li = list(map(int,str(n)))
	for i in range(len(li) - 1):
		if li[i] == li[i+1]:
			c = 0
			if li[i] not in d:
				d[li[i]] = 1
			else:
				d[li[i]] = d[li[i]] + 1

	if c==1:
		li.sort()
		return li[0]
	dic = {}
	m = sorted(d.keys())
	for i in m:
		dic[i] = d[i]
	dic = sorted(dic.items(), key = lambda item : item[1],reverse = True)
	return dic[0][0]	


