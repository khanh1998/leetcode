from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)

class Solution:
    def postorderTraversal(self, root: TreeNode) -> [int]:
        left = 'left'
        right = 'right'
        node_stack = [root]
        direct_stack = [None]
        deep = 0
        values = []
        while len(node_stack) > 0:
            print({ 'node_stack': node_stack })
            print({ 'direct_stack': direct_stack })
            print({ 'deep': deep })
            print({ 'direct nth', direct_stack[deep]})
            curr = node_stack[deep]
            if curr == None:
                node_stack.pop()
                direct_stack.pop()
                deep -= 1
            else:
                curr_direct = direct_stack[deep]
                if curr_direct == None:
                    node_stack.append(curr.left)
                    direct_stack[deep] = left
                    direct_stack.append(None)
                    deep += 1
                if curr_direct == left:
                    node_stack.append(curr.right)
                    direct_stack[deep] = right
                    direct_stack.append(None)
                    deep += 1
                if curr_direct == right:
                    node_stack.pop()
                    direct_stack.pop()
                    values.append(curr.val)
                    deep -= 1
        return values


def create_tree(values: [int]) -> TreeNode:
    root = TreeNode(values[0])
    values = values[1:]
    queue = Queue()
    queue.put(root)
    while len(values) > 0:
        node = queue.get()
        [left_value, right_value] = values[:2]
        values = values[2:]
        left_node = TreeNode(left_value)
        right_node = TreeNode(right_value)
        node.left = left_node
        node.right = right_node
        queue.put(left_node)
        queue.put(right_node)
    return root

def test_tree(root: TreeNode):
    queue = Queue()
    queue.put(root)
    values = []
    while not queue.empty():
        curr = queue.get()
        if curr:
            values.append(str(curr.val))
            queue.put(curr.left)
            queue.put(curr.right)
    print(', '.join(values))

root = create_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
test_tree(root)
solution = Solution()
print(solution.postorderTraversal(root))
