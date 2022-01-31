from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0 # farthest index you can go to
        for idx, jump in enumerate(nums): # this loop to calculate farthest index we can go to
            if idx > farthest: # you can not go to this current index, because it's too far :')
                return False
            farthest = max(farthest, idx + jump)
        return True

s = Solution()
print(s.canJump([2,3,1,1,4]) == True)
print(s.canJump([3,2,1,0,4]) == False)
print(s.canJump([0]) == True)