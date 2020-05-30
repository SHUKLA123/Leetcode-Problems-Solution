# Problem No. = 215 , Problem Title : Kth Largest Element in an Array

# Detailed Statement

# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

nums = [3,2,1,5,6,4]
k = 2
def findKthLargest(nums, k):
    return sorted(nums)[-k]
print(findKthLargest(nums,k))