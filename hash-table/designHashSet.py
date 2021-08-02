class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.data.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            index = self.data.index(key)
            if index > -1:
                self.data = [*self.data[:index], *self.data[index+1:]]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        for item in self.data:
            if item == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.data)
print(obj.contains(2))
obj.remove(2)
print(obj.data)
print(obj.contains(2))