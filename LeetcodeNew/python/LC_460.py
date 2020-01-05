"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.



Follow up:
Could you do both operations in O(1) time complexity?



Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""

import collections

"""
What is my data structure?
1. A Doubly linked Node
class Node:
	+ key: int
	+ value: int
	+ freq: int
	+ prev: Node
	+ next: Node
2. A Doubly Linked List
Note: This part could be replaced by OrderedDict, I implemented it by hand for clarity

class DLinkedList:
	- sentinel: Node
	+ size: int
	+ append(node: Node) -> None
	+ pop(node: Node) -> Node
3. Our LFUCache
class LFUCache:
	- node: dict[key: int, node: Node]
	- freq: dict[freq: int, lst: DlinkedList]
	- minfreq: int
	+ get(key: int) -> int
	+ put(key: int, value: int) -> None

Explanation
Each key is mapping to the corresponding node (self.node), where we can retrieve the node in O(1) time.

Each frequency freq is mapped to a Doubly Linked List (self.freq), where all nodes in the DLinkedList have the same frequency, freq. Moreover, each node will be always inserted in the head (indicating most recently used).

A minimum frequency self.minfreq is maintained to keep track of the minimum frequency of across all nodes in this cache, such that the DLinkedList with the min frequency can always be retrieved in O(1) time.

Here is how the algorithm works
get(key)

query the node by calling self.node[key]
find the frequency by checking node.freq, assigned as f, and query the DLinkedList that this node is in, through calling self.freq[f]
pop this node
update node's frequence, append the node to the new DLinkedList with frequency f+1
if the DLinkedList is empty and self.minfreq == f, update self.minfreq to f+1.
return node.val
put(key, value)

If key is already in cache, do the same thing as get(key), and update node.val as value
Otherwise:
if the cache is full, pop the least frequenly used element (*)
add new node to self.node
add new node to self.freq[1]
reset self.minfreq to 1
(*) The least frequently used element is the tail element in the DLinkedList with frequency self.minfreq

Implementation
Below is the implementation with detailed comment as well.

"""



class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:
    """ An implementation of doubly linked list.

	Two APIs provided:

    append(node): append the node to the head of the linked list.
    pop(node=None): remove the referenced node.
                    If None is given, remove the one from tail, which is the least recently used.

    Both operation, apparently, are in O(1) complexity.
    """
    def __init__(self):
        self.dummy = Node(None, None) # dummy node
        self.dummy.next = self.dummy.prev = self.dummy
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, node):
        node.next = self.dummy.next
        node.prev = self.dummy
        node.next.prev = node
        self.dummy.next = node
        self.size += 1

    def pop(self, node=None):
        if self.size == 0:
            return

        if not node:
            node = self.dummy.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

        return node

class LFUCache:
    def __init__(self, capacity):
        """
        Three things to maintain:

        1. a dict, named as `self.node`, for the reference of all nodes given key.
           That is, O(1) time to retrieve node given a key.

        2. Each frequency has a doubly linked list, store in `self.freq`, where key
           is the frequency, and value is an object of `DLinkedList`

        3. The min frequency through all nodes. We can maintain this in O(1) time, taking
           advantage of the fact that the frequency can only increment by 1. Use the following
		   two rules:

           Rule 1: Whenever we see the size of the DLinkedList of current min frequency is 0,
                   the min frequency must increment by 1.

           Rule 2: Whenever put in a new (key, value), the min frequency must 1 (the new node)

        """
        self.size = 0
        self.capacity = capacity

        self.node = dict() # key: Node
        self.freq = collections.defaultdict(DLinkedList)
        self.minfreq = 0


    def _update(self, node):
        """
        This is a helper function that used in the following two cases:

            1. when `get(key)` is called; and
            2. when `put(key, value)` is called and the key exists.

        The common point of these two cases is that:

            1. no new node comes in, and
            2. the node is visited one more times -> node.freq changed ->
               thus the place of this node will change

        The logic of this function is:

            1. pop the node from the old DLinkedList (with freq `f`)
            2. append the node to new DLinkedList (with freq `f+1`)
            3. if old DlinkedList has size 0 and self.minfreq is `f`,
               update self.minfreq to `f+1`

        All of the above opeartions took O(1) time.
        """
        freq = node.freq

        self.freq[freq].pop(node)
        if self.minfreq == freq and not self.freq[freq]:
            self.minfreq += 1

        node.freq += 1
        freq = node.freq
        self.freq[freq].append(node)

    def get(self, key):
        """
        Through checking self.node[key], we can get the node in O(1) time.
        Just performs self._update, then we can return the value of node.

        """
        if key not in self.node:
            return -1

        node = self.node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        """
        If `key` already exists in self.node, we do the same operations as `get`, except
        updating the node.val to new value.

        Otherwise, the following logic will be performed

        1. if the cache reaches its capacity, pop the least frequently used item. (*)
        2. add new node to self.node
        3. add new node to the DLinkedList with frequency 1
        4. reset self.minfreq to 1

        (*) How to pop the least frequently used item? Two facts:

        1. we maintain the self.minfreq, the minimum possible frequency in cache.
        2. All cache with the same frequency are stored as a DLinkedList, with
           recently used order (Always append at head)

        Consequence? ==> The tail of the DLinkedList with self.minfreq is the least
                         recently used one, pop it...


        """
        if self.capacity == 0:
            return

        if key in self.node:
            node = self.node[key]
            self._update(node)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self.freq[self.minfreq].pop()
                del self.node[node.key]
                self.size -= 1

            node = Node(key, value)
            self.node[key] = node
            self.freq[1].append(node)
            self.minfreq = 1
            self.size += 1



class LFUCacheAgain:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity

        self.node = dict() # key: Node
        self.freq = collections.defaultdict(DLinkedList)
        self.minfreq = 0


    def _update(self, node):
        freq = node.freq

        self.freq[freq].pop(node)
        if self.minfreq == freq and not self.freq[freq]:
            self.minfreq += 1

        node.freq += 1
        freq = node.freq
        self.freq[freq].append(node)

    def get(self, key):
        if key not in self.node:
            return -1

        node = self.node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.node:
            node = self.node[key]
            self._update(node)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self.freq[self.minfreq].pop()
                del self.node[node.key]
                self.size -= 1

            node = Node(key, value)
            self.node[key] = node
            self.freq[1].append(node)
            self.minfreq = 1
            self.size += 1




class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.freq = count


class LFUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key = {}
        self.frequency = {}
        self.minVal = None

    def get(self, key):
        if not key in self.key:
            return -1
        node = self.key[key]
        del self.frequency[node.freq][key]
        if not self.frequency[node.freq]:
            del self.frequency[node.freq]
        node.freq += 1
        if not node.freq in self.frequency:
            self.frequency[node.freq] = collections.OrderedDict()

        self.frequency[node.freq][key] = node

        if not self.minVal in self.frequency:
            self.minVal += 1
        return node.val

    def put(self, key, value):
        # 如果存在该如何处理 更新value且计数+1
        if self.capacity == 0:
            return None
        if key in self.key:
            self.key[key].val = value
            self.get(key)
        else:
            if len(self.key) == self.capacity:
                item = self.frequency[self.minVal].popitem(last=False)
                del self.key[item[0]]
            node = Node(key, value, 1)
            self.key[key] = node
            if not 1 in self.frequency:
                self.frequency[1] = collections.OrderedDict()

            self.frequency[1][key] = node
            self.minVal = 1








