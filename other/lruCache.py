class Node:
	def __init__(self, val: int, key: int, prev: 'Node', next: 'Node') -> None:
		self.prev = prev
		self.val = val
		self.key = key
		self.next = next
	def __str__(self) -> str:
		return str(self.val)
	def __repr__(self) -> str:
		return str(self.val)

class DoubleLinkedList:
	def __init__(self, size: int) -> None:
		self.size = size
		self.head = None
		self.tail = None
		self.length = 0		
	def add(self, val: int, key: int) -> tuple:
		if self.length == 0:
			newNode = Node(val, prev=self.tail, key=key, next=None)
			self.head = newNode
			self.tail = newNode
			self.length += 1
			return (newNode, None)
		else:
			newNode = Node(val, prev=None, key=key, next=self.head)
			self.head.prev = newNode
			self.head = newNode
			removed_key = None
			if self.length == self.size:
				removed = self.tail
				self.tail = self.tail.prev
				removed.prev = None
				self.tail.next = None
				removed_key = removed.key
			else:
				self.length += 1
			return (newNode, removed_key)

	def move_up(self, node: 'Node'):
		if node != self.head:
			# remove current node
			left = node.prev
			right = node.next
			left.next = right
			if right != None:
				right.prev = left
			# set tail to new position
			if node == self.tail:
				self.tail = left

			# put the current node on the top
			node.prev = None
			node.next = self.head
			self.head.prev = node
			self.head = node
		return (None, None)

	def __str__(self) -> str:
		values = []
		curr = self.head
		while curr != None:
			values.append(str(curr.val))
			curr = curr.next
		return f'tail:{self.tail.val},head:{self.head.val}, : ' + ','.join(values)

class LRUCache:
	def __init__(self, capacity: int):
		self.values = DoubleLinkedList(capacity)
		self.keyToRef = {}

	def get(self, key: int) -> int:
		if key in self.keyToRef:
			node = self.keyToRef[key]
			val = node.val
			left_key, right_key = self.values.move_up(node)
			# swap references of two keys in map
			if left_key != None and right_key != None:
				left_ref = self.keyToRef[left_key]
				right_ref = self.keyToRef[right_key]
				del self.keyToRef[right_key]
				del self.keyToRef[left_key]
				self.keyToRef[right_key] = left_ref
				self.keyToRef[left_key] = right_ref
			return val
		else:
			return -1

	def put(self, key: int, value: int) -> None:
		if key in self.keyToRef:
			self.get(key)
			ref = self.keyToRef[key]
			ref.val = value
			return
		node, old_key = self.values.add(value, key)
		if old_key != None:
			del self.keyToRef[old_key]
		self.keyToRef[key] = node


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2,1)
print(obj.values, obj.keyToRef)
obj.put(1,1)
print(obj.values, obj.keyToRef)
obj.put(2,3)
print(obj.values, obj.keyToRef)
obj.put(4,1)
print(obj.values, obj.keyToRef)
print(obj.get(1) == -1)
print(obj.get(2) == 3)