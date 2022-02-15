from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        row_markers = [False] * rows
        column_markers = [False] * columns
        # print_array(matrix)
        # to mark which columns and which rows has 0
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    row_markers[r] = True
                    column_markers[c] = True
        # processing
        for r in reversed(range(rows)):
            for c in reversed(range(columns)):
                if row_markers[r] or column_markers[c]:
                    matrix[r][c] = 0

        # print_array(matrix)

def print_array(arr):
    for row in arr:
        print(row)
    print()

s = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(matrix)
print(matrix == [[1,0,1],[0,0,0],[1,0,1]])
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(matrix)
print(matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
matrix = [[1,2,3],[4,5,6],[7,8,0]]
s.setZeroes(matrix)
print(matrix == [[1,2,0], [4,5,0], [0,0,0]])
matrix = [[1,2,3],[4,5,6],[0,7,8]]
s.setZeroes(matrix)
print(matrix == [[0,2,3],[0,5,6],[0,0,0]])