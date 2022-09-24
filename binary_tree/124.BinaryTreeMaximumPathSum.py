# Definition for a binary tree node.
from queue import Queue
from typing import Iterable, List, Optional, Tuple

MIN = -1001

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def find(self, node: Optional[TreeNode]) -> Tuple[int, int]:
        '''
            the first int: max path to connect with parent node to form a new path.
            the second int: max path we can found in the subtree, candidate for the biggest path of the problem.
        '''
        if node == None:
            return MIN, MIN
        leftMaxBranch, leftMax = self.find(node.left)
        rightMaxBranch, rightMax = self.find(node.right)
        maxBranch = node.val + max(leftMaxBranch, rightMaxBranch, 0)
        maxPath = max(leftMax, rightMax, node.val + leftMaxBranch + rightMaxBranch, maxBranch)
        return maxBranch, maxPath

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _, maxPath = self.find(root)
        return maxPath

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
tree = buildBinaryTree([-1,-2,-3,-4])
print(s.maxPathSum(tree) == -1)
tree = buildBinaryTree([-10,9,20,None,None,15,7])
print(s.maxPathSum(tree) == 42)
tree = buildBinaryTree([10,9,-10,None,None,15,7])
print(s.maxPathSum(tree) == 24)
tree = buildBinaryTree([1,2,3])
print(s.maxPathSum(tree) == 6)
tree = buildBinaryTree([1])
print(s.maxPathSum(tree) == 1)
tree = buildBinaryTree([-1])
print(s.maxPathSum(tree) == -1)
tree = buildBinaryTree([-1, 2])
print(s.maxPathSum(tree) == 2)
tree = buildBinaryTree([-5, -4])
print(s.maxPathSum(tree) == -4)
tree = buildBinaryTree([5, 4])
print(s.maxPathSum(tree) == 9)
tree = buildBinaryTree([5, None, 4])
print(s.maxPathSum(tree) == 9)
tree = buildBinaryTree([5, 1, -2, None, None, -3, -4])
print(s.maxPathSum(tree) == 6)
tree = buildBinaryTree([-5, 1, -2, None, None, -3, -4])
print(s.maxPathSum(tree) == 1)