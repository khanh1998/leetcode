class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

class List:
    def __init__(self, values: []):
        self.head = None
        for value in reversed(values):
            newNode = ListNode(value, self.head)
            self.head = newNode
    def __str__(self):
        current = self.head
        strings = []
        while current is not None:
            strings.append(str(current.val))
            current = current.next
        return ', '.join(strings)

class Solution:
    def string(self, head):
        current = head
        strings = []
        while current is not None:
            strings.append(str(current.val))
            current = current.next
        return ', '.join(strings)
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if head and not head.next:
            return True
        # the case that the list has three or more items
        fast = head
        slow = head
        firstHalfTail = head
        nextSlow = head.next
        isOddLength = True
        # reverse first half of the list
        while fast is not None:
            if fast.next and not fast.next.next:
                isOddLength = False
                break
            if not fast.next:
                isOddLength = True
                break
            fast = fast.next.next
            slow = nextSlow
            nextSlow = slow.next
            # detach slow item
            firstHalfTail.next = nextSlow
            # point slow to head
            slow.next = head
            # update head
            head = slow
        # remove middle item of odd length list
        if isOddLength:
            head = head.next
        # checking
        slow = head
        while nextSlow is not None:
            if slow.val != nextSlow.val:
                return False
            slow = slow.next
            nextSlow = nextSlow.next
        return True

list = List([1,3,2,4,3,2,1])
print(list)
solution = Solution()
print(solution.isPalindrome(list.head))

