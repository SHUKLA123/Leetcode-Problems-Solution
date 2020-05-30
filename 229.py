def majorityElement(self, nums: List[int]) -> List[int]:
    n = len(nums)
    a = n/3
    b = Counter(nums)
    l = []
    for i,j in b.items():
        if j>a:
            l.append(i)
    return l