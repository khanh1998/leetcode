from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = [0]*32
        for num in nums:
            for i in range(0,32):
                ithBitIsOn = (num >> i) & 1
                if ithBitIsOn:
                    count[i] = (count[i] + 1) % 3 # count[i] = 0, 1 or 2

        result = 0

        print(count)

        for i in range(0,32):
            if count[i] > 0:
                result |= 1 << i # turn ith bit of result on (or not)
        
        return self.convert(result)

    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x

s = Solution()
print(s.singleNumber([5,-3,5,5]))