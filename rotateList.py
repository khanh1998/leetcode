# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

class Solution:
    def getLength(self, head: ListNode) -> int:
        length = 0
        cur = head
        while cur != None:
            cur = cur.next
            length += 1
        return length

    def getCutOffPart(self, head: ListNode, length: int) -> ListNode:
        behind, front = head, head
        behindBehind = None # this node is aimed hold the connection to the behind node
        last = None # the last node of the list
        for index in range(length):
            front = front.next
        while front != None:
            last = front
            front = front.next
            behindBehind = behind
            behind = behind.next
        return behindBehind, behind, last

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = self.getLength(head)
        if k == 0 or length <= 1:
            return head
        newLength = k % length
        if newLength == 0:
            return head
        # get all references needed for the cut off part
        behindBehind, behind, last = self.getCutOffPart(head, newLength)
        # break the connection from the rest of list to the cut off part
        behindBehind.next = None
        # move the cut off part to the top of the list
        last.next = head
        head = behind
        return behind

def createList(values: [int]) -> ListNode:
    head = ListNode(values[-1], None)
    for value in reversed(values[:-1]):
        newNode = ListNode(value, head)
        head = newNode
    return head

def printList(head: ListNode) -> str:
    cur = head
    values = []
    while cur != None:
        values.append(str(cur.val))
        cur = cur.next
    string = ', '.join(values)
    print(string)
    return string
myList = createList([1,2,3,4,5])
printList(myList)
solution = Solution()
rotated = solution.rotateRight(myList, 2)
printList(rotated)
