from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Kadane algorithm
        Refer to: https://leetcode.com/problems/maximum-subarray/discuss/1595097/JAVA-or-Kadane's-Algorithm-or-Explanation-Using-Image 
        '''
        max, sum = float('-inf'), 0
        for i in nums:
            sum += i
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
print(s.maxSubArray([1]) == 1)
print(s.maxSubArray([1,2,3,4,5]) == 15)
print(s.maxSubArray([-1,-2,-3,-4]) == -1)