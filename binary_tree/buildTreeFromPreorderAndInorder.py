# Definition for a binary tree node.
from typing import List
from queue import Queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        node_val = preorder[0]
        node = TreeNode(val=node_val)
        node_val_index = inorder.index(node.val)
        inorder_left, inorder_right = inorder[:node_val_index], inorder[node_val_index + 1:]
        preorder_left, preorder_right = preorder[1:node_val_index + 1], preorder[node_val_index + 1:]
        if len(inorder_left) > 0 and len(preorder_left) > 0:
            node.left = self.buildTree(preorder_left, inorder_left)
        if len(inorder_right) > 0 and len(preorder_right) > 0:
            node.right = self.buildTree(preorder_right, inorder_right)
        return node
    
    def printTree(self, node: TreeNode):
        queue = Queue()
        queue.put(node)
        values = []
        while not queue.empty():
            item = queue.get()
            values.append(item.val)
            if item.left:
                queue.put(item.left)
            if item.right:
                queue.put(item.right)
        print(values)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

solution = Solution()
tree = solution.buildTree(preorder, inorder)
solution.printTree(tree)