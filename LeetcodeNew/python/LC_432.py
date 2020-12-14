"""
https://leetcode.com/problems/all-oone-data-structure/discuss/91453/Python-solution-with-detailed-explanation
https://leetcode.com/problems/all-oone-data-structure/discuss/91428/Python-solution-with-detailed-comments
"""



class Node:
    def __init__(self):
        self.keys = set([])
        self.prev, self.nxt = None, None

    def add_key(self, key):
        self.keys.add(key)

    def remove_key(self, key):
        self.keys.remove(key)

    def get_any_key(self):
        if self.keys:
            result = self.keys.pop()
            self.add_key(result)
            return result
        else:
            return None

    def is_empty(self):
        return len(self.keys) == 0


class DoubleLinkedList:
    def __init__(self):
        self.head_node, self.tail_node = Node(), Node()
        self.head_node.nxt, self.tail_node.prev = self.tail_node, self.head_node

    def insert_after(self, x):
        node, temp = Node(), x.nxt
        x.nxt, node.prev = node, x
        node.nxt, temp.prev = temp, node
        return node

    def insert_before(self, x):
        return self.insert_after(x.prev)

    def insert_after_head(self):
        return self.insert_after(self.head_node)

    def remove(self, x):
        prev_node = x.prev
        prev_node.nxt, x.nxt.prev = x.nxt, prev_node

    def get_head(self):
        return self.head_node.nxt

    def get_tail(self):
        return self.tail_node.prev


class AllOne:
    def __init__(self):
        self.dll, self.key_counter = DoubleLinkedList(), defaultdict(int)
        self.node_freq = {}

    def _rmv_key_pf_node(self, pf, key):
        if pf in self.node_freq:
            node = self.node_freq[pf]
            node.remove_key(key)
            if node.is_empty():
                self.dll.remove(node)
                self.node_freq.pop(pf)

    def inc(self, key):
        self.key_counter[key] += 1
        cf, pf = self.key_counter[key], self.key_counter[key ] -1
        if cf not in self.node_freq:
            self.node_freq[cf] = self.dll.insert_after_head() if pf == 0 else self.dll.insert_after(self.node_freq[pf])
        self.node_freq[cf].add_key(key)
        if pf > 0:
            self._rmv_key_pf_node(pf, key)

    def dec(self, key):
        if key in self.key_counter:
            self.key_counter[key] -= 1
            cf, pf = self.key_counter[key], self.key_counter[key ] +1
            if self.key_counter[key] == 0:
                self.key_counter.pop(key)
            if cf not in self.node_freq and cf != 0:
                self.node_freq[cf] = self.dll.insert_before(self.node_freq[pf])
            if cf != 0:
                self.node_freq[cf].add_key(key)
            self._rmv_key_pf_node(pf, key)

    def getMaxKey(self):
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().get_any_key() else ""

    def getMinKey(self):
        return self.dll.get_head().get_any_key() if self.dll.get_tail().get_any_key() else ""




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
