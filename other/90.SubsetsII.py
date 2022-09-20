from typing import List

class Solution:
    def build(self, nums: List[int], tmp: List[List[int]], i: int) -> List[List[int]]:
        if i == len(nums):
            return [tmp]
        # take ith num
        take = self.build(nums, [*tmp, nums[i]], i+1)

        # don't take ith num,
        # skips consecutive duplicated values
        j = i + 1
        while j < len(nums) and nums[i] == nums[j]:
            j += 1

        notTake = self.build(nums, tmp, j)

        return [*take, *notTake]

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #backtracking
        nums.sort()
        result = self.build(nums, [], 0)
        return result

    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #n.log(n)
        result = [[]]
        lastResLen = 0
        for i in range(len(nums)):
            tmp = []
            if i > 0 and nums[i] == nums[i - 1]:
                for item in result[lastResLen:]:
                    tmp.append(item + [nums[i]])
            else:
                for item in result[:]:
                    tmp.append(item + [nums[i]])
            lastResLen = len(result)
            result += tmp
        return result
s = Solution()
print(s.subsetsWithDup(nums=[1,2,2]))
print(s.subsetsWithDup(nums=[0]))
print(s.subsetsWithDup(nums=[1,2,2,3]))