import time

class Solution:
    def search(self, nums: [int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while end >= start:
            middle = (end + start) // 2
            middle_value = nums[middle]
            print(f'start: {start}, end: {end}, middle: {middle}, middle value: {middle_value}')
            if target == middle_value:
                return middle
            elif target < middle_value:
                end = middle - 1
            elif target > middle_value:
                start = middle + 1
            print(f'start: {start}, end: {end}, middle: {middle}, middle value: {middle_value}')
            time.sleep(2)
        return -1

nums = [5]
target = 5
s = Solution()
print(s.search(nums, target))
