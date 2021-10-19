from typing import Optional
import sys
sys.path.append("..")
from linkedlist import MyLinkedList, Node as ListNode
from rotateList import printList

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        new_head = head
        curr_node = head.next
        head.next = None
        next_node = None
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = new_head
            new_head = curr_node
            curr_node = next_node
        return new_head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        dummy = ListNode(None, head)
        before_begin_group = dummy
        begin_group = head
        end_group = dummy
        after_end_group = head
        done = False
        while True:
            for _ in range(k):
                if end_group == None or after_end_group == None:
                    done = True
                    break
                end_group = end_group.next
                after_end_group = after_end_group.next
            if done:
                break
            print('-', before_begin_group, begin_group, end_group, after_end_group)
            before_begin_group.next = None
            end_group.next = None
            self.reverseLinkedList(begin_group)
            before_begin_group.next = end_group
            begin_group.next = after_end_group
            ###
            before_begin_group = begin_group
            begin_group = after_end_group
            ###
            end_group = before_begin_group
            print('+', before_begin_group, begin_group, end_group, after_end_group)
            printList(dummy)
        return dummy.next

s = Solution()
l = MyLinkedList()
l.addAtTail(1)
l.addAtTail(2)
l.addAtTail(3)
l.addAtTail(4)
l.addAtTail(5)
l.addAtTail(6)
l.addAtTail(7)
l.addAtTail(8)
print('hooooo')
print(l)
printList(s.reverseKGroup(l.head, 3))
