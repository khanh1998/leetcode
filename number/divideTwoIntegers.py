class Solution:
    def sign(self, number: int) -> int:
        if number < 0:
            return -1
        return 1

    def divide(self, dividend: int, divisor: int) -> int:
        max = 2 ** 31 - 1
        min = - (2 ** 31)
        if dividend == min and divisor == -1:
            return max
        sign = 1 if self.sign(dividend) == self.sign(divisor) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend - divisor >= 0:
            count = 0
            base = divisor
            while (base << count) <= dividend:
                count += 1
            quotient += 1 << count - 1
            dividend -= divisor << count - 1
        return sign * quotient

s = Solution()
print(s.divide(10, 1) == 10)
print(s.divide(1, 5) == 0)
print(s.divide(10, 5) == 2)
print(s.divide(10, -5) == -2)
print(s.divide(-10, 5) == -2)
print(s.divide(-10, -5) == 2)
print(s.divide(10, 10) == 1)
print(s.divide(10, 1) == 10)
print(s.divide(0, 1) == 0)
print(s.divide(10, 3) == 3)
print(s.divide(7, -3) == -2)
print(s.divide(-7, 3) == -2)
print(s.divide(-7, -3) == 2)
print(s.divide(2 ** 31 - 1, 1) == 2 ** 31 - 1)
print(s.divide(2 ** 31 - 1, -1) == -(2 ** 31 - 1))
print(s.divide(-2 ** 31, 1) == -2 ** 31)
print(s.divide(-2 ** 31, -1) == 2 ** 31 - 1)
print(s.divide(-2 ** 31, -1), 2 ** 31 - 1)