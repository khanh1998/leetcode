from queue import Queue
import pprint
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)

class Solution:
    def preorderTraversal(self, root: TreeNode) -> [int]:
        left = 'left'
        right = 'right'
        node_queue = Queue()    
        values = []
        node_stack = [root]
        deep = 0
        direct_stack = [None]
        pp = pprint.PrettyPrinter(indent=2)
        while len(node_stack) > 0:
            pp.pprint({'stack': node_stack})
            pp.pprint({'diret': direct_stack})
            pp.pprint({'deep': deep})
            pp.pprint('-----------------------')
            curr_direct = direct_stack[deep]
            curr_node = node_stack[deep]
            if curr_node == None:
               node_stack.pop()
               direct_stack.pop()
               deep -= 1
            else:
                if curr_direct == None:
                    values.append(curr_node.val)
                    direct_stack[deep] = left
                    node_stack.append(curr_node.left)
                    direct_stack.append(None)
                    deep += 1
                if curr_direct == left:
                    direct_stack[deep] = right
                    node_stack.append(curr_node.right)
                    direct_stack.append(None)
                    deep += 1
                if curr_direct == right:
                    node_stack.pop()
                    direct_stack.pop()
                    deep -= 1
        print(values)
        return values

def create_tree(values: [int]) -> TreeNode:
    level = 1
    root = TreeNode(values[0])
    values = values[1:].copy()
    node_queue = Queue()
    node_queue.put(root)
    while len(values) > 0:
        curr_node = node_queue.get()
        [left_value, right_value] = values[:2]
        values = values[2:]
        left_node = TreeNode(left_value)
        right_node = TreeNode(right_value)
        curr_node.left = left_node
        curr_node.right = right_node
        node_queue.put(left_node)
        node_queue.put(right_node)
    return root

def print_value(root: TreeNode):
    node_queue = Queue()
    node_queue.put(root)
    values = []
    while not node_queue.empty():
        curr = node_queue.get()
        if curr != None:
            values.append(str(curr.val))
            node_queue.put(curr.left)
            node_queue.put(curr.right)
    string = ', '.join(values)
    print(string)
    return string

root = create_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print_value(root)
solution = Solution()
solution.preorderTraversal(root)
