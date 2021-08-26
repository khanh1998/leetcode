class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sToT = {}
        tToS = {}
        for index, tChar in enumerate(t):
            sChar = s[index]
            currTChar = sToT.get(sChar)
            currSChar = tToS.get(tChar)
            # one char maps to two chars
            if currTChar != None and currTChar != tChar:
                return False
            # two chars map to one char
            if currSChar != None and currSChar != sChar:
                return False
            tToS.get(tChar)
            sToT[sChar] = tChar
            tToS[tChar] = sChar
        return True

solution = Solution()
print(solution.isIsomorphic("badc", "baba"))
print(solution.isIsomorphic("egg", "add"))
print(solution.isIsomorphic("foo", "bar"))
print(solution.isIsomorphic("paper", "title"))