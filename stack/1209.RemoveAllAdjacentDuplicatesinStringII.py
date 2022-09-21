EMPTY = ""

class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.length = 0
    
    def string(self) -> str:
        string = ''
        for _, char in self.stack:
            string += char
        return string

    def top(self)-> tuple:
        if self.length == 0:
            return (0, EMPTY)
        return self.stack[-1]

    def push(self, val: tuple):
        self.stack.append(val)
        self.length += 1

    def pop(self) -> tuple:
        if self.length == 0:
            return (-1, EMPTY)
        last = self.stack[-1]
        del self.stack[-1]
        self.length -= 1
        return last



class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = Stack()
        for char in s:
            topCount, topChar = stack.top()
            if char == topChar:
                stack.push((topCount + 1, char))
            else:
                stack.push((1, char))

            topCount, topChar = stack.top()
            if topCount == k:
                for _ in range(k):
                    stack.pop()
        return stack.string()


s = Solution()
print(s.removeDuplicates('abcd', 2) == 'abcd')
print(s.removeDuplicates('deeedbbcccbdaa', 3) == 'aa')
print(s.removeDuplicates('pbbcggttciiippooaais', 2) == 'ps')