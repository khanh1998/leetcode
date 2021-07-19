from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def nextLevel(self, node: TreeNode, prevDepth: int) -> int:
        max_length = None
        if node == None:
            return prevDepth
        else:
            left = self.nextLevel(node.left, prevDepth + 1) 
            right = self.nextLevel(node.right, prevDepth + 1) 
            max_length = left if left > right else right
            return max_length
            
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.nextLevel(root, 0)

def create_tree(values: [int]) -> TreeNode:
    if len(values) == 0:
        return None
    root = TreeNode(val=values[0])
    values = values[1:] # remove first value
    node_queue = Queue()
    node_queue.put(root)
    while len(values) > 0:
        curr_node = node_queue.get()
        pair_values = values[:2]
        values = values[2:]
        # for left node first
        left_value = pair_values[0]
        pair_values = pair_values[1:]
        left_node = TreeNode(val=left_value)
        curr_node.left = left_node
        node_queue.put(left_node)
        if len(pair_values) == 1:
            right_value = pair_values[0]
            right_node = TreeNode(val=right_value)
            curr_node.right = right_node
            node_queue.put(right_node)
    return root

root = create_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
solution = Solution()
depth = solution.maxDepth(root)
print(depth)
