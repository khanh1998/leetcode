from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = {}
        numToInd = {}        
        # map from value to index
        for index, num in enumerate(nums):
            numToInd[num] = index
        # find triplets
        for i, numI in enumerate(nums[:-2]):
            for j, numJ in enumerate(nums[i+1:]):
                jIndex = j + i + 1
                remain = 0 - numI - numJ
                index = numToInd.get(remain, None)
                if index != None and index > jIndex and index != i and index != jIndex:
                    arr = [numI, numJ, remain]
                    arr.sort()
                    result[tuple(arr)] = True
        return list(map(list, list(result.keys())))

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
# -4, -1, -1, 0, 1, 2
print(s.threeSum([0,0,0,0,0,0,0,0]))
print(s.threeSum([1,2,3,4,5]))
print(s.threeSum([]))
print(s.threeSum([0]))