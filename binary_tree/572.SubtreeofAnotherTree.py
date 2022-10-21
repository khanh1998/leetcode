from queue import Queue
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, treeA: Optional[TreeNode], treeB: Optional[TreeNode]) -> bool:
        if treeA is None and treeB is None:
            return True
        if treeA is None or treeB is None:
            return False
        if treeA.val != treeB.val:
            return False
        isLeftSame = self.isSameTree(treeA.left, treeB.left)
        if not isLeftSame:
            return False
        return self.isSameTree(treeA.right, treeB.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right

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
root = buildBinaryTree([1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2])
subTree = buildBinaryTree([1,None,1,None,1,None,1,None,1,None,1,2])
print(s.isSubtree(root, subTree))