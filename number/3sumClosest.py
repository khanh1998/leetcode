from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        closestSum = float('inf')
        closestDiff = float('inf')
        for index, currentNum in enumerate(nums):
            leftIdx, rightIdx = index + 1, length - 1
            while leftIdx < rightIdx:
                threeSum = currentNum + nums[leftIdx] + nums[rightIdx]
                diff = abs(threeSum - target)
                if diff < closestDiff:
                    closestDiff = diff
                    closestSum = threeSum
                if threeSum == target:
                    return threeSum
                if threeSum > target:
                    rightIdx -= 1
                if threeSum < target:
                    leftIdx += 1
        return closestSum


s = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(nums, target) == 2)

nums = [0,0,0]
target = 1
print(s.threeSumClosest(nums, target) == 0)
