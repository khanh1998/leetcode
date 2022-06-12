class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = x
        reversedN = 0
        while n > 0:
            digit = n % 10
            reversedN = reversedN * 10 + digit
            n = n // 10
        return x == reversedN

s = Solution()
print(s.isPalindrome(121) == True)
print(s.isPalindrome(-121) == False)
print(s.isPalindrome(10) == False)