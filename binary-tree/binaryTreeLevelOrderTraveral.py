from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) ->[[int]]:
        if root == None:
            return []
        node_queue = Queue()        
        node_queue.put(root)
        values = []
        level = 0
        num_node_level = 1
        while not node_queue.empty():
            level_values = []
            num_node_next_level = 0
            for index in range(num_node_level):
                if not node_queue.empty():
                    node = node_queue.get()
                    level_values.append(node.val)
                    if node.left:
                        node_queue.put(node.left)
                        num_node_next_level += 1
                    if node.right:
                        node_queue.put(node.right)
                        num_node_next_level += 1
                else:
                    break
            num_node_level = num_node_next_level
            values.append(level_values)
            level_values = []
            level += 1
        return values;

def create_tree(values: [int]) -> TreeNode:
    root = TreeNode(val=values[0])
    values = values[1:] 
    node_queue = Queue()
    node_queue.put(root)
    while len(values) > 0:
        node = node_queue.get()
        pairValues = values[:2]
        left_value = pairValues[0]
        values = values[1:]
        left_node = TreeNode(val=left_value)
        node.left = left_node
        node_queue.put(left_node)
        if len(pairValues) == 2:
            right_value = pairValues[1]
            values = values[1:]
            right_node = TreeNode(val=right_value)
            node.right = right_node
            node_queue.put(right_node)
    return root

tree = create_tree([1,2,3,4])
solution = Solution()
result = solution.levelOrder(tree)
print(result)
