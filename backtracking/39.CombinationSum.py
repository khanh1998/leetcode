from typing import List

class Solution:
    def find(self, candidates: List[int], target: int, stack: List[int], level: int, res: List[List[int]]):
        if target == 0:
            res.append([*stack])
            return
        for i, v in enumerate(candidates):
            # print('level: ', level, 'num: ', v, 'target: ', target, i < target, stack)
            if v <= target:
                stack.append(v)
                self.find(candidates[i:], target - v, stack, level + 1, res)
                stack.pop()
            else:
                break

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.find(sorted(candidates), target, [], 0, res)
        return res

s = Solution()
print(s.combinationSum([2,3,6,7], 7) == [[2,2,3],[7]])
print(s.combinationSum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]])
print(s.combinationSum([2], 1) == [])