class MyHashSet:

    def __init__(self, size: int = 5):
        """
        Initialize your data structure here.
        """
        self.max_buckets = size
        self.buckets = [None] * size
        self.bucket_size = 4

    def hash(self, value: int) -> int:
        return value % self.max_buckets

    def add(self, key: int) -> None:
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        if bucket is not None:
            if key not in bucket:
                bucket.append(key)
        else:
            self.buckets[bucket_index] = [key]

    def remove(self, key: int) -> None:
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        if bucket is not None and key in bucket:
            index = bucket.index(key)
            self.buckets[bucket_index] = [*bucket[:index], *bucket[index + 1:]]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        if bucket is not None and key in bucket:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.buckets)
print(obj.contains(2))
obj.remove(2)
print(obj.buckets)
print(obj.contains(2))