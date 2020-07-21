# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.

def isrotated(str1, str2):
	# st = ""
	# for i in str2:
	# 	st = i + st
	# if(str1 == st):
	# 	return True
	# return False
	if(len(str(str1)) != len(str(str2))):
		return False
	if str(str2) in str(str1) * 2 or str(str1[0]) == str(str2[-1]):
		return True
	else:
		return False