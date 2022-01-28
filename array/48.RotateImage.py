from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        width = len(matrix[0])
        for i in range(width // 2):
            top = i
            bottom = width - i - 1
            right = width - i - 1
            left = i
            for j in range(width - 2*i - 1):
                tmp = matrix[bottom - j][left]
                matrix[bottom - j][left] = matrix[bottom][right - j]
                matrix[bottom][right - j] = matrix[top + j][right]
                matrix[top + j][right] = matrix[top][left + j]
                matrix[top][left + j] = tmp

def print_array(arr: List[List[int]]):
    print('-------------')
    for l in arr:
        print(l)

s = Solution()
m = [[5]]
print_array(m)
s.rotate(m)
print_array(m)
m = [[5,1],[2,4]]
print_array(m)
s.rotate(m)
print_array(m)
m = [[5,1,9],[2,4,8],[13,3,6]]
print_array(m)
s.rotate(m)
print_array(m)
m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print_array(m)
s.rotate(m)
print_array(m)
m = [[5,1,9,11,14],[2,4,8,10,34],[13,3,6,7,54],[15,14,12,16,76],[4,2,1,5,6]]
print_array(m)
s.rotate(m)
print_array(m)
