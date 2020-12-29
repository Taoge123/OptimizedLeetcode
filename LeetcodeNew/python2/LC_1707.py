"""

421. Maximum XOR of Two Numbers in an Array
1697. Checking Existence of Edge Length Limited Paths

"""


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
                # res = res * 2
            else:
                node = node[cur]
        return res


class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()
        for i, query in enumerate(queries):
            queries[i] = [i, query]

        queries = sorted(queries, key=lambda x: x[1][1])
        # print(queries)
        trie = Trie()
        res = [-1] * len(queries)
        j = 0
        for i, (x, m) in queries:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            res[i] = trie.query(x)
        return res



