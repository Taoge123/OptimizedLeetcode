
import collections

class MyHashSet:
    def __init__(self):
        self.buckets = 1000
        self.itemsPerBuckets = 1001
        self.table = collections.defaultdict(list)

    def hashcode(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def add(self, key: int) -> None:
        hashKey = self.hashcode(key)
        if not self.table[hashKey]:
            self.table[hashKey] = [False] * self.itemsPerBuckets
        self.table[hashKey][self.pos(key)] = True

    def remove(self, key: int) -> None:
        hashKey = self.hashcode(key)
        if self.table[hashKey]:
            self.table[hashKey][self.pos(key)] = False

    def contains(self, key: int) -> bool:
        hashKey = self.hashcode(key)
        return self.table[hashKey] and self.table[hashKey][self.pos(key)]





