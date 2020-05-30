def twoSum(self, nums: List[int], target: int) -> List[int]:
    a = enumerate(nums)
    nums = sorted(nums)
    print(nums)
    left = 0
    right = len(nums)-1
    while left <= right:
        if nums[left]+nums[right] == target:
            break 
        elif nums[left]+nums[right] < target:
            left +=  1
        else:
            right -= 1
    l = []
    c,d = nums[left],nums[right]
    for i,j in a:
        if j == c:
            l.append(i)
        elif j == d:
            l.append(i)
    return l
            
            