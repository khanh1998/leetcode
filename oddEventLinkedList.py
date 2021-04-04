class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        self.val

class List:
    def __init__(self, values: [int]):
        self.head = None
        for value in reversed(values):
            newNode = ListNode(value, self.head)
            self.head = newNode
    def __str__(self):
        current = self.head
        values = []
        while current is not None:
            values.append(str(current.val))
            current = current.next
        return ', '.join(values)
            
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # if the list has one or two items
        # then no need to do anything
        if not head.next or not head.next.next:
            return head
        # if the list has at least three items
        oddTail = head
        evenHead = head.next
        currentOdd = None
        currentEven = head.next
        while currentEven is not None and currentEven.next is not None:
            currentOdd = currentEven.next
            # detach nextOdd
            currentEven.next = currentOdd.next
            # move currentEven forward
            currentEven = currentEven.next
            # point nextOdd to evenHead
            currentOdd.next = evenHead
            # poin oddTail to currentOdd
            oddTail.next = currentOdd
            # update oddTail
            oddTail = currentOdd
        return head

list = List([1,2,3,4,5,6,7,8])
print(list)
solution = Solution()
result = solution.oddEvenList(list.head)
list.head = result
print(list)
