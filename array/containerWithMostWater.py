from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_vol = 0
        while left < right:
            left_height = height[left]
            right_height = height[right]
            length = right - left
            vol = min(left_height, right_height) * length
            if vol > max_vol:
                max_vol = vol
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return max_vol
    
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]) == 49)
print(s.maxArea([1,1]) == 1)
print(s.maxArea([4,3,2,1,4]) == 16)
print(s.maxArea([1,2,1]) == 2)
print(s.maxArea([]) == 0)
print(s.maxArea([1]) == 0)
