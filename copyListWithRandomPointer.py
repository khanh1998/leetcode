# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyListAndMakeMap(self, head: 'Node') -> 'Node':
        map = {}        
        copy_head = None
        copy_tail = None
        current = head
        while current != None:
            val, next, random = current.val, current.next, current.random
            newNode = Node(val, next, random)
            map[current] = newNode
            if copy_head == None and copy_tail == None:
                copy_head = newNode
                copy_tail = newNode
            else:
                copy_tail.next = newNode
                copy_tail = newNode
            current = current.next
        return copy_head, map

    def copyRandomList(self, head: 'Node') -> 'Node':
        copy_head, map = self.copyListAndMakeMap(head)
        current_old = head
        current_new = copy_head
        while current_old != None:
            random_old = current_old.random
            random_new = map.get(random_old)
            current_new.random = random_new

            current_new = current_new.next
            current_old = current_old.next
        return copy_head


    def createList(self, numbers: list) -> Node:
        head = None
        for num in reversed(numbers):
            newNode = Node(num, head)
            head = newNode
        return head

    def printList(self, head: Node):
        current = head
        values = []
        while current != None:
            values.append(str(current.val))
            current = current.next
        print(','.join(values))

solution = Solution()
l = solution.createList([1,2,3,4,5,6,7,8,9])
c = solution.copyRandomList(l)
solution.printList(l)
solution.printList(c)
