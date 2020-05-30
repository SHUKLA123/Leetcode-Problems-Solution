# Problem Id : 1347.  Problem Statement : Minimum Number of Steps to Make Two Strings Anagram Difficulty : Medium

#Description: 

#Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.
#Return the minimum number of steps to make t an anagram of s.
#An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# solution : 

#I have first counted all occurence of both string character. 
#Then I check if t has a chacter which is not present in the s then i add in count + b[i](occuence of the chacacter in t string). 
#If t has a chacter which has greater ocuurence in t than s then b[i]-a[i] which will create same as number of occurence of that character in a.   

from collections import Counter
s = "leetcode"
t = "practice"
def minSteps(s,t):
	a = Counter(s)
	b = Counter(t)
	count = 0
	for i,j in b.items():
		if i not in a.keys():
			count += b[i]
		elif i in a.keys() and j > a[i]:
			count += b[i] - a[i]
	return count
print(minSteps(s,t))