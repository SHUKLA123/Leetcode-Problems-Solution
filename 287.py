def findDuplicate(self, nums):
    a = Counter(nums)
    for i,j in a.items():
        if j > 1:
            return i