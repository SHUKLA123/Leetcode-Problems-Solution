from numpy import prod
nums =  [10,5,2,6]
k = 100
def numSubarrayProductLessThanK(nums, k):
    count = 0
    for i in range(1,len(nums)+1):
        l = maxSlidingWindow(nums,i,k)
        print(l)
        count += l
    return l
            
def maxSlidingWindow(nums,k1,k):
    count = 0
    for end in range(k1,len(nums)):
    	print(nums[end-k1:end],k1)
    	a = prod(nums[end-k1:end])
    	if a<k:
    		count += 1
    c = prod(nums[len(nums)-k:len(nums)])
    if c<k:
    	count += 1
    return count
print(numSubarrayProductLessThanK(nums,k))