def thirdMax(self, nums: List[int]) -> int:
    nums = list(set(nums))
    if len(nums) == 1:
        return nums[0]
    if nums == None:
        return 0
    return sorted(nums)[-3] if len(nums)>=3 else sorted(nums)[-1]