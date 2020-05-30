#Problem Id : 1295,  Problem Statement : Find Numbers with Even Number of Digits, Dificulty : Medium

#Given an array nums of integers, return how many of them contain an even number of digits.

def test(nums):
	count = 0
	for i in nums:
		i = len(str(i))
		if i & 1 != 1:
			count += 1
	return count
nums = [12,345,2,6,7896]
print(test(nums))