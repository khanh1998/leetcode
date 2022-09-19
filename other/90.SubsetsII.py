from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
print(s.subsetsWithDup(nums=[1,2,3,3,4]))