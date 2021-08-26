class Solution:
    def firstUniqChar(self, s: str) -> int:
        charToFirstIndex = {}
        charToNumOcurr = {}
        for index, char in enumerate(s):
            firstIndex = charToFirstIndex.get(char)
            if firstIndex is None:
                charToFirstIndex[char] = index
            numOcurr = charToNumOcurr.get(char)
            if numOcurr is None:
                charToNumOcurr[char] = 1
            else:
                charToNumOcurr[char] += 1
        for key, value in charToNumOcurr.items():
            if value == 1:
                return charToFirstIndex[key]
        return -1