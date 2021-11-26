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

    
    def lengthOfLongestSubstringV2(self, s: str) -> int:
        ''' faster solution '''
        length = len(s)
        if length == 0:
            return 0
        begin, end = 0, 0
        longest = 1
        charToIdx = { s[0]: 0 }
        while end < length - 1:
            end += 1
            length = len(s)
        if length == 0:
            return 0
        begin, end = 0, 0
        longest = 1
        charToIdx = { s[0]: 0 }
        while end < length - 1:
            end += 1
            idx = charToIdx.get(s[end], None)
            if idx != None and idx >= begin:
                begin = min(charToIdx[s[end]] + 1, length - 1)
            else:
                longest = max(longest, end - begin + 1)
            charToIdx[s[end]] = end
        return longest

solution = Solution()
result = solution.lengthOfLongestSubString('au')
print(result)
