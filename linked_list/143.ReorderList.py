from typing import List, Optional, Tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        firstHead, firstTail, secondHead = split(head)
        secondHead = reverse(secondHead)
        firstCurr = firstHead
        while firstCurr is not None and firstCurr.next is not None:
            # take the node
            node = secondHead
            secondHead = secondHead.next
            node.next = None
            # put the node in the first half
            next = firstCurr.next
            firstCurr.next = node
            node.next = next
            firstCurr = next
        # concat spare nodes in second half to first half
        firstTail.next = secondHead

def split(head: Optional[ListNode]) -> Tuple[ListNode, ListNode, ListNode]:
    fast, slow, prev = head, head, None
    while fast is not None:
        prev = slow
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next
    prev.next = None
    firstHead, secondHead = head, slow
    firstTail = prev
    return firstHead, firstTail, secondHead

def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    curr, next = head.next, None
    head.next = None
    while curr is not None:
        next = curr.next
        curr.next = head
        head = curr
        curr = next
    return head
        
def makeLinkedList(values: List[int]) -> ListNode:
    if len(values) == 0:
        return None
    head = ListNode(val=values[0])
    tail = head
    for num in values[1:]:
        node = ListNode(val=num) 
        tail.next = node
        tail = node
    return head

def toArray(node: ListNode) -> List[int]:
    result = []
    curr = node
    while curr is not None: 
        result.append(curr.val)
        curr = curr.next
    return result

s = Solution()

arr=[1,2,3,4]
def test(arrs: List[List[int]]):
    for arr in arrs:
        l = makeLinkedList(arr)
        s.reorderList(l)
        print(toArray(l))

arrs = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6]]
test(arrs)