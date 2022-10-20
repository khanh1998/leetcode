from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        if length == 1:
            return 0
        items = sorted(intervals, key=lambda x: (x[0], x[1])) # sort by start value
        count = 0
        i, j = 0, 1
        while i < length - 1 and j <= length - 1:
            left, right = items[i], items[j]
            if left[1] > right[0]: # overlap
                count += 1
                if left[1] < right[1]:
                    j += 1
                else:
                    i = j
                    j += 1
            else:
                i = j
                j += 1
        return count

s = Solution()
print(s.eraseOverlapIntervals([[1,2],[1,3],[1,4]]) == 2)
print(s.eraseOverlapIntervals([[1,5],[2,5],[3,5]]) == 2)
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1)
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2)
print(s.eraseOverlapIntervals([[1,2],[2,3]]) == 0)
print(s.eraseOverlapIntervals([[1,6],[2,5],[3,4]]) == 2)
print(s.eraseOverlapIntervals([[1,6],[2,5],[3,4],[1,6]]) == 3)
print(s.eraseOverlapIntervals([[1,3],[4,6],[2,4],[3,5],[6,7]]) == 2)
print(s.eraseOverlapIntervals([[1,2],[2,3],[1,4]]) == 1)
print(s.eraseOverlapIntervals([[-2,3],[-1,2],[0,1]]) == 2)
print(s.eraseOverlapIntervals([[1,2]]) == 0)