from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        intervals are non-overlapping
        '''
        starts, ends = [], []
        intervals.append(newInterval)
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
print(s.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]])
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]])