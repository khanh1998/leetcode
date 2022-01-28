from typing import List


class Solution:
    def find(self, candidates: List[int], target: int, stack: List[int], res: List[List[int]], level: int):
        if target == 0:
            res.append([*stack])
            return
        for i, v in enumerate(candidates):
            if i > 0 and v == candidates[i - 1]:
                continue
            if v <= target:
                stack.append(v)
                self.find(candidates[i + 1:], target - v, stack, res, level + 1)
                stack.pop()
            else:
                break

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.find(sorted(candidates), target, [], res, 1)
        return res

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]])
print(s.combinationSum2([2,5,2,1,2], 5) == [[1,2,2],[5]])