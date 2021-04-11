from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return False
        else:
            return self.compare(root.left, root.right)
    def compare(self, left: TreeNode, right: TreeNode) -> bool:
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val == right.val:
            outer = self.compare(left.left, right.right)
            inner = self.compare(left.right, right.left)
            return outer and inner
        else:
            return False

def create_tree(values: [int]) -> TreeNode:
    queue = Queue()
    root = TreeNode(values[0])
    values = values[1:]
    queue.put(root)
    while len(values) > 0:
        curr_node = queue.get()
        left_value = values[0]
        values = values[1:]
        left_node = TreeNode(left_value)
        curr_node.left = left_node
        queue.put(left_node)
        if len(values) >= 1:
            right_value = values[0]
            values = values[1:]
            right_node = TreeNode(right_value)
            curr_node.right = right_node
            queue.put(right_node)
    return root

def print_value(root: TreeNode):
    node_queue = Queue()
    node_queue.put(root)
    values = []
    level = 0
    while not node_queue.empty():
        level_values = []
        for i in range(pow(2, level)):
            curr = node_queue.get()
            if curr != None:
                level_values.append(str(curr.val))
                node_queue.put(curr.left)
                node_queue.put(curr.right)
        if len(level_values) > 0:
            values.append(level_values)
        level += 1
    print(values)
    return values

root = create_tree([1,2,2,3,3,3,3])
solution = Solution()
result = solution.isSymmetric(root)
print_value(root)
print(f'is symmetric: {result}')
