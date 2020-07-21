# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	# for i in range(len(s1)):
	# 	while(i < len(s3)):
	# 		if(s1[i] == s2[i]):
	# 			s1[i] = s3[i]
	# 		i = i + 1
	# return s1
	c = s1.count(s2)
	if c==0:
		return s1
	elif c==1:
		st = ''
		start = s1.find(s2)
		end = start + len(s2)
		st = s1[0:start] + s3 + s1[end:]
		return st
	else:
		st = s1
		for i in range(c):
			start = st.find(s2)
			end = start + len(s2)
			st = st[0:start] + s3 + st[end:]
		return st

