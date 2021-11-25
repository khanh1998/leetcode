class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ShorterSolution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1, ptr2 = l1, l2
        head, tail = None, None
        carry = 0
        # 5 4 3 2 1
        #           |
        # 9 8 7
        #       |
        # 4 3 1 3 1
        # \       /
        # val1 = 1, val2 = 0
        # sum = 1, carry = 0, digit=1
        while ptr1 != None or ptr2 != None or carry != 0:
            val1, val2 = 0, 0
            if ptr1 != None:
                val1 = ptr1.val
                ptr1 = ptr1.next
            if ptr2 != None:
                val2 = ptr2.val
                ptr2 = ptr2.next
            digitsSum = val1 + val2 + carry
            carry = digitsSum // 10
            digit = digitsSum % 10
            newNode = ListNode(val=digit)
            if head == None and tail == None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
        return head



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resultHead = None
        resultTail = None
        curL1, curL2 = l1, l2
        length1, length2 = 0, 0
        # calculate length of the lists
        while curL2 != None or curL1 != None:
            if curL2:
                curL2 = curL2.next
                length2 += 1
            if curL1:
                curL1 = curL1.next
                length1 += 1
        # length difference
        print('length1', length1)
        print('length2', length2)
        diff = abs(length1 - length2)
        # calculate the sum
        curL1, curL2 = l1, l2
        carry = 0
        while curL1 != None or curL2 != None:
            # get operands
            if length1 > length2 and diff > 0 and curL2 == None:
                val2 = 0
                val1 = curL1.val
                diff -= 1
                curL1 = curL1.next
            elif length2 > length1 and diff > 0 and curL1 == None:
                val2 = curL2.val
                val1 = 0
                diff -= 1
                curL2 = curL2.next
            else:
                val1, val2 = curL1.val, curL2.val
                curL1 = curL1.next
                curL2 = curL2.next
            # sum
            sum = val1 + val2 + carry
            actualValue = sum % 10 
            carry = sum // 10
            newNode = ListNode(actualValue, None)
            if resultHead == None:
                resultHead = newNode
            if resultTail != None:
                resultTail.next = newNode
            resultTail = newNode
        if carry != 0:
            newNode = ListNode(carry, None)
            resultTail.next = newNode
            resultTail = newNode
        return resultHead

def createList(values: []) -> ListNode:
    head = None
    for value in reversed(values):
        newNode = ListNode(value, head)
        head = newNode
    return head

def printList(head: ListNode):
    values = []
    current = head
    while current != None:
        values.append(str(current.val))
        current = current.next
    string = ', '.join(values)
    print(string)

head1 = createList([9])
printList(head1)
head2 = createList([9])
printList(head2)
solution = Solution()
printList(solution.addTwoNumbers(head1, head2))
