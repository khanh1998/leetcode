from typing import List
# the idea here is to use binary search,
# but we won't stop when the algo hit the target,
# we keep searching util searching-range is 0.
# we apply binary search two times, to find the indexes.

class Solution:
    def searchBoudary(self, nums: List[int], target: int, left: bool) -> List[int]:
        l, r, mid = 0, len(nums) - 1, None
        res = -1
        while l <= r:
            mid = (l + r) // 2
            # print('---')
            # print(l, mid, r)
            # print(nums[l], nums[mid], nums[r])
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] == target:
                # the surprising thing is here,
                # we don't stop when we hit the target
                res = mid
                if left == True:
                    r = mid - 1
                else:
                    l = mid + 1
        return res
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.searchBoudary(nums, target, left=True)
        right = self.searchBoudary(nums, target, left=False)
        res = [left, right]
        return res

s = Solution()
print(s.searchRange([], 0) == [-1, -1])
print(s.searchRange([1], 1) == [0, 0])
print(s.searchRange([1, 1], 1) == [0, 1])
print(s.searchRange([1, 1, 1], 1) == [0, 2])
print(s.searchRange([1,2,3,4,4,4,4,4,4,5,5,6,6,7,8,9], 4) == [3, 8])
print(s.searchRange([5,7,7,8,8,10], 8) == [3, 4])
print(s.searchRange([5,7,7,8,8,10], 5) == [0, 0])
print(s.searchRange([5,7,7,8,8,10], 7) == [1, 2])
print(s.searchRange([5,7,7,8,8,10], 6) == [-1, -1])