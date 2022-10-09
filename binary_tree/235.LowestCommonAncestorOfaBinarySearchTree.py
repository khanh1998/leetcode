class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < node.val and q.val < node.val:
            return self.dfs(node.left, p, q)
        if p.val > node.val and q.val > node.val:
            return self.dfs(node.right, p, q)
        return node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)