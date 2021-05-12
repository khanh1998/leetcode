from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return 0 if root == None else self.hasPathSumNext(root, targetSum, 0)
    def hasPathSumNext(self, node: TreeNode, targetSum: int, prevSum: int) -> bool:
        if not node.left and not node.right:
            return True if targetSum == prevSum + node.val else False
        else:
            left, right = False, False
            if node.left:
                left = self.hasPathSumNext(node.left, targetSum, prevSum + node.val)
            if node.right:
                right = self.hasPathSumNext(node.right, targetSum, prevSum + node.val)
            return left or right

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

root = create_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print_value(root)
solution = Solution()
result = solution.hasPathSum(root, 15)
print(result)
