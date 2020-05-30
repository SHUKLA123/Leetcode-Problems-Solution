def searchInsert(self, nums: List[int], target: int) -> int:
    try:
        a = nums.index(target)
        return nums.index(target)
    except:
        for i in range(len(nums)):
            if target < nums[i]:
                return i
        return len(nums)