# Leetcode , Problem No. : 55

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

nums = [2,3,1,1,4]

def canJump(nums):
    if len(nums) is 1 or nums.count(0) is 0:
        return True
    if nums[0] is 0:
        return False
    l = []
    for i in range(len(nums)):
        if i+nums[i] >= len(nums)-1 and i<len(nums)-1:
            return True
        if nums[i] is 0:
            if max(l) <= nums[i]+i:
                return False
        l.append(i+nums[i])
print(canJump(nums))