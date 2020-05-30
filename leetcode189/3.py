from collections import Counter
favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
def peopleIndexes(favoriteCompanies):
	l = []
	for i in favoriteCompanies:
		flag = 0
		for j in favoriteCompanies:
			if set(i).issubset(set(j)):
				flag += 1
		if flag == 1 or flag == 0:
			l.append(favoriteCompanies.index(i))
	return l
print(peopleIndexes(favoriteCompanies))