from typing import List


class Solution:
    def find(self, s: str, wordDict: List[str], start: int) -> bool:
        lengthS = len(s)
        if start >= lengthS:
            return True
        for word in wordDict:
            lengthW = len(word)
            if lengthS - start < lengthW:
                continue
            if word == s[start:start + lengthW]:
                ok = self.find(s, wordDict, start + lengthW)
                if ok == True:
                    return True
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.find(s, wordDict, 0)

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
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

