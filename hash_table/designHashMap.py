class MyHashMap:
    def __init__(self, bucket_num=10):
        """
        Initialize your data structure here.
        """
        self.buckets = [None] * bucket_num
        self.bucket_num = bucket_num

    def hash(self, value: int) -> int:
        return value % self.bucket_num

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        if bucket is None:
            self.buckets[bucket_index] = [(key, value)]
        else:
            for curr_index, (curr_key, curr_value) in enumerate(bucket):
                if key == curr_key:
                    bucket[curr_index] = (key, value)
                    return
            bucket.append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        if bucket is not None:
            for (curr_key, curr_value) in bucket:
                if curr_key == key:
                    return curr_value
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        remove_index = None
        if bucket is not None:
            for index, (curr_key, _) in enumerate(bucket):
                if curr_key == key:
                    remove_index = index
                    break
            if remove_index is not None:
                self.buckets[bucket_index] = [
                    *bucket[:remove_index], *bucket[remove_index + 1:]]


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(3))
obj.put(2, 1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))
