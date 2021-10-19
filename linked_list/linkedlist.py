class Node:
    def __init__(self, val, next):
        self.val = val
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
        newNode = Node(val, self.head)
        self.length += 1
        self.head = newNode
        if self.length == 1:
            self.tail = newNode
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val, None)
        if self.tail != None:
            self.tail.next = newNode
        if self.tail == None:
            self.head = newNode
        self.length += 1
        self.tail = newNode
        
    def findAtIndex(self, index) -> Node:
        assert index >= 0 and index < self.length, "index is not valid"
        curIdx = 0
        curNode = self.head
        while curIdx < index:
            if curNode != None:
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
            newNode = Node(val, curNode)
            prevNode.next = newNode
            self.length += 1
                
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # assert self.length > 0, "empty linked list"
        if index == 0:
            self.head = self.head.next
        elif index > 0 and index < self.length:
            prevNode = self.findAtIndex(index - 1)
            curNode = prevNode.next
            nextNode = curNode.next
            if nextNode == None:
                self.tail = prevNode # delete last element
            prevNode.next = nextNode
            curNode.next = None
        else:
            return;
        self.length -= 1
    
    def str(self):
        string = ''
        curNode = self.head
        while curNode != None:
            string += f' {curNode.val} '
            curNode = curNode.next
        return string
    
    def __repr__(self):
        curNode = self.head
        values = []
        while curNode != None:
            values.append(str(curNode.val))
            curNode = curNode.next
        return ' -> '.join(values)

#Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# index = 0
# val = 3
# obj.addAtTail(1)
# obj.addAtTail(2)
# obj.addAtTail(3)
# obj.addAtTail(4)
# obj.addAtTail(5)
# obj.addAtIndex(0, 0)
# obj.addAtIndex(6, 6)
# obj.addAtIndex(3, 1)
# obj.deleteAtIndex(3)
# obj.deleteAtIndex(6)
# obj.deleteAtIndex(0)
# obj.deleteAtIndex(7)
# obj.addAtIndex(7, 9)
