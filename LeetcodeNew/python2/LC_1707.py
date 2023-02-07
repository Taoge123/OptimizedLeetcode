"""

421. Maximum XOR of Two Numbers in an Array
1697. Checking Existence of Edge Length Limited Paths

"""


# class Trie2:
#     def __init__(self):
#         self.root = {}
#
#     def insert(self, num):
#         node = self.root
#         for i in range(31, -1, -1):
#             bit = (num >> i) & 1
#             if bit not in node:
#                 node[bit] = {}
#             node = node[bit]
#
#     def query(self, num):
#         if not self.root:
#             return -1
#         node = self.root
#         res = 0
#         for i in range(31, -1, -1):
#             cur = (num >> i) & 1
#             target = 1 - cur
#             if target in node:
#                 node = node[target]
#                 res |= (1 << i)
#                 # res = res * 2
#             else:
#                 node = node[cur]
#         return res


class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            if num & 1 << i:
                if not node.one:
                    node.one = TrieNode()
                node = node.one
            else:
                if not node.zero:
                    node.zero = TrieNode()
                node = node.zero

    def query(self, num):
        node = self.root
        maxi = 0
        for i in range(31, -1, -1):
            isNum = num & 1 << i
            if not node:
                return maxi if maxi else -1
            if node.one and not isNum:
                node = node.one
                maxi += 1 << i
            elif node.zero and isNum:
                node = node.zero
                maxi += 1 << i
            else:
                node = node.one or node.zero
        return maxi


class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()
        for i, query in enumerate(queries):
            queries[i] = [i, query]

        queries = sorted(queries, key=lambda x : x[1][1])
        trie = Trie()
        res = [-1] * len(queries)
        j = 0
        for i, (x, m) in queries:
            # for each query, add numbers that are smaller than x
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            # compute i, then move on to the next query x
            res[i] = trie.query(x)
        return res



