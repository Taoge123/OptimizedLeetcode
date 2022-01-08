"""
https://www.youtube.com/watch?v=DMGtWgH5VmU&t=20s

"""

# Need to come back and check

import collections


class Solution:
    def getCoprimes(self, nums: List[int], edges):

        n = len(nums)
        # key is the value of ancestors nodes, value is the deepest node who has that value
        parents = collections.defaultdict(dict)
        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # populate parents
        visited = set()

        def dfs(node, pathDict, depth):
            parents[node] = pathDict.copy()
            visited.add(node)
            newPathDict = pathDict.copy()
            newPathDict[nums[node]] = (depth, node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, newPathDict, depth + 1)

        dfs(0, {}, 0)

        # calculate the answer
        res = []
        for i in range(n):
            num1 = nums[i]
            parentsList = [(depth, key, nodeID) for key, (depth, nodeID) in parents[i].items()]
            parentsList.sort(reverse=True)

            node = -1

            for _, num2, nodeID in parentsList:
                if math.gcd(num1, num2) == 1:
                    node = nodeID
                    break
            res.append(node)

        return res






