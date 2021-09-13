# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List
import time

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        print('-----------------------------------------')
        shorter = None
        longer = None
        if len(nums1) > len(nums2):
            shorter = nums2
            longer = nums1
        else:
            shorter = nums1
            longer = nums2
        if len(shorter) == 0 and len(longer) > 0:
            mid = len(longer) // 2
            if len(longer) % 2 == 0:
                return (longer[mid-1] + longer[mid]) / 2
            else:
                return longer[mid]
        startIdx = 1
        endIdx = len(shorter)
        total_length = len(nums1) + len(nums2)
        half_length = (len(nums1) + len(nums2)) // 2
        shorter.append(float('inf'))
        longer.append(float('inf'))
        shorter.insert(0, float('-inf'))
        longer.insert(0, float('-inf'))
        print(shorter, longer, total_length, half_length)
        while startIdx <= endIdx:
            print('start: ', startIdx, 'end: ', endIdx)
            centerIdxShorter = (startIdx + endIdx) // 2
            centerIdxLonger = None
            if total_length % 2 == 0:
                centerIdxLonger = half_length - centerIdxShorter
            else:
                centerIdxLonger = half_length - centerIdxShorter
            print('center idx shorter: ', centerIdxShorter, 'center idx longer: ', centerIdxLonger)
            print(shorter[centerIdxShorter], ' < ', longer[centerIdxLonger + 1], longer[centerIdxLonger], ' < ', shorter[centerIdxShorter + 1])
            if shorter[centerIdxShorter] <= longer[centerIdxLonger + 1] and longer[centerIdxLonger] <= shorter[centerIdxShorter + 1]:
                if total_length % 2 == 0:
                    maximum = max(shorter[centerIdxShorter], longer[centerIdxLonger])
                    minimum = min(shorter[centerIdxShorter + 1], longer[centerIdxLonger + 1])
                    print(maximum, minimum) 
                    return (maximum + minimum) / 2
                else:
                    return min(shorter[centerIdxShorter + 1], longer[centerIdxLonger + 1])
            else:
                if shorter[centerIdxShorter] >= longer[centerIdxLonger + 1]:
                    # move to left side
                    endIdx = centerIdxShorter - 1
                    startIdx = 0
                elif longer[centerIdxLonger] >= shorter[centerIdxShorter + 1]:
                    # move to right
                    startIdx = centerIdxShorter + 1

s = Solution()
print(s.findMedianSortedArrays([1,2,3], [4,5,6]) == 3.5)
print(s.findMedianSortedArrays([1,2,3,4,5,6], [1,2,3,4,5,6]) == 3.5)
print(s.findMedianSortedArrays([1,2,3,5,6,7], [1,2,3,4,5,6,7]) == 4)
print(s.findMedianSortedArrays([1,2,3,5,6,7], [5,6,7,8,9,10]) == 6)
print(s.findMedianSortedArrays([1,2,3,4,5,6], [7,8,9]) == 5)
print(s.findMedianSortedArrays([1,2,3,4], [5,6,7]) == 4)
print(s.findMedianSortedArrays([1,2,3], [4,5,6,7]) == 4)
print(s.findMedianSortedArrays([1,3], [2]) == 2)
print(s.findMedianSortedArrays([1,2], [3,4]) == 2.5)
print(s.findMedianSortedArrays([0,0], [0,0]) == 0)
print(s.findMedianSortedArrays([], [1]) == 1)
print(s.findMedianSortedArrays([], [2,3]) == 2.5)
print(s.findMedianSortedArrays([], [2,3,4]) == 3)
print(s.findMedianSortedArrays([1], [1]) == 1)
print(s.findMedianSortedArrays([1,1,1,1], [1]) == 1)