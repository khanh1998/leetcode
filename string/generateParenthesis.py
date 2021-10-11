from typing import List


class Solution:
    results = []
    def generate(self, n: int, genArr: List[str], open: int, close: int):
        if len(genArr) == 2*n:
            genStr = "".join(genArr)
            if self.valid(genStr):
                self.results.append(genStr)
        else:
            if open < n:
                genArr.append('(')
                self.generate(n, genArr, open + 1, close)
                genArr.pop()
            if close < n:
                genArr.append(')')
                self.generate(n, genArr, open, close + 1)
                genArr.pop()

    def valid(self, genParen: str) -> bool:
        count = 0
        for c in genParen:
            if c == '(':
                count += 1
            if c == ')':
                count -= 1
            if count < 0:
                return False
        if count != 0:
            return False
        return True
    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []
        self.generate(n, [], 0, 0)
        return self.results

s = Solution()
print(s.generateParenthesis(4))
print(s.generateParenthesis(3))
print(s.generateParenthesis(2))
print(s.generateParenthesis(1))