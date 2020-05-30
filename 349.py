def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    a = set(nums1)
    b = set(nums2)
    l = []
    if len(a)<=len(b):
        for i in a:
            if i in b:
                l.append(i)
    else:
        for i in b:
            if i in a:
                l.append(i)
    return l