class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numToIndices = {}
        for index, num in enumerate(nums):
            indices = numToIndices.get(num)
            if indices is None:
                numToIndices[num] = [index]
            else:
                for idx in indices:
                    if abs(index - idx) <= k:
                        return True
                numToIndices[num].append(index)
        return False