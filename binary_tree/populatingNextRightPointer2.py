from queue import Queue

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        above_queue = Queue()
        above_queue.put(root)
        while not above_queue.empty():
            # get all children of the above nodes
            tmp = Queue()
            below_queue = Queue()
            while not above_queue.empty():
                item = above_queue.get()
                if item and item.left:
                    below_queue.put(item.left)
                if item and item.right:
                    below_queue.put(item.right)
                tmp.put(item)
            above_queue = tmp
            # populates value to next pointer
            item = above_queue.get()
            if item:
                while not above_queue.empty():
                    nextItem = above_queue.get()
                    if nextItem:
                        item.next = nextItem
                        item = nextItem
            # move to below queue
            above_queue = below_queue
        return root
