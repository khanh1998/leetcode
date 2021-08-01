from queue import Queue

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Codec:

  def serialize(self, root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    if not root:
      return []
    values = []
    first_queue = Queue()
    first_queue.put(root)
    notNullCount = 1
    while notNullCount > 0:
      notNullCount = 0 # to count not null item in second queue
      second_queue = Queue()
      while not first_queue.empty():
        item = first_queue.get()
        if item:
          values.append(item.val)
          second_queue.put(item.left)
          second_queue.put(item.right)
          if item.left:
            notNullCount += 1
          if item.right:
            notNullCount += 1
        else:
          values.append(None)
      first_queue = second_queue
    return values

  def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if len(data) == 0:
      return None
    root = TreeNode(data[0])
    values = data[1:]
    queue = Queue()
    queue.put(root)
    while len(values) > 0:
      currNode = queue.get()
      left, right, *rest = values[:2]
      if left:
        left_node = TreeNode(left)
        queue.put(left_node)
        currNode.left = left_node
      if right:
        right_node = TreeNode(right)
        queue.put(right_node)
        currNode.right = right_node
      values = rest
    return root
