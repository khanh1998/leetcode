from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ''' using xor 
            for example: nums = [1,3,2]
            res ^= 0 ^ 1 ^ 2
            res ^= 1 ^ 2 ^ 3
            res ^= 3
            res == 0
        '''
        n = len(nums)
        result = 0
        for i in range(n):
            result ^= i # [0,n-1]
            result ^= nums[i] # all num in array
        result ^= n

        return result

    def missingNumber1(self, nums: List[int]) -> int:
        length = len(nums)
        flipZero = False # use this var to track sign of zero
        for num in nums:
            index = abs(num)
            if index < length:
                nums[index] = 0 - nums[index]
                if nums[index] == 0:
                    flipZero = True 
        
        for index, num in enumerate(nums):
            if num == 0 and flipZero == False:
                return index
            if num > 0:
                return index
        return len(nums) # miss last number

s = Solution()
print(s.missingNumber([2,0]) == 1)
print(s.missingNumber([3,0,1]) == 2)
print(s.missingNumber([3,2,1]) == 0)
print(s.missingNumber([0,2,1]) == 3)
print(s.missingNumber([0,1]) == 2)
print(s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8)