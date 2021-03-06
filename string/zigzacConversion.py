# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    ''''
        numRow = 6
        abcdfg | hijl | mkhuye | fdsf | jljksd | fjs_
        abcdfg | hijl | mkhuye | fdsf | j
        row 0: a m j
        row 5: partIndex = 1 : g e d
        formula: charIndex = rowIndex + partIndex * (numRow + (numRow - 2)); charIndex < len(s)
        row 1: b l k f l
        partIndex = 2
        formula:
            charIndex = rowIndex + partIndex * (numRow + (numRow - 2)); charIndex < len(s)
            charIndex = (partIndex + 1) * (numRow + (numRow - 2)) - rowIndex ; charIndex < len(s)
    '''
    def convertMethod1(self, s: str, numRows: int) -> str:
        zigzac = ''
        if numRows == 1:
            return s
        partLength = numRows + (numRows - 2)
        for rowIndex in range(numRows):
            partIndex = 0
            while True:
                # take a character in straigh line
                charIndex = rowIndex + partIndex * partLength
                if charIndex >= len(s):
                    break
                zigzac += s[charIndex]
                # take a character in diagonal line
                if rowIndex > 0 and rowIndex < numRows - 1:
                    charIndex = (partIndex + 1) * partLength - rowIndex
                    if charIndex >= len(s):
                        break
                    zigzac += s[charIndex]
                partIndex += 1
        return zigzac

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzac = ['' for _ in range(numRows)]
        goingDown = False
        currRow = 0
        for char in s:
            zigzac[currRow] += char
            if currRow == 0 or currRow == numRows - 1:
                goingDown = not goingDown
            currRow += 1 if goingDown else -1
        result = ''.join(zigzac)
        return result

s = Solution()
print(s.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI')
print(s.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')
print(s.convert('PAYPALISHIRING', 2) == 'PAHNAPLSIIGYIR')
print(s.convert('A', 1) == 'A')
print(s.convert('AB', 2) == 'AB')