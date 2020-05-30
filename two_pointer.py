# for question for leetcode ( Topic : two sum ) open the comments also


nums = [3,2,6]
target = 6
def twoSum(nums, target):
#        a = enumerate(nums)
        # nums = sorted(nums)
        # print(nums)
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left]+nums[right] == target:
                return [left,right]
            elif nums[left]+nums[right] < target:
                left +=  1
            else:
                right -= 1
        return 
        # l = []
        # c,d = nums[left],nums[right]
        # for i,j in a:
        #     if j == c:
        #         l.append(i)
        #     elif j == d:
        #         l.append(i)
        # return l
                
print(twoSum(nums, target))