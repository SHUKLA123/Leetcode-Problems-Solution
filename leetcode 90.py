# Probem Id : 90  Problem Statement : Subsets II

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Runtime: 56 ms, faster than 10.01% of Python3
from collections import Counter
def subsets(nums):
        n = len(nums)
        nth_bit = 1 << n
        result = []
        nums = sorted(nums)
        for i in range(2**n):
            bitmask = list(bin(i | nth_bit)[3:])
            temp = []
            for j,k in zip(nums,bitmask):
                if k != "0":
                    temp.append(j)
            if temp not in result:
                result.append(tuple(temp))
        a = Counter(result)
        final = list(map(list,a.keys()))
        return final
nums = [4,4,4,1,4]
print(subsets(nums))