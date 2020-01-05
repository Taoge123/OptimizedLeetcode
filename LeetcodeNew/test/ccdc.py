class Node3:
    def __init__(self, k, v):
        self.prev = None
        self.next = None
        self.key = k
        self.val = v
        self.cnt = 1

class DoublyLinkedList:
    def __init__(self):
        self.head = Node3(0, 0) # head is a dummy head node
        self.tail = Node3(0, 0) # tail is a dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self, node):
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

class LFUCache(object):

    def __init__(self, capacity):
        self.keys = {}
        self.freq = collections.defaultdict(DoublyLinkedList)
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0

    def get(self, key):

        if key not in self.keys:
            return -1
        else:
            node = self.keys[key]
            prevCount = node.cnt
            node.cnt += 1
            self.freq[prevCount].removeNode(node)
            self.freq[node.cnt].add(node)
            if prevCount == self.minFreq and self.freq[prevCount].size == 0:
                self.minFreq += 1
            return node.val

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key not in self.keys:
            node = Node3(key, value)
            self.keys[key] = node
            if self.size != self.capacity:
                self.freq[1].add(node)
                self.size += 1
            else:
                prevTail = self.freq[self.minFreq].removeTail()
                self.keys.pop(prevTail.key)
                self.freq[1].add(node)
            self.minFreq = 1
        else:
            node = self.keys[key]
            node.val = value
            prevCount = node.cnt
            node.cnt += 1
            self.freq[prevCount].removeNode(node)
            self.freq[node.cnt].add(node)
            if prevCount == self.minFreq and self.freq[prevCount].size == 0:
                self.minFreq += 1
                
                
                
                
                
                