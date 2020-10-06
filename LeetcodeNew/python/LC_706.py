
class MyHashMap:
    def __init__(self):
        self.numBuckets = 1000
        self.buckets = [-1] * self.numBuckets

    def put(self, key: int, value: int) -> None:
        index = key % self.numBuckets
        if self.buckets[index] == -1:
            self.buckets[index] = []

        for i, kvPair in enumerate(self.buckets[index]):
            if kvPair[0] == key:
                self.buckets[index][i] = (key, value)
                return

        self.buckets[index].append((key, value))


    def get(self, key: int) -> int:
        index = key % self.numBuckets
        if self.buckets[index] == -1:
            return -1

        for kvPair in self.buckets[index]:
            if kvPair[0] == key:
                return kvPair[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.numBuckets
        indexToRemove = -1

        if self.buckets[index] == -1:
            return

        for i, kvPair in enumerate(self.buckets[index]):
            if kvPair[0] == key:
                indexToRemove = i
                break

        if indexToRemove == -1:
            return

        else:
            del self.buckets[index][indexToRemove]





class ListNode:
    def __init__(self, key):
        self.key = key
        self.val = None
        self.next = None

class MyHashMap2:
    SIZE = 1000

    def __init__(self):
        self.hashing = [ListNode(-1) for _ in range(self.SIZE)]

    def put(self, key: int, value: int) -> None:
        head = self.hashing[key % self.SIZE]
        current = head.next
        while current:
            if current.key == key: break
            current = current.next
        else:
            current = ListNode(key)
            current.next = head.next
            head.next = current
        current.val = value

    def get(self, key: int) -> int:
        current = self.hashing[key % self.SIZE].next
        while current:
            if current.key == key: break
            current = current.next
        else:
            return -1
        return current.val

    def remove(self, key: int) -> None:
        current = self.hashing[key % self.SIZE]
        while current and current.next:
            if current.next.key == key: break
            current = current.next
        else:
            return None
        current.next = current.next.next


