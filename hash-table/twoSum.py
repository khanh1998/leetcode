class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # convert array to map
        numToIndex = {}
        for index, num in enumerate(nums):
            numToIndex[num] = index
        # find indices
        for index, num in enumerate(nums):
            diff = target - num
            diffIndex = numToIndex.get(diff)
            if diffIndex != None and diffIndex != index:
                return [index, diffIndex]