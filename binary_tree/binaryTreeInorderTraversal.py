from enum import Enum
from queue import Queue
import time
from typing import List
# Definition for a binary tree node.
class Direct(Enum):
    left = 1
    right = 2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)

# In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        stack = []
        traversal = []
        directs = []
        deep = -1 # deep of directs
        current = root
        index = 0 # deep of current node
        while current != None or len(stack) != 0:
            print('-----------------------------')
            print('stack', stack)
            print('directs', directs)
            print('traverse', traversal)
            print(current, deep, index)
            if current == None:
                current = stack.pop()
                index -= 1
            else:
                if deep == index:
                    prevDirect = directs[deep]
                    directs.pop()
                    if prevDirect == Direct.left:
                        traversal.append(current.val)
                        directs.append(Direct.right)
                        index += 1
                        stack.append(current)
                        current = current.right
                    if prevDirect == Direct.right:
                        if len(stack) > 0:
                            current = stack.pop()
                        else:
                            current = None
                        index -= 1
                        deep -= 1
                else:
                    directs.append(Direct.left)
                    stack.append(current)
                    current = current.left
                    deep += 1
                    index += 1
            print('```````````')
            print(len(stack))
        return traversal

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

def testValidTree(root: TreeNode):
    queue = Queue()
    queue.put(root)
    arr = []
    count = 1
    while not queue.empty():
        curr = queue.get()
        left, right = curr.left, curr.right
        arr.append(curr.val)
        if left != None:
            queue.put(left)
        if right != None:
            queue.put(right)
    return arr

root = createTree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(f'test valid tree {testValidTree(root)}')
solution = Solution()
traversal = solution.inorderTraversal(root)
print(traversal)
