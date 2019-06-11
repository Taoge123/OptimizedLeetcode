
"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""

"""
I do not think array solutions are acceptable interviews. 
So here is my naive implementation of Hash with chaining. 
One can play with m (number of slots in HashTable) to optimize the runtime. 
I got 90% with setting m = 1000."""


# using just arrays, direct access table
# using linked list for chaining

class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000;
        self.h = [None] * self.m

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)  # update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.m
        cur = prev = self.h[index]
        if not cur: return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next


class MyHashMap2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [-1] * 1000001

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.table[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.table[key]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.table[key] = -1


class MyHashMap3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [[[], []] for i in range(self.size)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        bucket, idx = self._index(key)

        if idx == -1:
            bucket[0].append(key)
            bucket[1].append(value)
        else:
            bucket[0][idx] = key
            bucket[1][idx] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket, idx = self._index(key)
        if idx == -1: return -1
        return bucket[1][idx]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        bucket, idx = self._index(key)
        if idx == -1:
            pass
        else:
            bucket[0].pop(idx)
            bucket[1].pop(idx)

    def _hash(self, key):
        return key % self.size

    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for idx, k in enumerate(bucket[0]):
            if k == key:
                return bucket, idx
        return bucket, -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)




