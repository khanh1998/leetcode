from typing import List

MIN = -10**9 - 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # build the map
        numMap = {}
        for num in nums:
            numMap[num] = True
        # process
        length = len(nums)
        longest = 0
        startVal, endVal = MIN, MIN # start and end value of the sequence
        for i in range(length):
            if nums[i] < startVal or nums[i] > endVal:
                start = next = nums[i]
                long = 1
                while True:
                    next += 1
                    if next in numMap:
                        long += 1
                    else:
                        break
                end = next - 1
                if long > longest:
                    longest = long
                    startVal = start
                    endVal = end
        return longest

    def longestConsecutive1(self, nums: List[int]) -> int:
        # naive brute force
        longest = 0
        length = len(nums)
        for num in nums:
            long = 1
            next = num
            for i in range(1, length):
                next += i
                if next in nums:
                    long += 1
                else:
                    break
            longest = max(longest, long)
        return longest

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]) == 4)
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9)
print(s.longestConsecutive([]) == 0)
print(s.longestConsecutive([1,5]) == 1)
print(s.longestConsecutive([1,2]) == 2)
print(s.longestConsecutive([-1,-2]) == 2)
print(s.longestConsecutive([0,1]) == 2)
print(s.longestConsecutive([1,4,6]) == 1)
print(s.longestConsecutive([1,4,5]) == 2)
print(s.longestConsecutive([1,2,5]) == 2)
print(s.longestConsecutive([3,1,2]) == 3)
print(s.longestConsecutive([-1,1,0]) == 3)
print(s.longestConsecutive([0,-1,1]) == 3)
print(s.longestConsecutive([-1,0,1]) == 3)