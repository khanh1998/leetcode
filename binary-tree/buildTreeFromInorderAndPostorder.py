from typing import List
from queue import Queue
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)

class TreeBuilder:
    def __init__(self):
        self.root = None

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        node = TreeNode(val=postorder[-1])
        parent_value_index = inorder.index(node.val)
        in_left, in_right = inorder[:parent_value_index], inorder[parent_value_index + 1:]
        post_left, post_right = postorder[:parent_value_index], postorder[parent_value_index:-1]
        if len(post_left) > 0 and len(in_left) > 0:
            node.left = self.buildTree(in_left, post_left)
        if len(post_right) > 0 and len(in_right) > 0:
            node.right = self.buildTree(in_right, post_right)
        return node

    def print_tree(self, tree: TreeNode):
        queue = Queue()
        queue.put(tree)
        values = []
        while not queue.empty():
            print('values ', values)
            item = queue.get()
            if item:
                values.append(item.val)
                queue.put(item.left)
                queue.put(item.right)
            else:
                values.append(None)
        return values



in_order   = [4, 8, 2, 5, 1, 6, 3, 7]
post_order = [8, 4, 5, 2, 6, 7, 3, 1]
in_order = [9,3,15,20,7]
post_order = [9,15,7,20,3]
treeBuilder = TreeBuilder()
root = treeBuilder.buildTree(in_order, post_order)
print(treeBuilder.print_tree(root))