import math

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        num = abs(x)
        sign = int(x / abs(x))
        reverseNum = None
        while num != 0:
            remainder = num % 10
            quotient =  math.floor(num / 10)
            if reverseNum is None:
                reverseNum = remainder
            else:
                reverseNum = reverseNum * 10 + remainder
            num = quotient
        if reverseNum > 2**31 - 1:
            return 0
        else:
            return sign*reverseNum
s = Solution()
print(s.reverse(0))