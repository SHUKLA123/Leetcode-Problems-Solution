nums = [2,3,1,2,4,3]
c = 7
for i in range(2,len(nums)):
	k = i
	def maxSlidingWindow(nums,k):
		window = 0
		d = {}
		window = sum(nums[:k])
		for end in range(k,len(nums)):
			window += nums[end]-nums[end-k]
			if window == c:
				print("mdk",k)
	print(maxSlidingWindow(nums,k)) 