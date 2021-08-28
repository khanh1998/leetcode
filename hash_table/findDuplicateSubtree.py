from queue import Queue
from typing import List, Optional
import sys
sys.path.append(sys.path[0] + '\\..')

from binary_tree.serializeAndDeserialize import Codec
# from binary_tree.binaryTreeInorderTraversal import Solution as BinaryTreeTraveser

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    map = {}

    def inorder(self, root: Optional[TreeNode]) -> tuple:
        left, right, wholeTree = None, None, None
        if root.left != None:
            left = self.inorder(root.left)

        if root.right != None:
            right = self.inorder(root.right)


        if left and right:
            # both left and right subtree
            wholeTree = (*left, root.val, *right)
        elif left:
            # only left subtree
            # -1 represent for the node that only have left children
            wholeTree = (*left, -1, root.val,)
            # because sometimes, inorder traverse result of a subtree that only have left child
            # and a subtree that only have right child are the same.
            # that is why I need -1 and -2 to differentiate these cases.
        elif right:
            # only right subtree
            # -2 repersent for the node that only have right children
            wholeTree = (root.val, -2, *right)
        else:
            # no right subtree and no left subtree
            wholeTree = (root.val,)
    
        self.count(wholeTree, root)
        return wholeTree

    def count(self, key: tuple, root: TreeNode):
        value = self.map.get(key, None)
        if not value:
            self.map[key] = { 'count': 1, 'root': root }
        else:
            self.map[key] = { 'count': value.get('count') + 1, 'root': value.get('root') }

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.map = {}
        self.inorder(root)
        codec = Codec()
        result = []
        for key, value in self.map.items():
            print(key, codec.serialize(value.get('root')), value.get('count'))
            if value.get('count') > 1:
                result.append(value.get('root'))
        return result

def createTree(inputValues: List[int]) -> TreeNode:
    queue = Queue()
    root = TreeNode(inputValues[0]) 
    queue.put(root)
    remainValues = inputValues[1:]
    level = 1
    while len(remainValues) > 0:
        breakPoint = pow(2, level)
        values = remainValues[:breakPoint]
        for pair in zip(values[::2], values[1::2]):
            left, right = pair
            print('-------------')
            print(f'left: {left}, right: {right}')
            node = queue.get()
            print(f'current node: {node.val}')
            leftNode = TreeNode(left)
            rightNode = TreeNode(right)
            node.left = leftNode
            node.right = rightNode
            queue.put(leftNode)
            queue.put(rightNode)
        level += 1
        remainValues = remainValues[breakPoint:]
    return root
