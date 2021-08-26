from queue import Queue
from typing import List

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Codec:

  def serialize(self, root: TreeNode) -> List[int]:
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

  def deserialize(self, data: List[int]) -> TreeNode:
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
      if len(values) > 1:
        left, right, *rest = values
      else:
        left, *rest = values
      
      if left != None:
        left_node = TreeNode(left)
        queue.put(left_node)
        currNode.left = left_node
      if right != None:
        right_node = TreeNode(right)
        queue.put(right_node)
        currNode.right = right_node
      values = rest
    return root
