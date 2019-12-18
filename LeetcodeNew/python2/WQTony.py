
import collections

class Solution:
    def bioHazard(self, n, affected, poisonous):
        res = []
        graph = collections.defaultdict(set)
        for i, j in zip(poisonous, affected):
            graph[i].add(j)
            graph[j].add(i)

        self.dfs(n, 1, affected, poisonous, [], res, graph)
        print(res)
        return len(res)

    def dfs(self, n, pos,  affected, poisonous, path, res, graph):
        # print(path)

        if pos == n+1:
            res.append(path[:])
            return


        for i in range(pos, n+1):
            if i in poisonous and graph[i] in path:
                continue

            self.dfs(n, i + 1, affected, poisonous, path + [i], res, graph)

        return res

#
n = 4
affected = [1, 2]
poisonous = [3, 4]

a = Solution()
print(a.bioHazard(n, affected, poisonous))

# def f(n, affected, poisonous):
#     graph = {k: v for k, v in zip(poisonous, affected)}
#     res = []
#     for i in range(1, n + 1):
#         tmp = []
#         for j in range(i, n + 1):
#             if tmp and j in graph and tmp[0] <= graph[j] <= tmp[-1]:
#                 break
#             tmp.append(j)
#             res.append(tmp[:])
#
#     print(len(res))
#     return res

# print(len(f(8, [2,3,4,3], [8,5,6,4])))



