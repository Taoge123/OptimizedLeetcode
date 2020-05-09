"""
DFS
最直白的方法就是把每个节点的位置给求出来，然后构建出题目要求的排列方式。
为了方便，我们在求的过程中就把相同X值的放到一起，同时保存Y坐标和值。

所以定义了一个Map，这个Map的结构是map<int, vector<pair<int, int>>>，
保存的是x ==> (-y, value)的映射。所以在进行DFS的过程中，我们会给每个坐标都记录下其坐标(X,Y)，
然后我们根据其坐标把相同X的都放到一起。为什么使用-y呢？这是因为题目中告诉我们节点的Y坐标更小，
而题目要求的Y排序是顺序是从上到下的。如果设置根节点层的Y坐标是0的话，
那么下面各层的真实Y值应该是-1,-2,-3……，我们的sort函数默认是递增排序的，
所以为了sort方便，放到vector中的是-y。

在求出相同X的所有(-y, value)对之后，我们进行了排序使得Y值是严格递增的，
当Y值相同时按照value值进行排序。然后把排序好了的节点的value值都取出来放到结果里即可。

一个不引起注意的点是，nodeMap一定要使用map数据结构，而不是unordered_map。
因为map会保证有序的，也就是说对nodeMap遍历的时候，X是已经排序好了。而unordered_map是无序结构，
遍历不会保证X是有序，增加了麻烦。

另外一个C++的知识点是当使用 for (auto nm : nodeMap)的时候，nm不是一个指针，
而是一个复制了的对象，所以不要使用nm->second，而应该使用nm.second.

时间复杂度是O(N + N*(N*log(N) + N))。第一个N是DFS要把每个节点进行遍历一次；
for循环有层N，循环里面有层排序是NlogN，遍历是N）。

空间复杂度是O(N)。

"""
import collections
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root):
        res = collections.defaultdict(list)
        queue = [(root, 0)]

        while queue:
            nextLevel = []
            cur = collections.defaultdict(list)

            for node, level in queue:
                heapq.heappush(cur[level], node.val)

                if node.left:
                    nextLevel.append((node.left, level - 1))

                if node.right:
                    nextLevel.append((node.right, level + 1))

            for level in cur:
                res[level].extend(heapq.nsmallest(len(cur[level]), cur[level]))

            queue = nextLevel

        return [res[i] for i in sorted(res)]


class SolutionDFS:
    def verticalTraversal(self, root):
        self.path = []
        self.dfs(root, 0, 0)
        self.path.sort()
        res = [[self.path[0][2]]]
        for i in range(1, len(self.path)):
            if self.path[i][0] == self.path[i - 1][0]:
                res[-1].append(self.path[i][2])
            else:
                res.append([self.path[i][2]])
        return res

    def dfs(self, root, x, y):
        if not root:
            return
        self.path.append((x, -y, root.val))
        self.dfs(root.left, x - 1, y - 1)
        self.dfs(root.right, x + 1, y - 1)






