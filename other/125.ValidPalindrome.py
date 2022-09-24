class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isUpperCase(s: str) -> bool:
            return ord(s) >= 65 and ord(s) <= 90
        def isLowerCase(s: str) -> bool:
            return ord(s) >= 97 and ord(s) <= 122
        def isNumeric(s: str) -> bool:
            return ord(s) >= 48 and ord(s) <= 57
        def isAlphaNumeric(s: str) -> bool:
            return isUpperCase(s) or isLowerCase(s) or isNumeric(s)
        def nomalize(s: str) -> str:
            if isUpperCase(s):
                return s.lower()
            return s

        i, j = 0, len(s) - 1
        while i < j:
            if not isAlphaNumeric(s[i]):
                i += 1
                continue
            if not isAlphaNumeric(s[j]):
                j -= 1
                continue
            if nomalize(s[i]) != nomalize(s[j]):
                return False
            else:
                i += 1
                j -= 1
        return True

s = Solution()
print(s.isPalindrome('A man, a plan, a canal: Panama') == True)
print(s.isPalindrome('race a car') == False)
print(s.isPalindrome(' ') == True)
print(s.isPalindrome('a') == True)
print(s.isPalindrome('aa') == True)
