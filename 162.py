def findPeakElement(self, nums: List[int]) -> int:
    if sorted(nums) == nums:
        return len(nums)-1
    for i in range(1,len(nums)):
        if i != len(nums)-1:
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                return i
    return 0