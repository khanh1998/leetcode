from typing import List, Set
from xmlrpc.client import Boolean


class Solution:
    def find(self,paths: List[List[Boolean]], word: str, letter_idx: int, board: List[List[str]], board_row: int, board_col: int):
        '''
        to find the letter at letter_idx
        '''
        # stop
        if letter_idx == len(word):
            return True 
        next_letter = word[letter_idx]
        height = len(board)
        width = len(board[0])
        # go up
        up_row = board_row - 1
        if board_row > 0 and next_letter == board[up_row][board_col] and not paths[up_row][board_col]:
            paths[up_row][board_col] = True
            res = self.find(paths, word, letter_idx + 1, board, up_row, board_col)
            paths[up_row][board_col] = False
            if res == True:
                return res
        # go down
        down_row = board_row + 1
        if board_row < height - 1 and next_letter == board[down_row][board_col] and not paths[down_row][board_col]:
            paths[down_row][board_col] = True
            res = self.find(paths, word, letter_idx + 1, board, down_row, board_col)
            paths[down_row][board_col] = False
            if res == True:
                return res
        # go left
        left_col = board_col - 1
        if board_col > 0 and next_letter == board[board_row][left_col] and not paths[board_row][left_col]:
            paths[board_row][left_col] = True
            res = self.find(paths, word, letter_idx + 1, board, board_row, left_col)
            paths[board_row][left_col] = False
            if res == True:
                return res
        # go right
        right_col = board_col + 1
        if board_col < width - 1 and next_letter == board[board_row][right_col] and not paths[board_row][right_col]:
            paths[board_row][right_col] = True
            res = self.find(paths, word, letter_idx + 1, board, board_row, right_col)
            paths[board_row][right_col] = False
            if res == True:
                return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        first_letter = word[0]
        height = len(board)
        width = len(board[0])
        paths = [([False] * width) for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if board[i][j] == first_letter:
                    paths[i][j] = True
                    res = self.find(paths, word, 1, board, i, j)
                    if res == True:
                        return True
                    paths[i][j] = False
        return False

s = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(s.exist(board, word) == True)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCE"
print(s.exist(board, word) == True)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ESE"
print(s.exist(board, word) == True)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCESEEDASFC"
print(s.exist(board, word) == True)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ASA"
print(s.exist(board, word) == True)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ADEE"
print(s.exist(board, word) == True)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(s.exist(board, word) == True)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(s.exist(board, word) == False)

board = [['A']]
word = 'A'
print(s.exist(board, word) == True)

board = [['A']]
word = 'B'
print(s.exist(board, word) == False)