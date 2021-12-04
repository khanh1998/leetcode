# https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List

class Solution:
    def lengthOfLIS2(self, nums: List[int]) -> int:
        length = len(nums)
        l = [0] * (length + 1)
        maxLength = 1
        for i in range(1, length + 1):
            # ith number is lonely
            l[i] = 1
            for j in reversed(range(1, i)):
                if nums[j-1] < nums[i-1] and l[i] < l[j] + 1:
                    l[i] = l[j] + 1
                    if l[i] > maxLength:
                        maxLength = l[i]
        return maxLength
    
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            print('-----------------------')
            print(f'x={x} i={i} j={j}')
            while i != j:
                m = (i + j) // 2
                print(f'm={m}')
                if tails[m] < x:
                    i = m + 1
                    print(f'i={i}')
                else:
                    j = m
                    print(f'j={j}')
            tails[i] = x
            print(f'tails[{i}]={x}')
            size = max(i + 1, size)
            print(f'size={size}')
            print(f'tails {tails}')
            print(f'nums {nums}')
        return size

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4)
#print(s.lengthOfLIS([0,1,0,3,2,3]) == 4)
#print(s.lengthOfLIS([7,7,7,7,7,7,7]) == 1)
#print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]) ==  6)
