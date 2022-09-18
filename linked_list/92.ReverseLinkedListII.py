from distutils.command.build import build
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
                  2         4
                  |         |
        1 -> 2 -> 3    4    5    6    7
                                      c    n

        Dummy -> 1 -> 2 -> 5 -> 4 -> 3 -> 6 -> 7
        h
                                               t
                                               s

        '''
        curr, count = head, 1
        dummy = ListNode()
        newHead, newTail, newStatic = dummy, dummy, dummy
        while curr != None:
            next = curr.next
            curr.next = None
            if count < left or count > right:
                newTail.next = curr
                newTail = curr
                newStatic = curr
            if count >= left and count <= right:
                curr.next = newStatic.next
                newStatic.next = curr
                while newTail.next != None:
                    newTail = newTail.next
            curr = next
            count += 1
        return newHead.next

def buildLinkedList(data: List[int]) -> ListNode:
    dummy = ListNode()
    head, tail = dummy, dummy
    for num in data:
        newNode = ListNode(val=num)
        tail.next = newNode
        tail = newNode
    return head.next

def toString(head: ListNode) -> str:
    curr = head.next
    s = f'{head.val}'
    while curr != None:
        s = f'{s}, {curr.val}' 
        curr = curr.next
    return s

s = Solution()

data = buildLinkedList([1,2,3,4,5])
res = s.reverseBetween(data, 2, 4)
print(toString(res) == '1, 4, 3, 2, 5')

data = buildLinkedList([1,2,3,4,5])
res = s.reverseBetween(data, 1, 5)
print(toString(res) == '5, 4, 3, 2, 1')

data = buildLinkedList([1,2,3,4,5])
res = s.reverseBetween(data, 1, 1)
print(toString(res) == '1, 2, 3, 4, 5')

data = buildLinkedList([1,2,3,4,5])
res = s.reverseBetween(data, 5, 5)
print(toString(res) == '1, 2, 3, 4, 5')

data = buildLinkedList([5])
res = s.reverseBetween(data, 1, 1)
print(toString(res) == '5')