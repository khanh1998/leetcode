from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        nums: sorted integer array
        '''
        result = []
        start = 0
        end = len(nums) - 1
        while start < end:
            # if nums[end] == nums[end - 1]:
            #     end -= 1
            #     continue
            # elif nums[start] == nums[start + 1]:
            #     start += 1
            #     continue
            two_sum = nums[start] + nums[end]
            if two_sum > target:
                end -= 1
            elif two_sum < target:
                start += 1
            else:
                result.append([nums[start], nums[end]])
                end -= 1
                start += 1
        print('two sum: ', result)
        return result
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        print(nums, target, k)
        result = []
        if k == 2:
            return self.twoSum(nums, target)
        for index, num in enumerate(nums):
            print('pick: ', num)
            diff = target - num
            res = self.kSum(nums[index+1:], diff, k - 1)
            for item in res:
                result.append([num, *item])
        return result
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        rawResult = self.kSum(nums, target, 4)
        result = []
        s = set()
        for item in rawResult:
            tup = tuple(item)
            if tup not in s:
                s.add(tup)
                result.append(item)
        return result

s = Solution()
a = [1,2,2,2,2,2]
print(s.fourSum(a, 7))
a = [1,0,-1,0,-2,2]
print(s.fourSum(a, 0))
