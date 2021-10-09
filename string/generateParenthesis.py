from typing import List


class Solution:
    results = []
    def generate(self, n: int, genArr: List[str]):
        if len(genArr) == 2*n:
            genStr = "".join(genArr)
            if self.valid(genStr):
                self.results.append(genStr)
        else:
            genArr.append('(')
            self.generate(n, genArr)
            genArr.pop()
            genArr.append(')')
            self.generate(n, genArr)
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
        self.generate(n, [])
        return self.results

s = Solution()
print(s.generateParenthesis(3))