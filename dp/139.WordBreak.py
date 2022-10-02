from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lengthS = len(s)
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in reversed(range(lengthS)):
            for word in wordDict:
                lengthW = len(word)
                if lengthW > (lengthS - i):
                    continue
                if word == s[i:i + lengthW]:
                    dp[i] = dp[i + lengthW]
                    if dp[i] == True:
                        break
        return dp[0]

s = Solution()
print(s.wordBreak("cars", ["car","ca","rs"]) == True)
print(s.wordBreak("leetcode", ["leet", "code"]) == True)
print(s.wordBreak("applepenapple", ["apple", "pen"]) == True)
print(s.wordBreak("catsandog",["cats","dog","sand","and","cat"]) == False)
print(s.wordBreak("catsanddogdogcatandcatssand",["cats","dog","sand","and","cat"]) == True)

