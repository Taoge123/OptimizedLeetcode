"""
https://leetcode.com/problems/all-oone-data-structure/discuss/91453/Python-solution-with-detailed-explanation
https://leetcode.com/problems/all-oone-data-structure/discuss/914 28/Python-solution-with-detailed-comments
"""

class DLinkedList:
    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.prev = None
        self.next = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = None
        self.next = None

    def insert_after(self, node):
        nxt = self.next
        self.next = node
        node.prev = self
        node.next = nxt
        nxt.prev = node


class AllOne:
    def __init__(self):
        self.head = DLinkedList()  # sentinel
        self.tail = DLinkedList()  # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}  # key to LinkedList

    def inc(self, key):
        if key not in self.dic:  # find current block and remove key
            node = self.head
        else:
            node = self.dic[key]
            node.keys.remove(key)

        if node.val + 1 != node.next.val:  # insert new block
            new_node = DLinkedList(node.val + 1)
            node.insert_after(new_node)
        else:
            new_node = node.next

        new_node.keys.add(key)  # update new_node
        self.dic[key] = new_node  # ... and dic of key to new_node

        if not node.keys and node.val != 0:  # delete current node if not seninel
            node.remove()

    def dec(self, key):
        if not key in self.dic:
            return

        node = self.dic[key]
        del self.dic[key]  # could use self.dic.pop(key)
        node.keys.remove(key)

        if node.val != 1:
            if node.val - 1 != node.prev.val:  # insert new block
                new_node = DLinkedList(node.val - 1)
                node.prev.insert_after(new_node)
            else:
                new_node = node.prev
            new_node.keys.add(key)
            self.dic[key] = new_node

        if not node.keys:  # delete current block
            node.remove()

    def getMaxKey(self):
        if self.tail.prev.val == 0:
            return ""
        key = self.tail.prev.keys.pop()  # pop and add back to get arbitrary (but not random) element
        self.tail.prev.keys.add(key)
        return key

    def getMinKey(self):
        if self.head.next.val == 0:
            return ""
        key = self.head.next.keys.pop()
        self.head.next.keys.add(key)
        return key


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
