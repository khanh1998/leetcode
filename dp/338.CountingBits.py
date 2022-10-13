from math import log
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # time complexity: O(n)
        counts = [0] * (n + 1)
        for i in range(1, n + 1):
            div = i // 2
            if i % 2 == 0:
                counts[i] = counts[div]
            else:
                counts[i] = counts[div] + 1
        return counts

    def countBits1(self, n: int) -> List[int]:
        # time complexity: O(nlogn)
        results = []
        def count(n: int) -> int:
            c = 0
            while n != 0:
                c += 1
                x = int(log(n, 2))
                n -= 2 ** x
            return c
        
        for val in range(n + 1):
            results.append(count(val))
        return results

s = Solution()
print(s.countBits(0) == [0])
print(s.countBits(1) == [0,1])
print(s.countBits(2) == [0,1,1])
print(s.countBits(3) == [0,1,1,2])
print(s.countBits(4) == [0,1,1,2,1])
print(s.countBits(5) == [0,1,1,2,1,2])
print(s.countBits(6) == [0,1,1,2,1,2,2])
print(s.countBits(7) == [0,1,1,2,1,2,2,3])
print(s.countBits(8) == [0,1,1,2,1,2,2,3,1])
print(s.countBits(9) == [0,1,1,2,1,2,2,3,1,2])