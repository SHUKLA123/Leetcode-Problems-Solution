def maxArea(self, height):
    left = 0
    right = len(height)-1
    maxarea = 0
    while left<right:
        a = height[right] if height[left]>height[right] else height[left]
        maxarea = max(a*(right-left),maxarea)
        if height[left]>height[right]:
            right -= 1
            
        else:
            left += 1
    return maxarea