
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def query(self, num):
        if not self.root:
            return -1
        node = self.root
        res = 0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            target = 1 - cur
            if target in node:
                node = node[target]
                res |= (1 << i)
            else:
                node = node[cur]
        return res


class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        trie = Trie()
        res = [-1] * len(queries)
        j = 0
        for i, (x, m) in queries:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            res[i] = trie.query(x)
        return res


