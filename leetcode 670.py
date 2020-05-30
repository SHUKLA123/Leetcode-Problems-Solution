# Problem Number : 670. Problem Statement : Maximum Swap Difficulty : Medium

#Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
#Return the maximum valued number you could get.

#Runtime: 28 ms, faster than 73.04% 

def test(num):
	list_n = list(str(num))
	max = list_n[:]
	for i in range(len(list_n)):
		for j in range(i+1,len(list_n)):
			list_n[i],list_n[j] = list_n[j],list_n[i]
			if max<list_n:
				max = list_n[:]
			list_n[i], list_n[j] = list_n[j], list_n[i]
	return int("".join(max))

print(test(num))