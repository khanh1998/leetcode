class Solution:
    def isValid(self, arr) -> bool:
        numToOccur = {}
        for num in arr:
            if num in numToOccur and num != '.':
                return False
            else:
                numToOccur[num] = True
        return True

    def isValidSudoku(self, board) -> bool:
        # check rows
        for row in board:
            if not self.isValid(row):
                return False
        # check columns
        size = len(board)
        for i in range(size): # interate over all column
            col = []
            for j in range(size): # interate over all rows
                col.append(board[j][i])
            if not self.isValid(col):
                return False
        # check sub boxes
        for i in range(3):
            for j in range(3):
                col = []
                i_topleft = i * 3
                j_topleft = j * 3
                for i_sub in range(3):
                    for j_sub in range(3):
                        i_abs = i_topleft + i_sub
                        j_abs = j_topleft + j_sub
                        col.append(board[i_abs][j_abs])
                if not self.isValid(col):
                    return False
        return True

solution = Solution()
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board))



