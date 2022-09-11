from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # a and b are two numbers that appear only one time in the list.
        a, b = 0, 0

        # xor whole list
        xor, aXorB = 0, 0
        for num in nums:
            xor ^= num

        # since every num appears twice, those numbers will be disappered. a and b appear once. 
        aXorB = xor 

        # find right most bit 1,
        # rightSetBit is a mask with only bit is on.
        rightSetBit = aXorB & (-aXorB)

        # split the list into two small lists,
        # all numbers in the first one contain right most bit 1,
        # all numbers in the second list don't.
        # for example, the binary representation: a = **1, b = **0. a^b = **1,
        # that means a will be in the first list, and b will be in the second list.

        for num in nums:
            if num & rightSetBit > 0:
                a ^= num
            else:
                b ^= num

        return [a, b]

s = Solution()
print(s.singleNumber([2147483647, -2147483648]) == [2147483647, -2147483648])
print(s.singleNumber([1, 1, 2147483647, -2147483648]) == [2147483647, -2147483648])
print(s.singleNumber([-2147483648, -2147483648, 2147483647, 2147483647, 4, 5]) == [5,4])
print(s.singleNumber([1,2,1,3,2,5]) == [3,5])
print(s.singleNumber([-1,0]) == [-1, 0])
print(s.singleNumber([0,1]) == [1,0])