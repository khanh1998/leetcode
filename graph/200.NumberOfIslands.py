from queue import Queue
from typing import List

LAND = '1'
VISISTED = '!'

# pairs of [row, column]
directions = [
    [-1, 0], # up
    [0, 1], # right
    [1, 0], # down
    [0, -1] # left
]

class Solution:
    def __init__(self) -> None:
        self.grid = None
        self.width = 0
        self.heigh = 0

    def isCoordicatorValid(self,row: int, column: int) -> bool:
        return row >= 0 and column >= 0 and row < self.heigh and column < self.width and self.grid[row][column] == LAND
    
    def markVisisted(self, row: int, column: int):
        self.grid[row][column] = VISISTED

    def bfs(self, row: int, colum: int):
        queue = Queue()
        queue.put((row, colum))
        while not queue.empty():
            r, c = queue.get()
            for rowDiff, colDiff in directions:
                rowNew = r + rowDiff
                colNew = c + colDiff
                if self.isCoordicatorValid(rowNew, colNew):
                    self.markVisisted(rowNew, colNew)
                    queue.put((rowNew, colNew))
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.heigh = len(grid)
        self.width = len(grid[0])
        count = 0
        for row in range(self.heigh):
            for column in range(self.width):
                if grid[row][column] == '1':
                    self.bfs(row, column)
                    count += 1
        return count

s = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(s.numIslands(grid) == 3)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(s.numIslands(grid) == 1)

grid = [
  ["1","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"]
]
print(s.numIslands(grid) == 1)

grid = [
  ["1","0","0","0","1"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"]
]
print(s.numIslands(grid) == 2)

grid = [
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["1","0","0","0","0"]
]
print(s.numIslands(grid) == 1)

grid = [
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","0","0"]
]
print(s.numIslands(grid) == 1)
