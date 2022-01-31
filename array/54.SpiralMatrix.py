from typing import List
from decimal import Decimal, ROUND_HALF_UP

class Solution:
    def stop(self, top: int, bottom: int, left: int, right: int) -> bool:
        return bottom < top or right < left

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        max_height = len(matrix)
        max_width = len(matrix[0])
        top, bottom, left, right = 0, max_height - 1, 0, max_width - 1
        arr = []

        while not self.stop(top, bottom, left, right):
            # corner case
            # top == bottom or left == right
            if top == bottom and left == right and top == left:
                arr.append(matrix[top][left])
            elif top == bottom:
                for t in range(left, right + 1):
                    arr.append(matrix[top][t])
            elif left == right:
                for r in range(top, bottom + 1):
                    arr.append(matrix[r][right])
            else:
                for t in range(left, right):
                    arr.append(matrix[top][t])
                for r in range(top, bottom):
                    arr.append(matrix[r][right])
                for b in reversed(range(left + 1, right + 1)):
                    arr.append(matrix[bottom][b])
                for l in reversed(range(top + 1, bottom + 1)):
                    arr.append(matrix[l][left])
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return arr

s = Solution()
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [1,2,3,6,9,8,7,4,5]
print(s.spiralOrder(a) == b)
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
b = [1,2,3,4,8,12,11,10,9,5,6,7]
print(s.spiralOrder(a) == b)
a = [[6,9,7]]
b = [6,9,7]
print(s.spiralOrder(a) == b)
a = [[1],[2],[3]]
b = [1,2,3]
print(s.spiralOrder(a) == b)
a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
