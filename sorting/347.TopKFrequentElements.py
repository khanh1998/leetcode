import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        c = collections.Counter(nums)
        counts = [[] for _ in range(len(nums)+1)]
        for num, count in c.items():
            counts[count] += [num]
        result = []
        n, i = k, len(nums) - 1
        while n > 0:
            if len(counts[i]) > 0:
                result += counts[i]
                n -= len(counts[i])
            i -= 1
        return result