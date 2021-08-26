from queue import Queue
import math

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def __init__(self) -> None:
        self.queue = Queue()

    def getItemOut(self) -> 'Node':
        item = self.queue.get()
        if item.left:
            self.queue.put(item.left)
        if item.right:
            self.queue.put(item.right)

        return item
    
    def connect(self, root: 'Node') -> 'Node':
        self.queue.put(root)
        level = 0
        self.getItemOut()
        level += 1
        while not self.queue.empty():
            numOfNode = math.pow(2, level)
            if numOfNode > 1:
                first_node = self.getItemOut()
                for i in range(0, int(numOfNode - 1)):
                    second_node = self.getItemOut()
                    first_node.next = second_node
                    first_node = second_node
            level += 1
        
        return root
        