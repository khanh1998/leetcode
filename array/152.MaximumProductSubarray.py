from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # two passes solution
        maxValue = -11
        cumulative = 1
        for num in nums:
            if cumulative == 0:
                cumulative = 1
            cumulative *= num
            maxValue = max(maxValue, cumulative)
        cumulative = 1
        for num in reversed(nums):
            if cumulative == 0:
                cumulative = 1
            cumulative *= num
            maxValue = max(maxValue, cumulative)
        return maxValue

s = Solution()
print(s.maxProduct([2,3,-2,4]) == 6)
print(s.maxProduct([-2,0,-1]) == 0)
print(s.maxProduct([1,-2,3,-1,4,-2,1]) == 24)