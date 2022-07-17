"""

https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list

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
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.dummy = Node(None, None) # dummy node
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
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
        self.size = 0
        self.capacity = capacity

        self.dic = dict() # key: Node
        self.freq = collections.defaultdict(DLinkedList)
        self.minfreq = 0


    def update(self, node):
        freq = node.freq

        self.freq[freq].pop(node)
        if self.minfreq == freq and not self.freq[freq]:
            self.minfreq += 1

        node.freq += 1
        freq = node.freq
        self.freq[freq].append(node)

    def get(self, key):
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.update(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.dic:
            node = self.dic[key]
            self.update(node)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self.freq[self.minfreq].pop()
                del self.dic[node.key]
                self.size -= 1

            node = Node(key, value)
            self.dic[key] = node
            self.freq[1].append(node)
            self.minfreq = 1
            self.size += 1



class LFUCache2:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.minfreq=None
        self.freq={}
        self.keys=collections.defaultdict(collections.OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.freq:
            return -1
        freq=self.freq[key]
        val=self.keys[freq][key]
        del self.keys[freq][key]
        if not self.keys[freq]:
            if freq==self.minfreq:
                self.minfreq+=1
            del self.keys[freq]
        self.freq[key]=freq+1
        self.keys[freq+1][key]=val
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity<=0:
            return
        if key in self.freq:
            freq=self.freq[key]
            self.keys[freq][key]=value
            self.get(key)
            return
        if self.capacity==len(self.freq):
            delkey,delval=self.keys[self.minfreq].popitem(last=False)
            del self.freq[delkey]
        self.freq[key]=1
        self.keys[1][key]=value
        self.minfreq=1




class Node3:
    def __init__(self, k, v):
        self.prev = None
        self.next = None
        self.key = k
        self.val = v
        self.cnt = 1


class DoublyLinkedList:
    def __init__(self):
        self.head = Node3(0, 0)  # head is a dummy head node
        self.tail = Node3(0, 0)  # tail is a dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addToHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def removeTail(self):
        prevTail = self.tail.prev
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        self.size -= 1
        return prevTail

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1


class LFUCache3:
    def __init__(self, capacity):
        self.freqTable = collections.defaultdict(DoublyLinkedList)
        self.keyTable = {}
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0

    def get(self, key):
        if key not in self.keyTable:
            return -1
        else:
            node = self.keyTable[key]
            prevCount = node.cnt
            node.cnt += 1
            self.freqTable[prevCount].removeNode(node)
            self.freqTable[node.cnt].addToHead(node)
            if prevCount == self.minFreq and self.freqTable[prevCount].size == 0:
                self.minFreq += 1
            return node.val

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key not in self.keyTable:
            node = Node3(key, value)
            self.keyTable[key] = node
            if self.size != self.capacity:
                self.freqTable[1].addToHead(node)
                self.size += 1
            else:
                prevTail = self.freqTable[self.minFreq].removeTail()
                self.keyTable.pop(prevTail.key)
                self.freqTable[1].addToHead(node)
            self.minFreq = 1
        else:
            node = self.keyTable[key]
            node.val = value
            prevCount = node.cnt
            node.cnt += 1
            self.freqTable[prevCount].removeNode(node)
            self.freqTable[node.cnt].addToHead(node)
            if prevCount == self.minFreq and self.freqTable[prevCount].size == 0:
                self.minFreq += 1




cache = LFUCache3(2)
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))       # returns 1
print(cache.put(3, 3))    # evicts key 2
print(cache.get(2))       # returns -1 (not found)
print(cache.get(3))       # returns 3.
print(cache.put(4, 4))    # evicts key 1.
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4


