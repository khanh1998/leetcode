class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(values: None) -> ListNode:
    head = None
    for value in reversed(values):
        newNode = ListNode(value, head)
        head = newNode
    return head
    
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        l1 = list1
        l2 = list2
        # check if the lists are empty
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return None
        # initialize
        headMerge = None
        tailMerge = None
        if l1.val >= l2.val:
            headMerge = l2
            tailMerge = l2
            l2 = l2.next
            tailMerge.next = None
        else:
            headMerge = l1
            tailMerge = l1
            l1 = l1.next
            tailMerge.next = None

        while l1 != None or l2 != None:
            if l1 == None:
                tailMerge.next = l2
                break
            elif l2 == None:
                tailMerge.next = l1
                break
            if l1.val >= l2.val:
                tailMerge.next = l2
                l2 = l2.next
                tailMerge = tailMerge.next
                tailMerge.next = None
            else:
                tailMerge.next = l1
                l1 = l1.next
                tailMerge = tailMerge.next
                tailMerge.next = None
        return headMerge

def printList(head: ListNode):
    current = head
    values = []
    while current != None:
        values.append(str(current.val))
        current = current.next
    string = ', '.join(values)
    print(string)
    
list1 = createList([1,2,4,5])
list2 = createList([0,3,6])
printList(list1)
printList(list2)
solution = Solution()
result = solution.mergeTwoLists(list1, list2)
print(type(result))
printList(result)
