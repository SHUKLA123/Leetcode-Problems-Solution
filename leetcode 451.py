# Problem Id : 451,  Problem Statement:  Sort Characters By Frequency 
#Difficul : Medium

# Description :

#Given a string, sort it in decreasing order based on the frequency of characters. 

from collections import Counter
s = "cccaaa"
def test(s):
	a = Counter(s)
	a = sorted(a.items(), key=lambda t: t[1])
	b = ""
	for i,j in a:
		b += i*j
	return b[::-1]

print(test(s))
