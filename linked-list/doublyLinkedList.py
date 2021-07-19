class Node:
    def __init__(self, val, next, prev):
        self.val = val
        self.prev = prev
        self.next = next
    def __repr__(self):
        return self.val
    def __str__(self):
        return f'{self.val}'

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.val))
            current = current.next
        return ', '.join(values)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        node = self.findAtIndex(index)
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the              first node of the linked list.
        """
        
        newNode = Node(val, self.head, None)
        if self.head is not None:
            self.head.prev = newNode
        self.length += 1
        self.head = newNode
        if self.length == 1:
            self.tail = newNode
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val, None, self.tail)
        if self.tail != None:
            self.tail.next = newNode
        if self.tail == None:
            self.head = newNode
        self.length += 1
        self.tail = newNode
        
    def findAtIndex(self, inputIndex) -> Node:
        assert inputIndex >= 0 and inputIndex < self.length, "index is not valid"
        curIdx = 0
        index = None
        curNode = None
        fromTail = False
        if inputIndex // self.length  >= 0.5:
            fromTail = True
            curNode = self.tail
            index = self.length - inputIndex - 1
        else:
            curNode = self.head
            index = inputIndex
        while curIdx < index:
            if curNode != None:
                if fromTail:
                    curNode = curNode.prev
                else:
                    curNode = curNode.next
                curIdx += 1
            else:
                raise Exception('something went wrong!!!')
                
        return curNode

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list,              the node will be appended to the end of linked list. If index is greater than the length, the node will not be          inserted.
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index > 0 and index < self.length:
            prevNode = self.findAtIndex(index - 1)
            curNode = prevNode.next
            newNode = Node(val, curNode, prevNode)
            prevNode.next = newNode
            curNode.prev = newNode
            self.length += 1
                
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # assert self.length > 0, "empty linked list"
        if index == 0:
            self.head = self.head.next
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        elif index > 0 and index < self.length:
            prevNode = self.findAtIndex(index - 1)
            curNode = prevNode.next
            nextNode = curNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            # remove reference of deleted node
            curNode.next = None
            curNode.prev = None
        else:
            return;
        self.length -= 1

list = MyLinkedList()
list.addAtHead(1)
print(list)
list.deleteAtIndex(0)
print(list)
