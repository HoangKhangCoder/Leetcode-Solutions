from collections import OrderedDict

class LRUCache:
    # Idea: use an OrderedDict to store key-value pairs while also
    # maintaining usage order (least-recently-used at the front,
    # most-recently-used at the back). Every time a key is accessed via
    # get/put, move it to the back (move_to_end) to mark it as most
    # recently used. When capacity is exceeded, remove the item at the
    # front (the least recently used one).

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # mark this key as just accessed
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # mark this key as just accessed
        self.cache[key] = value

        # If we've exceeded capacity, evict the least recently used item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)