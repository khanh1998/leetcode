# https://leetcode.com/problems/next-permutation
# refer to: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
from typing import List

class Solution:
    def inPlaceReverse(self, nums: List[int], start: int = None, end: int = None):
        if start is None:
            start = 0
        if end is None:
            end = len(nums) - 1
        for i in range((end - start + 1) // 2):
            tmp = nums[start + i] 
            nums[start + i] = nums[end - i]
            nums[end - i] = tmp

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        pivot = None
        for i in reversed(range(1, length)):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break
        # if pivot != None:
        #     print('pivot: ', pivot, nums[pivot])
        # all numbers in the list are in descending order
        # so the next permutation is the reversed of current list
        if pivot == None:
            self.inPlaceReverse(nums)
            return
        # find the number to replace
        idx = length - 1
        for i in range(pivot + 1, length - 1):
            if nums[i + 1] <= nums[pivot]:
                idx = i
                break
        # print('to be replaced: ', idx, nums[idx])
        # swap
        tmp = nums[pivot]
        nums[pivot] = nums[idx]
        nums[idx] = tmp
        # print('before reversed: ', nums)
        # reverse
        self.inPlaceReverse(nums, pivot + 1)
        

s = Solution()
a = [0,1,2,5,3,3,0]
s.nextPermutation(a)
print(a == [0,1,3,0,2,3,5])

a = [1,2,3,4,5,6]
s.nextPermutation(a)
print(a == [1,2,3,4,6,5])

a = [2,6,5,4,3]
s.nextPermutation(a)
print(a == [3,2,4,5,6])

a = [9, 5, 4, 3, 1]
s.nextPermutation(a)
print(a == [1,3,4,5,9])
        
a = [1,5,1]
s.nextPermutation(a)
print(a == [5,1,1])

a = [1,2,3,6,5,4]
s.nextPermutation(a)
print(a == [1,2,4,3,5,6])