# Probem Id : 78  Problem Statement : Subsets

# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Runtime: 32 ms, faster than 75.74%

def subsets(nums):
	n = len(nums)
	nth_bit = 1 << n
	result = []
	for i in range(2**n):
	    bitmask = list(bin(i | nth_bit)[3:])
	    temp = []
	    for j,k in zip(nums,bitmask):
	    	if k != "0":
	    		temp.append(j)
	    result.append(temp)
	return result

nums = [1,2,3]
print(subsets(nums))

# def subsets(nums):
# 	result = []
# 	n = len(nums)
# 	for i in range(n):
# 	    for j in range(i+1,n):
# 	    	print(nums[i:j])
# 	return result

# nums = [1,2,3]
# print(subsets(nums))

