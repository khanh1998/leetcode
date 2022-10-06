from queue import Queue
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, node: Optional[TreeNode]) -> List[int]:
        if node is None:
            return []
        left = self.inorder(node.left)
        right = self.inorder(node.right)
        return left + [node.val] + right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sort = self.inorder(root)
        return sort[k-1]

def buildBinaryTree(nums: List[int]) -> TreeNode:
    nodes = Queue()
    root = TreeNode(nums[0])
    nodes.put(root)
    numIdx = 0
    length = len(nums)

    def next() -> int:
        nonlocal numIdx
        numIdx += 1
        return nums[numIdx] if numIdx < length else None

    while not nodes.empty() or numIdx < length - 1:
        node = nodes.get()
        leftValue = next()
        if leftValue:
            node.left = TreeNode(val=nums[numIdx])
            nodes.put(node.left)
        rightValue = next()
        if rightValue:
            node.right = TreeNode(val=nums[numIdx])
            nodes.put(node.right)
    return root

s = Solution()
tree = buildBinaryTree([3,1,4,None,2])
print(s.kthSmallest(tree, 1) == 1)
tree = buildBinaryTree([3])
print(s.kthSmallest(tree, 1) == 3)
tree = buildBinaryTree([3,None,4])
print(s.kthSmallest(tree, 2) == 4)
tree = buildBinaryTree([3,1,4])
print(s.kthSmallest(tree, 2) == 3)
tree = buildBinaryTree([5,3,6,2,4,None,None,1])
print(s.kthSmallest(tree, 3) == 3)