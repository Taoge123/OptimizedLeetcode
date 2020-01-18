from typing import  List
import collections
import bisect

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.leads = []
        self.times = times
        counter = collections.Counter()
        lead = -1

        for p in persons:
            counter[p] += 1
            if counter[p] >= counter[lead]:
                lead = p
            self.leads.append(lead)

    def q(self, t: int) -> int:
        return self.leads[bisect.bisect(self.times, t) - 1]

# realtime


class Node:
    def __init__(self):
        self.prev = self.next = None
        self.keys = set()
        self.issentinel = False

    def add_key(self, key):
        self.keys.add(key)

    def remove_key(self, key):
        if key in self.keys:
            self.keys.remove(key)

    def isempty(self):
        return len(self.keys) == 0 and not self.issentinel

    def get_one_key(self):
        if len(self.keys) == 0:
            return ''
        k = self.keys.pop()
        self.keys.add(k)
        return k


class DLinkedList:
    def __init__(self):
        self.sentinel = Node()
        self.sentinel.prev = self.sentinel.next = self.sentinel
        self.sentinel.issentinel = True

    def insert_after(self, node, key):
        new_node = Node()
        new_node.keys.add(key)

        new_node.next = node.next
        node.next.prev = new_node
        new_node.prev = node
        node.next = new_node

    def insert_before(self, node, key):
        new_node = Node()
        new_node.keys.add(key)

        new_node.prev = node.prev
        node.prev.next = new_node
        new_node.next = node
        node.prev = new_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = collections.Counter()
        self.list = DLinkedList()
        self.freq = {0: self.list.sentinel}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        prev_node = self.freq[self.count[key]]
        prev_node.remove_key(key)

        self.count[key] += 1
        freq = self.count[key]
        if freq not in self.freq:
            self.list.insert_after(prev_node, key)
            self.freq[freq] = prev_node.next
        else:
            self.freq[freq].add_key(key)

        if prev_node.isempty():
            del self.freq[freq - 1]
            self.list.remove(prev_node)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        next_node = self.freq[self.count[key]]
        next_node.remove_key(key)

        self.count[key] -= 1
        freq = self.count[key]
        if freq > 0:
            if freq not in self.freq:
                self.list.insert_before(next_node, key)
                self.freq[freq] = next_node.prev
            else:
                self.freq[freq].add_key(key)

        if next_node.isempty():
            del self.freq[freq + 1]
            self.list.remove(next_node)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return self.list.sentinel.prev.get_one_key()

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return self.list.sentinel.next.get_one_key()


        # Your AllOne object will be instantiated and called as such:
        # obj = AllOne()
        # obj.inc(key)
        # obj.dec(key)
        # param_3 = obj.getMaxKey()
        # param_4 = obj.getMinKey()