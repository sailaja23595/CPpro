"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def partition(array,start,end):
	pivot = array[start]
	left = start + 1
	right = end

	res = False
	while not res:
		while left <= right and array[left] <= pivot:
			left = left + 1
		while array[right] >= pivot and right >= left:
			right = right - 1
		if right < left:
			res = True
		else:
			t = array[left]
			array[left] = array[right]
			array[right] = t
	t = array[start]
	array[start] = array[right]
	array[right] = t
	return right

def quicksupport(array,start,end):
	if start < end:
		point = partition(array,start,end)
		quicksupport(array,start,point-1)
		quicksupport(array,point+1,end)

def quicksort(array):
	quicksupport(array,0,len(array)-1)
	return array
	