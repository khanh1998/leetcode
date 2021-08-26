class Solution:
    def lengthOfLongestSubString(self, s: str) -> int:
        max = 0
        sub = ''
        for i in range(len(s)):
            substring = ''
            for j, c in enumerate(s[i:]):
                if substring.find(c) == -1:
                    substring += c
                    print(substring)
                else:
                    break
                length = len(substring)
                if (length > max):
                    max = len(substring)
                    sub = substring
            if len(s) == 1:
                return 1
        print(sub)
        return max

solution = Solution()
result = solution.lengthOfLongestSubString('au')
print(result)
