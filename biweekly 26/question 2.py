def simplifiedFractions(n):
	l = []
	c = []
	for i in range(1,n+1):
		for j in range(1,n+1):
			b = str(i)+"/"+str(j)
			a = i/j
			if a>0 and a<1 and a not in c:
				l.append(b)
				c.append(a)
	return l
n = 1
print(simplifiedFractions(n))