# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        firstIdx, lastIdx = 0, len(nums) - 1
        count = 0
        while lastIdx >= firstIdx and count < 20:
            count += 1
            middleIdx = (firstIdx + lastIdx) // 2
            first, last, middle = nums[firstIdx], nums[lastIdx], nums[middleIdx]
            # print(first, last, middle)
            if middle == target:
                return middleIdx
            if middle >= first and middle <= last:
                # normal case, the array is not rotated
                # it's just a ascending array
                # 1 2 3 4 5 6 7 8 9 10 11 12
                #             |
                if middle > target:
                    # target: 4
                    lastIdx = middleIdx - 1
                if middle < target:
                    # target: 10
                    firstIdx = middleIdx + 1

            else:
                # the array is rotated
                if middle >= first and middle >= last:
                    # 6 7 8 9 10 11 12 1 2 3 4 5
                    #            |
                    # F                        L
                    if middle < target:
                        # 6 7 8 9 10 11 12 1 2 3 4 5
                        #            |
                        #               F          L
                        firstIdx = middleIdx + 1
                    if middle > target:
                        if target <= last:
                            # 6 7 8 9 10 11 12 1 2 3 4 5
                            #            |
                            #               F          L
                            # target: 3
                            firstIdx = middleIdx + 1
                        if target > last:
                            # 6 7 8 9 10 11 12 1 2 3 4 5
                            #            |
                            # F        L
                            # target: 7
                            lastIdx = middleIdx - 1
                if middle <= first and middle <= last:
                    # 10 11 12 1 2 3 4 5 6 7 8 9
                    #              |
                    if middle < target:
                        if target > last:
                            # 10 11 12 1 2 3 4 5 6 7 8 9
                            #              |
                            # F          L
                            # target: 11
                            lastIdx = middleIdx - 1
                        if target <= last:
                            # 10 11 12 1 2 3 4 5 6 7 8 9
                            #              |
                            #                F         L
                            # target: 7
                            firstIdx = middleIdx + 1
                    if middle > target:
                        # 10 11 12 1 2 3 4 5 6 7 8 9
                        #              |
                        # F          L
                        # target: 2
                        lastIdx = middleIdx - 1
        return -1

s = Solution()
# not rotated array
print(s.search([1,2,3,4,5,6,7,8,9], 4) == 3)
print(s.search([1,2,3,4,5,6,7,8,9], 1) == 0)
print(s.search([1,2,3,4,5,6,7,8,9], 9) == 8)
print(s.search([1,2,3,4,5,6,7,8,9], 7) == 6)
print(s.search([1,2,3,4,5,6,7,8,9], 10) == -1)
# rotated array
print(s.search([1], 1) == 0)
print(s.search([1], 2) == -1)
print(s.search([3, 1], 1) == 1)
print(s.search([4,5,6,7,8,9,0,1,2], 0) == 6)
print(s.search([4,5,6,7,8,9,0,1,2], 5) == 1)
print(s.search([4,5,6,7,8,9,0,1,2], 4) == 0)
print(s.search([4,5,6,7,8,9,0,1,2], 2) == 8)
print(s.search([4,5,6,7,8,9,0,1,2], 10) == -1)
print(s.search([8,9,10,1,2,3,4,5,6,7], 6) == 8)
print(s.search([8,9,10,1,2,3,4,5,6,7], 8) == 0)
print(s.search([8,9,10,1,2,3,4,5,6,7], 9) == 1)
print(s.search([8,9,10,1,2,3,4,5,6,7], 7) == 9)
print(s.search([8,9,10,1,2,3,4,5,6,7], 11) == -1)