solution = Solution()
codec = Codec()
data = [94,93,95,92,94,96,94,93,93,93,95,97,97,95,95,92,94,94,94,92,94,94,96,98,98,96,98,96,94,94,96,91,91,93,95,93,95,95,95,91,93,93,95,95,93,97,97,97,97,97,99,95,97,97,99,95,97,93,95,None,95,95,95,90,92,90,92,92,94,94,96,94,None,96,94,94,94,96,None,90,92,None,None,94,None,94,96,None,None,None,None,96,None,None,None,96,98,96,96,96,96,100,100,94,94,98,96,96,96,98,100,94,96,98,98,94,94,94,96,None,None,94,96,94,94,89,91,None,93,91,91,91,91,None,91,None,None,None,None,None,None,93,95,95,95,93,95,None,None,95,93,None,None,None,None,None,93,None,95,93,95,None,97,95,97,95,95,97,99,97,97,None,97,95,None,95,97,101,101,99,99,95,None,93,None,97,99,95,97,97,97,95,95,99,97,101,99,93,93,95,97,97,99,99,None,None,None,None,95,95,95,97,95,None,None,95,None,None,95,None,None,88,88,92,None,None,94,90,92,92,92,90,90,90,92,90,92,None,None,None,94,94,96,None,None,None,94,None,None,None,None,94,None,None,None,94,None,None,None,96,None,96,96,94,94,None,None,None,96,96,94,96,96,100,100,96,98,96,96,None,96,94,None,94,96,None,None,100,102,100,None,None,100,98,98,94,96,92,94,96,98,98,98,94,94,96,98,96,98,96,98,None,96,96,94,98,98,96,98,100,102,98,None,92,94,92,94,96,None,None,None,96,98,98,100,100,100,94,96,94,None,None,96,96,98,None,None,None,None,96,94,None,None,87,89,91,None,None,None,89,89,None,91,93,93,None,93,89,91,89,91,91,89,93,None,91,None,None,None,None,93,None,None,None,None,None,None,None,None,None,None,None,None,None,95,97,None,95,None,None,95,95,97,95,97,95,None,95,95,97,97,101,101,101,101,95,95,97,99,95,None,95,97,97,None,95,None,93,95,None,None,None,None,101,103,99,None,None,101,None,None,None,None,None,93,97,97,None,91,None,95,97,97,97,None,97,None,97,99,95,95,93,None,None,97,97,None,95,None,None,99,95,97,97,99,95,97,95,97,93,95,99,97,97,99,95,97,97,99,99,99,101,101,None,99,91,None,None,None,None,None,None,93,None,97,95,95,97,None,97,97,101,99,None,99,99,None,None,None,97,97,None,None,None,None,97,97,None,None,None,95,None,None,None,None,None,None,None,None,None,None,None,None,92,None,None,None,None,None,None,94,88,None,None,None,90,90,None,None,None,None,88,88,None,None,None,90,None,None,None,None,None,None,None,None,96,96,96,96,96,96,96,94,None,None,96,96,94,None,94,96,96,None,98,96,100,102,None,None,102,102,None,100,94,96,94,None,96,98,98,None,94,96,96,None,98,None,None,None,96,94,None,None,None,94,None,None,None,104,None,100,None,102,None,None,96,96,96,96,None,92,None,96,None,96,None,None,96,None,None,None,None,None,98,None,None,None,94,94,None,None,None,98,None,96,None,None,100,None,96,96,96,98,96,98,98,100,94,None,None,None,None,None,None,98,94,92,96,96,None,100,96,None,98,None,98,100,94,94,96,98,None,96,98,100,98,98,100,100,102,100,100,None,None,None,None,92,92,None,None,None,96,94,None,96,98,98,96,98,96,None,102,None,98,None,None,None,100,100,None,None,None,None,96,98,96,98,None,94,None,None,95,None,87,None,None,91,91,91,87,None,None,89,91,None,None,None,None,None,None,None,None,None,97,95,95,97,None,None,None,None,97,95,None,None,93,None,95,93,None,None,95,None,97,99,95,95,99,None,None,103,101,None,None,103,None,99,95,95,None,95,95,93,None,97,None,None,None,None,93,95,95,97,None,None,None,None,97,None,None,None,None,None,None,None,101,None,101,103,97,97,95,None,None,None,None,97,None,None,95,None,None,None,None,97,None,None,93,93,None,None,97,None,None,None,99,None,95,95,None,None,97,95,None,None,95,None,97,None,97,99,99,None,None,None,None,99,93,95,91,93,97,97,95,95,101,99,None,None,None,None,99,None,None,None,93,None,93,95,97,95,97,99,95,95,97,99,99,101,97,None,None,99,99,99,None,None,103,103,101,101,None,101,None,93,None,91,None,95,None,95,None,97,99,99,97,99,97,97,97,None,95,95,None,None,None,97,101,99,99,101,None,None,None,None,95,None,None,None,93,None,None,None,None,88,None,None,None,None,None,None,None,None,88,None,90,92,None,None,94,96,None,None,96,96,98,None,96,96,None,None,94,96,92,None,94,None,96,98,100,100,None,96,94,None,None,None,102,None,None,None,None,102,None,None,94,94,94,96,None,96,None,None,92,94,96,None,94,None,94,94,None,96,None,98,None,None,None,100,100,102,None,None,98,None,96,98,None,None,None,None,None,None,None,None,94,94,None,94,None,None,None,None,94,96,96,96,96,96,None,96,None,None,96,96,98,98,None,100,98,100,None,None,None,94,94,96,92,92,92,94,None,98,None,98,94,96,94,96,None,None,None,100,None,None,92,None,92,94,None,96,98,96,96,None,98,98,98,None,96,None,96,96,None,None,None,100,98,None,None,100,96,98,None,None,98,98,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,96,96,98,None,None,100,100,96,98,100,98,None,None,96,98,98,98,96,None,94,None,None,None,None,100,98,None,100,None,None,102,None,None,None,None,None,None,87,None,None,None,None,None,95,95,None,97,None,None,None,97,97,None,95,97,95,97,95,None,None,None,None,None,None,None,95,None,None,None,None,None,None,101,97,None,93,None,None,None,None,103,None,None,95,None,95,93,95,95,95,None,None,93,None,93,None,None,None,None,95,95,None,None,95,97,97,99,None,None,None,None,103,None,None,None,95,95,99,None,93,None,None,None,None,None,93,95,97,95,95,97,None,97,97,None,95,None,None,None,None,None,95,97,99,97,97,99,None,None,99,97,101,None,95,None,None,93,97,97,91,93,91,93,93,91,93,93,None,None,99,97,93,93,95,97,93,None,None,95,None,None,None,93,91,93,95,95,95,97,None,None,None,None,None,None,99,None,None,None,None,None,97,None,95,None,None,None,None,None,99,None,None,None,95,95,None,97,97,None,99,99,95,None,None,None,None,None,None,101,99,None,95,95,None,None,None,None,97,99,None,95,99,None,97,None,None,None,97,None,None,None,101,None,99,None,None,None,103,None,None,None,None,None,94,94,None,None,None,None,None,98,94,94,None,None,None,None,96,None,96,None,None,96,None,102,None,98,None,None,None,None,None,None,None,None,94,94,None,94,96,94,None,None,None,None,None,None,None,94,94,None,None,None,None,None,None,None,None,100,None,None,96,94,None,96,None,None,None,None,94,None,None,None,None,96,None,None,94,None,None,96,None,None,96,None,None,None,None,None,96,None,None,None,96,96,None,98,None,None,98,None,None,None,None,102,None,None,92,94,96,None,96,96,None,90,None,None,92,92,None,92,92,None,None,92,None,92,94,92,None,100,96,None,94,None,None,94,96,None,98,None,92,94,94,96,None,None,92,90,None,None,94,None,94,96,94,96,98,96,None,None,None,None,94,96,None,None,94,None,94,94,None,None,None,98,98,None,None,100,None,None,None,102,None,None,96,None,None,96,None,None,None,None,96,None,100,None,None,None,None,None,None,102,None,None,104,104,None,None,None,None,None,97,None,95,95,None,95,97,None,None,95,None,None,103,None,97,95,95,None,None,93,93,None,None,None,95,None,None,None,93,None,None,97,None,93,None,None,None,None,None,95,None,None,None,None,None,None,None,95,97,95,None,95,None,97,99,None,None,None,None,91,93,None,95,None,None,None,97,95,None,89,None,None,91,None,None,None,None,None,None,None,None,91,None,93,95,93,91,None,None,95,None,93,None,95,None,None,None,None,None,None,93,None,None,None,95,None,None,None,None,89,None,None,95,None,None,95,None,95,93,None,None,None,97,95,None,None,None,95,None,None,None,None,95,None,95,99,None,97,None,None,None,None,103,95,None,95,None,None,97,None,None,None,None,None,None,None,None,None,None,None,96,94,None,None,None,98,None,None,None,104,None,None,None,None,None,None,None,None,None,94,94,None,None,None,94,None,98,94,None,None,96,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,94,None,None,None,None,None,None,None,None,None,92,None,None,None,None,94,None,94,None,92,None,94,92,94,94,96,94,92,None,None,None,None,94,94,None,None,96,None,92,None,96,None,None,None,None,None,None,None,94,None,None,None,96,None,None,102,None,None,None,None,None,None,None,None,None,None,None,None,None,None,93,None,93,None,None,None,99,None,None,None,None,None,None,None,None,None,None,None,None,None,None,91,None,None,None,91,None,None,None,None,None,97,None,None,None,91,None,95,None,None,None,None,None,None,None,97,None,None,None,None,101,None,94,None,None,None,None,None,None,92,None,None,None,96,None,None,94,None,None,96,None,None,93,None,None,None,None,None,None,None,97]
# tree = codec.deserialize([0,0,0,0,None,None,0,None,None,None,0])
tree = codec.deserialize(data)
print(codec.serialize(tree))
print('build tree success')
result = solution.findDuplicateSubtrees(tree)
print(len(result))
for t in result:
    print(codec.serialize(t))