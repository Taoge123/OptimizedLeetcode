
"""

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.




班上有N名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知A是 B的朋友，B是C 的朋友，
那么我们可以认为A也是 C的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个N * N的矩阵M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第i个和j 个学生互为朋友关系，
否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
---------------------
作者：GorillaNotes
来源：CSDN

问题分析：
（1）可以先找到一个人，把这个人的所有朋友都入队。
（2）然后依次出队，把朋友的朋友都入队，已经入过队列的，则不再入队（是不是广度优先搜索）。
（3）知道不再有朋友入队，而且已经出队完成，说明现在已经组成了一个朋友圈。
（4）然后把剩下的没被分到朋友圈里面的，同学，再次入队，进行下一个朋友圈的计算，依次循环直到结束。
---------------------
作者：GorillaNotes
来源：CSDN
原文：https://blog.csdn.net/XX_123_1_RJ/article/details/82656277
版权声明：本文为博主原创文章，转载请附上博文链接！

这道题让我们求朋友圈的个数，题目中对于朋友圈的定义是可以传递的，
比如A和B是好友，B和C是好友，那么即使A和C不是好友，那么他们三人也属于一个朋友圈。
那么比较直接的解法就是DFS搜索，对于某个人，遍历其好友，然后再遍历其好友的好友，
那么我们就能把属于同一个朋友圈的人都遍历一遍，我们同时标记出已经遍历过的人，
然后累积朋友圈的个数，再去对于没有遍历到的人在找其朋友圈的人，这样就能求出个数。
其实这道题的本质是之前那道题Number of Connected Components in an Undirected Graph，
其实许多题目的本质都是一样的，就是看我们有没有一双慧眼能把它们识别出来：
"""


# dfs, 75ms
class Solution1:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        circles = 0
        visited = [0] * n
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, M, visited)
                circles += 1
        return circles

    def dfs(self, idx, M, visited):
        visited[idx] = 1
        for j in range(len(M)):
            if M[idx][j] == 1 and visited[j] == 0:
                self.dfs(j, M, visited)


# bfs, 115ms
class Solution2:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        circles = 0
        visited = [0] * n
        for i in range(n):
            if visited[i] == 0:
                self.bfs(i, M, visited)
                circles += 1
        return circles

    def bfs(self, idx, M, visited):
        n = len(M)
        visited[idx] = 1
        queue = [idx]
        while queue:
            curr = queue.pop(0)
            for j in range(n):
                if M[curr][j] == 1 and visited[j] == 0:
                    queue.append(j)
                    visited[j] = 1


class Solution3:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        ds = DisjointSet()

        for i in range(len(M)):
            ds.make_set(i)

        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    ds.union(i, j)

        return ds.num_sets

class Node:
    def __init__(self, data, parent=None, rank=0):
        self.data = data
        self.parent = parent
        self.rank = rank

class DisjointSet:
    def __init__(self):
        self.map = {}
        self.num_sets = 0

    def make_set(self, data):
        node = Node(data)
        node.parent = node
        self.map[data] = node
        self.num_sets += 1

    def union(self, data1, data2):
        node1 = self.map[data1]
        node2 = self.map[data2]

        parent1 = self.find_set_util(node1)
        parent2 = self.find_set_util(node2)

        if parent1.data == parent2.data:
            return

        if parent1.rank >= parent2.rank:
            if parent1.rank == parent2.rank:
                parent1.rank += 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2

        self.num_sets -= 1


    def find_set(self, data):
        return self.find_set_util(self.map[data])

    def find_set_util(self, node):
        parent = node.parent
        if parent == node:
            return parent

        node.parent = self.find_set_util(node.parent) # path compression
        return node.parent

