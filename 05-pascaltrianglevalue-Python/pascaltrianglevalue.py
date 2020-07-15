# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	r = 1
	if row < col :
		return 0
	if row == col:
		return row
	# elif row < col:
	# 	return 0
	if col > (row-col) :
		col = row - col
	for i in range(0, col):
		r = r*row - i
		r = r//(i+1)
	return r