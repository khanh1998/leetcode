from email.mime import base
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        BIT_LENGTH = 17
        baseCount = [0] * BIT_LENGTH # 2^17 > 10^5
        numsCount = [0] * BIT_LENGTH # 2^17 > 10^5
        result = 0

        for i in range(BIT_LENGTH):
            for index, num in enumerate(nums):
                if num & (1<<i):
                    numsCount[i] += 1

                if index & (1<<i):
                    baseCount[i] += 1

            if numsCount[i] > baseCount[i]:
                result |= (1<<i)

        return result

    def findDuplicate2(self, nums: List[int]) -> int:
        # negative marking
        # all number are in range 1 -> n, each number appears exactly one,
        # exept one number appears twice.
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                return abs(num)
            nums[index] = - nums[index] # flip sign of the number
        return -1 # cannot find the duplication

    def findDuplicate1(self, nums: List[int]) -> int:
        # sorting solution
        # time complexity: n*log(n)
        nums.sort()
        lastIndex = len(nums) - 1
        for index, num in enumerate(nums):
            if index == lastIndex:
                break
            nextNum = nums[index + 1]
            if num == nextNum:
                return num

        return -1 # cannot find the duplication

s = Solution()
print(s.findDuplicate([3,1,3,4,2]) == 3)
print(s.findDuplicate([1,3,4,2,2]) == 2)
print(s.findDuplicate([1,1]) == 1)
print(s.findDuplicate([2,2,2,2,2]) == 2)