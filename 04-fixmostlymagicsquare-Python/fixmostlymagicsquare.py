# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	li = []
	for i in L:
		p = 0
		p = p + sum(i)
		li.append(p)
	if (len(li) != len(set(li))):
		q = max(li) - min(li)
		large = max(li)
		for i in li:
			if i == large:
				position = li.index(max(li))
		a = L[position]
		position1 = a.index(max(a))
		a[position1] = max(a) - q
		L[position] = a
		return L