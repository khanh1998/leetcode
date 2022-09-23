from typing import List


class Solution:
    def __init__(self) -> None:
        self.dict = {}
        for i in range(1, 27):
            key = f'{i}'
            self.dict[key] = True

    def count(self, s: str, i: int, arr: List[str]) -> int:
        if i >= len(s):
            return 1
        c = 0
        # take ith digit
        key = f'{s[i]}'
        if key in self.dict:
            arr.append(key)
            c += self.count(s, i + 1, arr)
            del arr[-1]
        #take ith and (i+1)th digits
        if i + 1 < len(s):
            key = f'{s[i:i+2]}'
            if key in self.dict:
                arr.append(key)
                c += self.count(s, i + 2, arr)
                del arr[-1]

        return c

    def numDecodings(self, s: str) -> int:
        return self.count(s, 0, [])

s = Solution()
print(s.numDecodings('11106') == 2)
print(s.numDecodings('12') == 2)
print(s.numDecodings('226') == 3)
print(s.numDecodings('06') == 0)