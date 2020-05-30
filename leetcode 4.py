# Problem Id : 4 Problem Title : Median of Two Sorted Arrays

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# solution : use module median to find median
# 84 ms, faster than 97.46% of Python3 


from statistics import median
nums1 = [1, 2]
nums2 = [3, 4]
def findMedianSortedArrays(nums1, nums2):
    l = nums1 + nums2
    return median(l)
print(findMedianSortedArrays(nums2,nums1))