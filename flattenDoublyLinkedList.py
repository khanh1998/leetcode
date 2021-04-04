class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def createList(self, values: list) -> 'Node':
        head = None
        for item in reversed(values):
            newNode = Node(item, None, head, None)
            if head != None:
                head.prev = newNode
            head = newNode
        return head

    def printList(self, head: 'Node') -> str:
        current = head
        values = []
        while current != None:
            values.append(str(current.val))
            current = current.next
        string = ', '.join(values)
        print(string)
        return string
            
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        flatten = []
        current = head
        while current != None and stack.count != 0:
            print('current value', current.val)
            flatten.append(current.val)
            if current == None and stack.count != 0:
                current = stack.pop()
                current = current.next
            else:
                if current.child == None:
                    current = current.next
                else:
                    stack.append(current)
                    current = current.child
        print('flatten: ', flatten)
        result_head = self.createList(flatten)
        return result_head

def split_list(values: list) -> list:
    values.append(None)
    ready_to_end_a_level = False
    start_index = 0
    lists = []
    for index, value in enumerate(values):
        if value != None and not ready_to_end_a_level:
            ready_to_end_a_level = True
        elif value == None and ready_to_end_a_level:
            lists.append(values[start_index:index])
            start_index = index + 1
            ready_to_end_a_level = False
    return lists

def createDoublyLinkedList(lists: list) -> Node:
    total_head = None
    last_head_index = None
    for a_list in reversed(lists):
        head = None
        for index, value in reversed(list(enumerate(a_list))):
            if value != None:
                child = None
                if index == last_head_index:
                    newNode.child = total_head
                newNode = Node(value, None, head, child)
                if head != None:
                    head.next = newNode
                head = newNode
            else:
                break

        last_head_index = index + 1
        total_head = head
    return total_head

def printDoublyLinkedList(head: 'Node'):
    next_child = None
    current = head
    values = []
    while True:
        if current != None and current.child:
            next_child = current.child
            # print('next child', next_child.val)
        if current == None and next_child == None:
            # print('final list', values)
            break
        if current == None and next_child != None:
            # print(values)
            current = next_child
            next_child = None
            values = []
        print('.................')
        print(current.val)
        print(current.next)
        print(current.prev)
        values.append(current.val) 
        current = current.next

def testData() -> 'Node':
    head = None
    node0, node1, node2, node3 = None, None, None, None
    node20, node21, node22 = None, None, None
    node20 = Node(20, node2, node21, None)
    node21 = Node(21, node20, node22, None)
    node22 = Node(22, node21, None, None)
    #
    node3 = Node(3, node2, None, None)
    node2 = Node(2, node1, node3, node20)
    node1 = Node(1, node0, node2, None)
    node0 = Node(0, None, node1, None)
    head = node0
    return head

input_values = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]
lists = split_list(input_values)
# head = createDoublyLinkedList(lists)
# printDoublyLinkedList(head)
solution = Solution()
data = testData()
printDoublyLinkedList(data)
# flatten = solution.flatten(head)
# solution.printList(flatten)
