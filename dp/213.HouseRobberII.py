from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        maxRob = 0
        length = len(nums)
        if length < 3:
            return max(nums)
        # forward pass without last item
        cumulative = [0] * length
        cumulative[0] = nums[0]
        cumulative[1] = max(nums[0], nums[1])
        for i in range(2, length-1):
            cumulative[i] = max(cumulative[i-1], cumulative[i-2] + nums[i])
        maxRob = max(maxRob, cumulative[-2])
        # backward pass without first item
        cumulative = [0] * length
        cumulative[-1] = nums[-1]
        cumulative[-2] = max(nums[-1], nums[-2])
        for i in reversed(range(1, length - 2)):
            cumulative[i] = max(cumulative[i+1], cumulative[i+2] + nums[i])
        maxRob = max(maxRob, cumulative[1])

        # another way is, in first forward pass, we solve this problem without first element.
        # in second forward pass, we solve this problem without last element.
        # finally we return max between two passes.

        return maxRob

s = Solution()
print(s.rob([2,3,2]) == 3)
print(s.rob([1,2,3,1]) == 4)
print(s.rob([1,2,3]) == 3)
print(s.rob([3]) == 3)
print(s.rob([3,1]) == 3)
print(s.rob([1,9,3,4,8,2]) == 17)
print(s.rob([9,1,3,4,8,2]) == 20)
print(s.rob([5,9,1,3,2,4]) == 16)
print(s.rob([3,2,5,8,1,4]) == 14)