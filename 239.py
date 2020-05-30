from statistics import median
nums =  [5,3,4]
k = 1
def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    if len(nums) == k:
        return [median(nums)]
    window,l = 0,[]
    window = median(nums[:k])
    for end in range(k,len(nums)):
        check = nums[end-k:end]
        l.append(median(check))
    l.append(median(nums[len(nums)-k:len(nums)]))
    return l