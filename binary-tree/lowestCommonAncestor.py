# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self) -> None:
        self.p_path = None
        self.q_path = None
        self.tmp_path = []
    
    def findNode(self, current: 'TreeNode', p_value: int, q_value: int):
        self.tmp_path.append(current)
        if self.q_path and self.p_path:
            return # stop
        if current.val == p_value:
            self.p_path = [val for val in self.tmp_path]
        if current.val == q_value:
            self.q_path = [val for val in self.tmp_path]
        if current.left:
            self.findNode(current.left, p_value, q_value)
        if current.right:
            self.findNode(current.right, p_value, q_value)
        self.tmp_path.pop()

    def findCommonNode(self) -> 'TreeNode':
        for p in reversed(self.p_path):
            for q in reversed(self.q_path):
                if p == q:
                    return q

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.findNode(root, p.val, q.val)
        common = self.findCommonNode()
        return common