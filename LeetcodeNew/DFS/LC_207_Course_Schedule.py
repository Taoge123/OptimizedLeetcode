"""

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


> 类型：BFS
> Time Complexity O(n)
> Space Complexity O(n)
Topological Sorting题
首先构建一个图，因为题目没有提供。
然后创建一个入度数组。
把入度数组里面为0的课丢进Queue，表示这门课无需Pre-req，
然后对这门课的所有邻居的入度减1。更新完邻居的入度后，如果发现邻居里面有入度为0，
则将其丢进Queue继续迭代。
"""

"""
这道课程清单的问题对于我们学生来说应该不陌生，因为我们在选课的时候经常会遇到想选某一门课程，
发现选它之前必须先上了哪些课程，这道题给了很多提示，第一条就告诉我们了这道题的本质就是在有向图中检测环。
LeetCode中关于图的题很少，有向图的仅此一道，还有一道关于无向图的题是 Clone Graph 无向图的复制。
个人认为图这种数据结构相比于树啊，链表啊什么的要更为复杂一些，尤其是有向图，很麻烦。
第二条提示是在讲如何来表示一个有向图，可以用边来表示，边是由两个端点组成的，用两个点来表示边。
第三第四条提示揭示了此题有两种解法，DFS和BFS都可以解此题。我们先来看BFS的解法，
我们定义二维数组graph来表示这个有向图，一位数组in来表示每个顶点的入度。
我们开始先根据输入来建立这个有向图，并将入度数组也初始化好。然后我们定义一个queue变量，
将所有入度为0的点放入队列中，然后开始遍历队列，从graph里遍历其连接的点，每到达一个新节点，
将其入度减一，如果此时该点入度为0，则放入队列末尾。直到遍历完队列中所有的值，
若此时还有节点的入度不为0，则说明环存在，返回false，反之则返回true。

 

下面我们来看DFS的解法，也需要建立有向图，还是用二维数组来建立，和BFS不同的是，
我们像现在需要一个一维数组visit来记录访问状态，
这里有三种状态，
    0表示还未访问过，
    1表示已经访问了，
    -1表示有冲突。
大体思路是，先建立好有向图，然后从第一个门课开始，找其可构成哪门课，暂时将当前课程标记为已访问，然后对新得到的课程调用DFS递归，直到出现新的课程已经访问过了，则返回false，没有冲突的话返回true，然后把标记为已访问的课程改为未访问

"""

"""
同样是拓扑排序，但是换了个做法，使用DFS。这个方法是，我们每次找到一个新的点，判断从这个点出发是否有环。

具体做法是使用一个visited数组，当visited[i]值为0，说明还没判断这个点；当visited[i]值为1，
说明当前的循环正在判断这个点；当visited[i]值为2，说明已经判断过这个点，
含义是从这个点往后的所有路径都没有环，认为这个点是安全的。

那么，我们对每个点出发都做这个判断，检查这个点出发的所有路径上是否有环，
如果判断过程中找到了当前的正在判断的路径，说明有环；找到了已经判断正常的点，
说明往后都不可能存在环，所以认为当前的节点也是安全的。如果当前点是未知状态，
那么先把当前点标记成正在访问状态，然后找后续的节点，直到找到安全的节点为止。
最后如果到达了无路可走的状态，说明当前节点是安全的。

findOrder函数中的for循环是怎么回事呢？这个和BFS循环次数不是同一个概念，
这里的循环就是看从第i个节点开始能否到达合理结果。这个节点可能没有出度了，
那就把它直接放到path里；也可能有出度，那么就把它后面的节点都进行一次遍历，
如果满足条件的节点都放到path里，同时把这次遍历的所有节点都标记成了已经遍历；
如果一个节点已经被安全的访问过，那么就放过它，继续遍历下个节点。

时间复杂度是O(N)，空间复杂度是O(N)。
--------------------- 
作者：负雪明烛 
来源：CSDN 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82951771 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""

"""

看到给的第二个测试用例立马就明白了，就是判断这些课程能否构成有向无环图（DAG）。
而任何时候判断DAG的方法要立刻想到拓扑排序。

拓扑排序是对有向无环图（DAG）而言的，对图进行拓扑排序即求其中节点的一个拓扑序列，
对于所有的有向边（U, V）（由U指向V），在该序列中节点U都排在节点V之前。

方法是每次选择入度为0的节点，作为序列的下一个节点，然后移除该节点和以从节点出发的所有边。

那这个方法比较简单粗暴了：要循环N次，这个循环次数并不是遍历节点的意思，而是我们如果正常取点的话，
N次就能把所有的节点都取完了，如果N次操作结束还没判断出来，那么就不是DAG.在这N次中，
每次都找一个入度为0的点，并把它的入度变为-1，作为已经取过的点不再使用，
同时把从这个点指向的点的入度都-1.

这个过程中，如果找不到入度为0的点，那么说明存在环。如果N次操作，
每次都操作成功的去除了一个入度为0的点，那么说明这个图是DAG.

时间复杂度是O(N ^ 2)，空间复杂度是O(N)。
--------------------- 
"""

import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = []
        while queue:
            node = queue.popleft()
            visited.append(node)
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return len(visited) == numCourses



