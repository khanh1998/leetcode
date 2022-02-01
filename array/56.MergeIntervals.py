from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        starts, ends = [], []
        for i in intervals:
            starts.append(i[0])
            ends.append(i[1])
        starts = sorted(starts)
        ends = sorted(ends)
        starts.append(float('inf'))
        res = []
        length = len(ends)
        start, end = None, None
        for i in range(length):
            if start == None:
                start = starts[i]
            if ends[i] < starts[i + 1]:
                end = ends[i]
            if end != None and start != None:
                res.append([start, end])
                start, end = None, None
        return res

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1, 6], [8, 10], [15, 18]])
print(s.merge([[1,4],[2,5],[3,6],[2,5],[6,8]]) == [[1,8]])
print(s.merge([[1,4],[4,5]]) == [[1,5]])
print(s.merge([[1,4]]) == [[1,4]])
print(s.merge([[1,3], [4,5]]) == [[1,3], [4,5]])
print(s.merge([[1,10], [2,4]]) == [[1,10]])
print(s.merge([[1,10], [2,4], [11, 13]]) == [[1,10], [11,13]])
