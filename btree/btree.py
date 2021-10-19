from typing import List

class NodeItem:
	'''
	A class used to represent a item in a Node in a B Tree
	...
	Attributes
	-----------
	key: int
		key of the reference
	ref: object
		reference to actual data
	'''
	key = None
	ref = None
	def __init__(self, key: int, ref: object) -> None:
		self.key = key
		self.ref = ref
			
class Node:
	'''
	A class used to represent a node in a B Tree
	...
	Attributes
	-----------
	capacity: int
		the maximum item each node can contain
	items: List[NodeItem]
		a list of pair key and ref called item
		the number of items <= capacity
	'''
	capacity = 0
	items = List[NodeItem]
	children = []
	max_item_idx = None
	min_item_idx = None
	max_key = float("inf")
	min_key = float("-inf")
	def __init__(self, capacity: int) -> None:
		'''
		Parameters
		----------
		capacity : int
			the maximum item each node can contain
		'''
		self.capacity = capacity	
	def add_item(self, key: int, ref: object) -> NodeItem:
		new_item = NodeItem(key, ref)
		if len(self.children) == self.capacity:
			return None
		if len(self.children) == 0:
			self.items.append(new_item)
			self.max_item_idx = 0
			self.min_item_idx = 0
			self.max_key = key
			self.min_key = key
		elif len(self.children) > 0 and len(self.children) < self.capacity:
			if key < self.min_key:
				self.items.insert(0, new_item)
				self.min_key = key
			elif key > self.max_key:
				self.items.append(new_item)
				self.max_key = key
			else:
				index = 1
				for index, item in enumerate(self.items[:-1]):
					next_item = self.items[index + 1]
					if item.key < key and key < next_item.key:
						self.items.insert(index, new_item)
			self.max_item_idx += 1
		return new_item

class BTree:
	'''
	A class used to represent a B Tree
	https://en.wikipedia.org/wiki/B-tree
	...
	Attributes
	-----------
	capacity: int
		the maximum item each node can contain
		each node can have capacity + 1 children
	root: Node
		the root node of the tree
	'''
	capacity = 0
	root = None
	def __init__(self, capacity: int) -> None:
		self.capacity = capacity
		self.root = Node(capacity)
	
	def add(self, key: int, ref: object) -> Node:
