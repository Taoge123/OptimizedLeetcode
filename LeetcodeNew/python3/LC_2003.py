
import collections


class Solution0:
    def smallestMissingValueSubtree(self, parents, nums):
        n = len(parents)
        res = [1] * n
        visited = set()
        if 1 not in nums:
            return res
        graph = collections.defaultdict(list)
        for i in range(n):
            graph[parents[i]].append(i)

        def dfs(node):
            if nums[node] not in visited:
                for child in graph[node]:
                    dfs(child)
                visited.add(nums[node])

        i = nums.index(1)
        miss = 1
        while i >= 0:
            dfs(i)
            while miss in visited:
                miss += 1
            res[i] = miss
            i = parents[i]
        return res


class Solution:
    def smallestMissingValueSubtree(self, parents, nums):

        def dfs(node):
            if not visited[nums[node]]:
                visited[nums[node]] = True
                for child in graph[node]:
                    dfs(child)

        n = len(nums)
        if 1 not in nums:
            return [1] * n

        graph = collections.defaultdict(list)
        for i, p in enumerate(parents):
            graph[p].append(i)

        curNode = nums.index(1)
        # print(nums, nums[1],  nums.index(1), curNode)
        visited = [False] * (max(nums) + 2)
        res = [1] * n
        curMissingNum = 1

        while curNode != -1:
            # mark all the numbers for the subtree rooted at curNode
            dfs(curNode)

            # find first missing numebr for the current subtree
            while visited[curMissingNum]:
                curMissingNum += 1

            res[curNode] = curMissingNum

            # move to the next parent
            curNode = parents[curNode]
        return res




class Solution2:
    def smallestMissingValueSubtree(self, parents, nums):
        n = len(parents)
        root = None
        node_with_num_one = None
        # construct graph
        graph = collections.defaultdict(list)
        for i in range(n):
            if parents[i] == -1:
                root = i
            else:
                graph[parents[i]].append(i)
            if nums[i] == 1:
                node_with_num_one = i

        res = [1] * n
        if node_with_num_one is None:
            return res
        # seen[i] = 1 means node i has been visited
        seen = [0] * 100002
        curr = node_with_num_one
        prev_missing = 1
        while curr != -1:
            # mark the values of the subtree rooted at curr
            self.dfs(curr, graph, seen, nums)
            # find the first unseen num
            for missing in range(prev_missing, 100002):
                if seen[missing] == 0:
                    res[curr] = missing
                    break
            prev_missing = missing
            curr = parents[curr]

        return res

    def dfs(self, root, graph, seen, nums):
        """Do DFS from root and mark the values of the subtree rooted at root in seen.
        """
        if seen[nums[root]] == 0:
            seen[nums[root]] = 1
            for child in graph[root]:
                self.dfs(child, graph, seen, nums)



