# https://leetcode.com/problems/string-to-integer-atoi/
import math

class Solution:
    maxInt = 2 ** 31 - 1 # 2147483647
    maxDividedBy10 = math.floor(maxInt/10)
    minInt = (2 ** 31) # 2147483647 ()
    minDividedBy10 = math.floor(minInt/10)

    def canBiggerThanMax(self, number: int, nextDigit: int) -> bool:
        if number > self.maxDividedBy10:
            return True
        elif number == self.maxDividedBy10:
            if nextDigit > 7: #last digit of max
                return True
        else:
            return False

    def canSmallerThanMin(self, number: int, nextDigit: int) -> bool:
        # because the number has no sign
        if number > self.minDividedBy10:
            return True
        elif number == self.minDividedBy10:
            if nextDigit > 8: #last digit of min
                return True
        else:
            return False

    def myAtoi(self, s: str) -> int:
        index = 0
        sign = 1
        number = 0
        if len(s) == 0:
            return 0
        # removing first white spaces
        while s[index] == ' ' and index < len(s) - 1:
            index += 1
        # taking sign of number
        if index < len(s) and (s[index] == '-' or s[index] == '+'):
            sign = -1 if s[index] == '-' else 1
            index += 1
        # convert chars to number
        while index < len(s) and s[index] >= '0' and s[index] <= '9':
            nextDigit = int(s[index])
            # check if the number could be bigger than 2^31 - 1 after add value of new digit
            if sign == 1 and self.canBiggerThanMax(number, nextDigit):
                return self.maxInt
            if sign == -1 and self.canSmallerThanMin(number, nextDigit):
                return -self.minInt
            number = number * 10 + int(s[index])
            index += 1
        return sign*number

s = Solution()
print(s.myAtoi("-2147483649"))
print(s.myAtoi("-2147483648"))
print(s.myAtoi("-2147483647"))
print(s.myAtoi("2147483648"))
print(s.myAtoi("2147483647"))
print(s.myAtoi("2147483646"))