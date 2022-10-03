from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        sums = [0] * length
        maxSoFar = 0
        for i in range(length):
            sums[i] = maxSoFar + nums[i]
            if i - 1 >= 0:
                maxSoFar = max(maxSoFar, sums[i -1])
        return max(sums[-1], maxSoFar)

s = Solution()
print(s.rob([9,2,3,9,5]) == 18)
print(s.rob([9,2,3,8,5]) == 17)
print(s.rob([9,2,1,8,7]) == 17)
print(s.rob([1,2,3,1]) == 4)
print(s.rob([2,7,9,3,1]) == 12)
print(s.rob([2,0,7,9,3,1]) == 12)