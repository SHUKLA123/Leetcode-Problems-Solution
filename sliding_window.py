nums = [1,9,-1,-2,7,3,-1,2]
k = 4
def maxSlidingWindow(nums,k):
	windowSum,maxSum = 0,0
	windowSum = sum(nums[:k])
	print(windowSum)
	for end in range(k,len(nums)):
		windowSum += nums[k]-nums[end - k]
		print(windowSum)
		maxSum = max(maxSum,windowSum)
	return maxSum
print(maxSlidingWindow(nums,k))
