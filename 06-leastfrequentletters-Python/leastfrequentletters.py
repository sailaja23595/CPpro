# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")
import string
# def splitstr(str):
# 	alp = ""
# 	number = ""
# 	spe = ""
# 	for i in range(len(str)):
# 		if(str[i].isdigit()):
# 			number = number + str[i]
# 		elif((str[i] >= 'A' and str[i]  <= 'Z')or (str[i] >= 'a' and str[i] <= 'z' ))
def leastfrequentletters(s):
	if len(s) == 0:
		return ''
	s = s.lower()
	alp = string.ascii_lowercase
	minc = 1500
	res = ''
	i = 0
	while i < 26:
		c = s.count(alp[i])
		if minc > c > 0 or minc == c:
			minc = c
			res = alp[i]
		i = i+1
	if res == '':
		return res
	return res
	
	# string = ""
	# if s.isalpha():
	# 	for i in s:
	# 		if string in i:
	# 			string[i] = string[i] + 1
	# 		return string 
	# return ''
		
