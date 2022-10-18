from typing import List, Optional, Set, Tuple

MIN = -1

# pairs of [row, column]
directions = [
    [-1, 0], # up
    [0, 1], # right
    [1, 0], # down
    [0, -1] # left
]

class Solution:
    def __init__(self) -> None:
        self.rows = None
        self.cols = None
        self.heights = None
        self.visisted = None
    
    def reachFacific(self, row: int, col: int) -> bool:
        return row < 0 or col < 0
    
    def reachAtlantic(self, row: int, col: int) -> bool:
        return row >= self.rows or col >= self.cols
    
    def getHeight(self, row: int, col: int) -> bool:
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols:
            return MIN
        return self.heights[row][col]

    def getVisisted(self, row: int, col: int) -> Tuple[bool, int, int]:
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols:
            return (False, 0, 0)
        atlantic, pacific = self.visisted[row][col]

        visisted = False
        if atlantic != 0 or pacific != 0:
            visisted = True
        
        return (visisted, atlantic, pacific)
    
    def setVisisted(self, row: int, col: int, atlantic: bool, pacific: bool):
        self.visisted[row][col] = (atlantic, pacific)

    # return atlantic, facific
    # 1: can visist, -1: can't visist
    def dfs(self, row: int, col: int, path: Set[Tuple[int, int]]) -> Tuple[bool, bool]:
        if self.reachAtlantic(row, col):
            return 1, -1
        if self.reachFacific(row, col):
            return -1, 1

        atlantic, pacific = -1, -1
        
        for rowDiff, colDiff in directions:
            rowNew, colNew = row + rowDiff, col + colDiff

            currH, nextH = self.getHeight(row, col), self.getHeight(rowNew, colNew)
            if nextH > currH or (rowNew, colNew) in path:
                continue

            visisted, atlan, paci = self.getVisisted(rowNew, colNew)
            if not visisted:
                path.add((row, col))
                atlan, paci = self.dfs(rowNew, colNew, path)
                path.remove((row, col))
            
            if atlan == 1:
                atlantic = 1
            
            if paci == 1:
                pacific = 1

            if atlantic == 1 and pacific == 1:
                break

            
        
        return atlantic, pacific

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = rows = len(heights)
        self.cols = cols = len(heights[0])
        self.heights = heights

        '''
            0: not visited
            -1: visisted and cannot reach to pacific (atlantic)
            1: visisted and can reach to pacific (atlantic)
        '''
        self.visisted = [[(0,0)] * cols for _ in range(rows)]

        results = []

        for row in range(rows):
            for col in range(cols):
                if row == 11 and col == 3:
                    print('here')
                atlantic, pacific = self.dfs(row, col, set([]))
                if pacific == 1 and atlantic == 1:
                    results.append([row, col])
                
                self.setVisisted(row, col, atlantic, pacific)

        return results

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
s = Solution()
print(s.pacificAtlantic(heights) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])
heights = [[1]]
print(s.pacificAtlantic(heights) == [[0,0]])
heights = [
    [1,1,1],
    [1,2,1],
    [1,1,1]
]
print(s.pacificAtlantic(heights))
heights = [
    [2,2,2],
    [2,1,2],
    [2,2,2]
]
print(s.pacificAtlantic(heights))

# heights=[[7,1,17,13,9,10,5,14,0,3],
# [7,15,7,8,15,16,10,10,5,13],
# [18,9,15,8,19,16,7,5,5,10],
# [15,11,18,3,1,17,6,4,10,19],
# [3,16,19,12,12,19,2,14,5,9],
# [7,16,0,13,14,7,2,8,6,19],
# [5,10,1,10,2,12,19,1,0,19],
# [13,18,19,12,17,17,4,5,8,2],
# [2,1,17,13,14,12,14,2,16,10],
# [5,8,1,11,16,1,18,15,6,19],
# [3,8,14,14,5,0,2,7,5,1],
# [17,1,9,17,10,10,10,7,1,16],
# [14,18,5,11,17,15,8,8,14,13],
# [6,4,10,17,8,0,11,4,2,8],
# [16,11,17,9,3,2,11,0,6,5],
# [12,18,18,11,1,7,12,16,12,12],
# [2,14,12,0,2,8,5,10,7,0],
# [16,13,1,19,8,13,11,8,11,3],
# [11,2,8,19,6,14,14,6,16,12],[18,0,18,10,16,15,15,12,4,3],[8,15,9,13,8,2,6,11,17,6],[7,3,0,18,7,12,2,3,12,10],[7,9,13,0,11,16,9,9,12,13],[9,4,19,6,8,10,12,6,7,11],[5,9,18,0,4,9,6,4,0,1],[9,12,1,11,13,13,0,16,0,6],[7,15,4,8,15,17,17,19,15,1],[7,17,4,1,1,14,10,19,10,19],[10,5,12,5,8,8,14,14,6,0],[16,10,10,7,13,4,0,15,18,0],[11,2,10,6,5,13,4,5,3,1],[9,14,16,14,15,3,2,13,17,8],[19,2,10,1,2,15,12,10,2,5],[12,4,8,9,8,6,4,14,14,0],[11,17,17,4,16,13,6,15,5,7],[12,18,1,3,9,10,7,1,1,1],[18,6,10,8,12,14,9,12,10,3],[15,13,18,13,8,5,12,14,18,0],[15,4,8,9,19,18,6,19,12,0],[4,14,15,4,17,17,9,17,9,0],[6,17,16,10,3,8,8,18,15,9],[3,8,4,2,13,0,2,8,8,2],[14,12,13,12,17,4,16,9,8,7],[0,19,8,16,1,13,7,6,15,11],[1,13,16,14,10,4,11,19,9,13],[8,0,2,1,16,12,16,9,9,9],[5,2,10,4,8,12,17,0,2,15],[11,2,15,15,14,9,11,19,18,11],[4,4,1,5,13,19,9,17,17,17],[4,1,8,0,8,19,11,0,5,4],[8,16,14,18,12,2,0,19,0,13],[7,11,3,18,8,2,2,19,8,7],[3,13,6,1,12,16,4,13,0,5],[12,1,16,19,2,12,16,15,19,6],[1,7,12,15,3,3,13,17,16,12]]
# s = Solution()
# print(s.pacificAtlantic(heights))