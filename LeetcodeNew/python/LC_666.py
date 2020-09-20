



import collections

class SolutionCsp:
    def pathSum(self, nums) -> int:
        table = collections.defaultdict(int)
        if not nums or len(nums) == 0:
            return 0
        self.res = 0
        for num in nums:
            table[num // 10] = num % 10

        self.helper(nums[0] // 10, 0, table)
        return self.res

    def helper(self, root, summ, table):
        level = root // 10
        pos = root % 10
        left = (level + 1) * 10 + pos * 2 - 1
        right = (level + 1) * 10 + pos * 2

        cur = summ + table[root]
        if left not in table and right not in table:
            self.res += cur
            return

        if left in table:
            self.helper(left, cur, table)
        if right in table:
            self.helper(right, cur, table)



class Solution:
    def pathSum(self, nums):
        res, cache = 0, {}
        # Convert numbers to tuples.
        nodes = [self.num_to_tuple(num, i, cache) for i, num in enumerate(nums)]
        pathSumm = [0] * len(nodes)

        for index, node in enumerate(nodes):
            depth, pos, value = node
            pathSumm[index] = value
            # Look up the dictionary for the node's parent.
            if depth - 1 in cache and (pos // 2) in cache[depth - 1]:
                # If node has a parent, add the parent's value to the path sum.
                pathSumm[index] += pathSumm[cache[depth - 1][pos // 2]]
            # Look up the dictionary for the node's children.
            if not (depth + 1 in cache and ((pos * 2) in cache[depth + 1] or (pos * 2 + 1) in cache[depth + 1])):
                # If there are no children, it is a leaf. Add the path sum to the res.
                res += pathSumm[index]
        return res

    def num_to_tuple(self, num, i, cache):
        # The node 113 becomes a tuple of (0, 0, 3).
        depth, pos, value = int(str(num)[0]) - 1, int(str(num)[1]) - 1, int(str(num)[2])
        if depth not in cache:
            cache[depth] = {}
        cache[depth][pos] = i
        return (depth, pos, value)



class Solution:
    def pathSum(self, nums):
        self.ans = 0
        root = Node(nums[0] % 10)

        for x in nums[1:]:
            depth, pos, val = x/100, x/10 % 10, x % 10
            pos -= 1
            cur = root
            for d in range(depth - 2, -1, -1):
                if pos < 2**d:
                    cur.left = cur = cur.left or Node(val)
                else:
                    cur.right = cur = cur.right or Node(val)

                pos %= 2**d

        def dfs(node, running_sum = 0):
            if not node: return
            running_sum += node.val
            if not node.left and not node.right:
                self.ans += running_sum
            else:
                dfs(node.left, running_sum)
                dfs(node.right, running_sum)

        dfs(root)
        return self.ans


"""
Intuition and Algorithm

As in Approach #1, we will depth-first search on the tree. 
One time-saving idea is that we can use num / 10 = 10 * depth + pos 
as a unique identifier for that node. 
The left child of such a node would have identifier 10 * (depth + 1) + 2 * pos - 1, 
and the right child would be one greater.
"""


class Solution2:
    def pathSum(self, nums):
        self.ans = 0
        values = {x / 10: x % 10 for x in nums}
        def dfs(node, running_sum = 0):
            if node not in values: return
            running_sum += values[node]
            depth, pos = divmod(node, 10)
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1

            if left not in values and right not in values:
                self.ans += running_sum
            else:
                dfs(left, running_sum)
                dfs(right, running_sum)

        dfs(nums[0] / 10)
        return self.ans


class Solution3:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dmap = {1 : 0}
        leaves = set([1])
        for num in nums:
            path, val = num / 10, num % 10
            lvl, seq = path / 10, path % 10
            parent = (lvl - 1) * 10 + (seq + 1) / 2
            dmap[path] = dmap[parent] + val
            leaves.add(path)
            if parent in leaves: leaves.remove(parent)
        return sum(dmap[v] for v in leaves)



class Solution4:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total, nodes_map = 0, {}
        def num_to_tuple(num, i):
            # The node 113 becomes a tuple of (0, 0, 3).
            depth, pos, value = int(str(num)[0]) - 1, int(str(num)[1]) - 1, int(str(num)[2])
            if depth not in nodes_map:
                nodes_map[depth] = {}
            nodes_map[depth][pos] = i
            return (depth, pos, value)
        # Convert numbers to tuples.
        nodes = [num_to_tuple(num, i) for i, num in enumerate(nums)]
        path_sums = [0] * len(nodes)

        for index, node in enumerate(nodes):
            depth, pos, value = node
            path_sums[index] = value
            # Look up the dictionary for the node's parent.
            if depth - 1 in nodes_map and (pos // 2) in nodes_map[depth - 1]:
                # If node has a parent, add the parent's value to the path sum.
                path_sums[index] += path_sums[nodes_map[depth - 1][pos // 2]]
            # Look up the dictionary for the node's children.
            if not (depth + 1 in nodes_map and ((pos * 2) in nodes_map[depth + 1] or (pos * 2 + 1) in nodes_map[depth + 1])):
                # If there are no children, it is a leaf. Add the path sum to the total.
                total += path_sums[index]
        return total




nums = [113, 215, 221]
a = Solution()
print(a.pathSum(nums))



