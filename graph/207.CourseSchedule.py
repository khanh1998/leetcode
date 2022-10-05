from typing import List, Set


PROCESSED = -1
UNPROCESSED = 0
PROCESSING = 1

class Solution:
    def __init__(self) -> None:
        self.adjacencyList = None

    def dfs(self, course: int, adjacencyList: List[List[int]], state: List[int]) -> bool:
        state[course] = PROCESSING

        for neighbor in adjacencyList[course]:
            if state[neighbor] is PROCESSED:
                continue
            if state[neighbor] is PROCESSING:
                return False
            can = self.dfs(neighbor, adjacencyList, state)
            if not can:
                return False

        state[course] = PROCESSED

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = [[] for _ in range(numCourses)]
        for item in prerequisites:
            course, prerequisite = item
            adjacencyList[course].append(prerequisite)
        state = [UNPROCESSED] * numCourses
        for c in range(numCourses):
            r = self.dfs(c, adjacencyList, state)
            if r == False:
                return False
        return True

s = Solution()
print(s.canFinish(numCourses=3,prerequisites=[[1,0],[2,1],[0,2]]) == False)
print(s.canFinish(numCourses=3,prerequisites=[[1,0],[2,1]]) == True)
print(s.canFinish(numCourses=3,prerequisites=[]) == True)
print(s.canFinish(numCourses=1,prerequisites=[]) == True)
print(s.canFinish(numCourses=4,prerequisites=[[1,0],[2,1],[0,2],[3,1]]) == False)
print(s.canFinish(numCourses=5,prerequisites=[[1,0],[2,1],[0,2],[3,1],[4,3]]) == False)
print(s.canFinish(numCourses=5,prerequisites=[[1,0],[2,1],[0,2],[3,1],[4,2]]) == False)
print(s.canFinish(numCourses=4,prerequisites=[[1,0],[2,1],[3,2],[1,3]]) == False)
print(s.canFinish(numCourses=4,prerequisites=[[1,0],[2,1],[3,2],[3,1]]) == True)