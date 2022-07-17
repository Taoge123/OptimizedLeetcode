"""
https://leetcode.com/problems/all-oone-data-structure/discuss/91453/Python-solution-with-detailed-explanation
https://leetcode.com/problems/all-oone-data-structure/discuss/91428/Python-solution-with-detailed-comments
"""

import collections


class Node:
    def __init__(self):
        self.keys = set()
        self.prev = None
        self.next = None

    def add_key(self, key):
        self.keys.add(key)

    def remove_key(self, key):
        self.keys.remove(key)

    def get_any_key(self):
        if self.keys:
            node = self.keys.pop()
            self.add_key(node)
            return node
        else:
            return None

    def is_empty(self):
        return len(self.keys) == 0


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def insert_after(self, x):
        node, nxt = Node(), x.next
        x.next, node.prev = node, x
        node.next, nxt.prev = nxt, node
        return node

    def insert_before(self, x):
        return self.insert_after(x.prev)

    def insert_after_head(self):
        return self.insert_after(self.head)

    def remove(self, x):
        prev_node = x.prev
        prev_node.next, x.next.prev = x.next, prev_node

    def get_head(self):
        return self.head.next

    def get_tail(self):
        return self.tail.prev


class AllOne:
    def __init__(self):
        self.dll = DoubleLinkedList()
        self.count = collections.defaultdict(int)
        self.freq = {}

    def _remove_node(self, freq, key):
        if freq in self.freq:
            node = self.freq[freq]
            node.remove_key(key)
            if node.is_empty():
                self.dll.remove(node)
                self.freq.pop(freq)

    def inc(self, key):
        self.count[key] += 1
        cf = self.count[key]
        pf = self.count[key] - 1
        if cf not in self.freq:
            if pf == 0:
                self.freq[cf] = self.dll.insert_after_head()
            else:
                self.freq[cf] = self.dll.insert_after(self.freq[pf])
        self.freq[cf].add_key(key)
        if pf > 0:
            self._remove_node(pf, key)

    def dec(self, key):
        if key in self.count:
            self.count[key] -= 1
            cf = self.count[key]
            pf = self.count[key] + 1
            if self.count[key] == 0:
                self.count.pop(key)
            if cf not in self.freq and cf != 0:
                self.freq[cf] = self.dll.insert_before(self.freq[pf])
            if cf != 0:
                self.freq[cf].add_key(key)
            self._remove_node(pf, key)

    def getMaxKey(self):
        if self.dll.get_tail().get_any_key():
            return self.dll.get_tail().get_any_key()
        else:
            return ""

    def getMinKey(self):
        if self.dll.get_head().get_any_key():
            return self.dll.get_head().get_any_key()
        else:
            return ""


class AllOne2:
    def __init__(self):
        self.queue = []
        self.table = {}

    def inc(self, key: str) -> None:
        if key not in self.table:
            self.table[key] = 1
            ele = (self.table[key], key)
            self.queue.append(ele)
            heapq.heapify(self.queue)
        else:
            self.queue.remove((self.table[key], key))
            self.table[key] += 1
            self.queue.append((self.table[key], key))
            heapq.heapify(self.queue)

    def dec(self, key: str) -> None:
        if self.table.get(key, 0) == 1:
            del self.table[key]
            self.queue.remove((1, key))
            heapq.heapify(self.queue)
        elif self.table.get(key, 0) != 0:
            self.queue.remove((self.table[key], key))
            self.table[key] -= 1
            self.queue.append((self.table[key], key))
            heapq.heapify(self.queue)

    def getMaxKey(self) -> str:
        ans = heapq.nlargest(1, self.queue)
        return ans[0][1] if ans else ''

    def getMinKey(self) -> str:
        ans = heapq.nsmallest(1, self.queue)
        return ans[0][1] if ans else ''
