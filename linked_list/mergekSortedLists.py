from typing import List, Optional
from queue import PriorityQueue
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
            exceeded time limit
        '''
        head, tail = None, None
        currNodes = [l for l in lists]
        while True:
            noneCounter = 0
            minIndex = None
            for index, currNode in enumerate(currNodes):
                if currNode == None:
                    noneCounter += 1
                elif minIndex == None and currNode != None:
                    minIndex = index
                elif currNode.val < currNodes[minIndex].val:
                    minIndex = index
            if noneCounter == len(lists):
                break
            newNode = ListNode(val=currNodes[minIndex].val)
            if head == None and tail == None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
            currNodes[minIndex] = currNodes[minIndex].next
        return head
    
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
            using priority queue
        '''
        queue = PriorityQueue()
        for l in lists:
            currNode = l
            while currNode != None:
                queue.put(currNode.val)
        head = None
        tail = None
        while not queue.empty():
            val = queue.get()
            newNode = ListNode(val=val)
            if head == None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
        return head

    def mergeTwoLists1(self, listOne: Optional[ListNode], listTwo: Optional[ListNode]) -> Optional[ListNode]:
        first, second = listOne, listTwo
        head, tail = None, None
        while first != None or second != None:
            if first == None:
                tail.next = second
                break
            elif second == None:
                tail.next = first
                break
            else:
                if first.val > second.val:
                    if head == None and tail == None:
                        head = second
                        tail = second
                        second = second.next
                    else:
                        tail.next = second
                        tail = second
                        second = second.next
                else:# first.val <= second.val
                    if head == None and tail == None:
                        head = first
                        tail = first
                        first = first.next
                    else:
                        tail.next = first
                        tail = first
                        first = first.next
        return head      
    def mergeTwoLists(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
    
    def mergeKListsRecur(self, lists: List[Optional[ListNode]], start: int, end: int) -> Optional[ListNode]:
        diff = end - start
        if diff >= 2:
            middle = start + (diff // 2)
            left = self.mergeKListsRecur(lists, start, middle)
            right = self.mergeKListsRecur(lists, middle + 1, end)
            return self.mergeTwoLists(left, right)
        elif diff == 0:
            return lists[start]
        elif diff == 1:
            return self.mergeTwoLists(lists[start], lists[end])
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        end = len(lists) - 1
        return self.mergeKListsRecur(lists, 0, end)
