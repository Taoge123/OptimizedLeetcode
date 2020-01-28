import collections

import collections


class SolutionTLE:
    def accountsMerge(self, accounts):
        n = len(accounts)
        self.parent = [x for x in range(n)]
        table = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            table[account[0]].append(i)
        for i in range(n):
            for j in table[accounts[i][0]]:
                if (not self.same(i, j)) and (set(accounts[i][1:]) & set(accounts[j][1:])):
                    self.union(i, j)
        temp = [set() for _ in range(n)]
        for i in range(n):
            self.parent[i] = self.find(i)
            temp[self.parent[i]] |= set(accounts[i][1:])
        res = []
        for i in range(n):
            if self.parent[i] == i:
                node = list()
                node.append(accounts[i][0])
                node.extend(sorted(temp[i]))
                res.append(node)
        return res

    def find(self, x):
        if x == self.parent[x]:
            return self.parent[x]
        parent = self.find(self.parent[x])
        self.parent[x] = parent
        return parent

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.parent[x] = y

    def same(self, x, y):
        return self.find(x) == self.find(y)


class UnionFind:
    def __init__(self):
        self.parent = [i for i in range(10001)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def accountsMerge(self, accounts):
        uf = UnionFind()
        nameTable = {}
        indexTable = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            emails = acc[1:]
            for email in emails:
                nameTable[email] = name
                if email not in indexTable:
                    indexTable[email] = i
                    i += 1
                uf.union(indexTable[acc[1]], indexTable[email])

        res = collections.defaultdict(list)
        for email in nameTable:
            res[uf.find(indexTable[email])].append(email)

        return [[nameTable[v[0]]] + sorted(v) for v in res.values()]




accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],
           ["Mary", "mary@mail.com"],["John","johnnybravo@mail.com"]]
a = Solution()
print(a.accountsMerge(accounts))

