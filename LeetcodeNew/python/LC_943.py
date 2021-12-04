"""
https://buptwc.com/2018/11/19/Leetcode-943-Find-the-Shortest-Superstring/
https://leetcode.com/problems/find-the-shortest-superstring/discuss/252948/Python-Recursion-with-Memory
https://leetcode.com/problems/find-the-shortest-superstring/discuss/195487/python-bfs-solution-with-detailed-explanation(with-extra-Chinese-explanation)

思路分析：
这道题实际上是一个图的问题。
对于A = ["catg","ctaagt","gcta","ttca","atgcatc"]
不妨认为每一个字符串对应一个结点。边的权值则对应着两个结点之间重复部分的长度。
（0对应’catg’, 1对应’ctaagt,以此类推）

其中，G[2][1] = 3表示1结点若放在2结点后面可以省下3个字符长度。
最终，省得越多，最后的字符串长度就越短。

那么这道题就转换成了，在一个图中，从某个点出发将所有点恰好遍历一遍，使得最后路过的路径长度最长。（注意，虽然1,3之间没有连线但仍然可以从结点1走到结点3。）

首先我们将图构造出来

我们这里采用bfs的方法去遍历整个图，但如果不做任何处理，将所有情况全部考虑的话，共有12x11x10x...x1 = 12!种情况，时间复杂度过大。
稍微想一想，这其中有很多重复计算，例如对于这两个状态：

2->1->3->…
1->2->3->…
同样是遍历了1,2,3这三个结点，并且当前都处在3结点上，我们是并不用将这两种情况都计算的。
假设对于1->2->3我们计算出来已经走过的长度为L1，对于2->1->3我们计算出来已经走过的长度为L2，如果有L2 < L1，那么无论后面怎么走，第二种情况都不可能比第一种情况更优。所以我们可以舍弃掉第二种情况。
基于这个思想，我们使用一个空间d[mask][node]来记录当前状态下已经走的路程。其中：
mask表示当前已经遍历过的结点，10011表示已经遍历了0,1,4三个结点。（1 << i）
node表示当前所处结点。

在bfs中，这里采用了这样的结构(node, mask, path, repeat_len)。其中：
node表示当前结点
mask表示当前遍历过的结点
path表示遍历结点的顺序(长度不超过12，所以不用担心空间过大)
repeat_len表示目前重复部分的长度。

当mask == 11111时，表示已经遍历过所有结点，我们取此时repeat_len最大的path，然后通过path构造最后的字符串

例如path = [2,1,3,0,4]，那么构造函数如下：

https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/943.Find-the-Shortest-Superstring

943.Find-the-Shortest-Superstring
这是一道难度较高的题。首先注意题目中的substring是连续的，和subsequence的概念不一样。

其次，我们要能敏锐地将它看出，其本质是一道TSP的问题。举个例子，假如说有三个字符串A,B,C，那么最终答案只可能是类似ABC,ACB,BAC,BCA,CAB,CBA这几种可能性的一种
（其中ABC表示将ABC三个字符串顺序相连，两两相接的部分能共用的话就共用）。于是我们发现，这个题目就是让我们找一条最短路径，能包含所有的节点A,B,C。
例如在上面的这个例子中，ABC,ACB,BAC,BCA,CAB,CBA的路径长度可能是互不相同的，我们要找出最短的。

慢着，路径ABC代表什么意思呢？它代表ABC三个字串连接起来（再利用公有部分）的长度。不难发现一个很好的性质，ABC的长度其实就是A的长度+（A到B的长度）+（B到C的长度）。
其中A到B的长度，表示从字串A增加多少个字符能够变成以B为结尾的字串。例如A=abc,B=bcd,C=cde，那么ABC就代表了abcde，并且肯定是包含了A，B，C三个子串的superstring；其中A到B的长度是1，B到C的长度也是1.

所以，我们可以预处理得到题目中任意两个字串（节点）之间的距离graph[i][j]。现在已知任意节点之间的路径距离，我们要找出一条最短的路径，能包含所有的节点（起始点可以自由选择），这就是典型的旅行商（TSP）问题。

TSP问题最经典的解法是结合了DP的思想。我们设计状态方程dp[set][last],其中set表示已经访问过的节点的集合，last表示这些已经访问过的点集里面最后一个访问到的那个节点。
我们认为{set,last}表示了一种“状态”，dp[set][last]就是到达这种状态时的最短路径长度。为什么要用两个指标来定义“状态”，这是因为仅仅根据set作为状态的话，不能往后续作为扩展。

举个例子，我们已经考察完了set4={1,2,3,4}，得到了当前最优解dp[set4]，那么我们想访问5号节点怎么办呢？显然我们不知道如何从已知的dp[set4]往待求的dp[set5]传递。
但是如果我们额外知道最后一个节点的信息，那么转移方程就好办了：

dp[set5] = min{dp[set4][1]+graph[1][5], dp[set4][2]+graph[2][5], ... , dp[set4][4]+graph[4][5]}
可见dp[set][last]是一个很好的状态，便于我们做状态转移。

当然，如果用一个真正的“集合”作为dp的下表，显然实现上很不方便。TSP有个非常成熟的解决方案，就是用整形的32位bit值为来代表节点集合的状态。第k个bit位的数值是1，那么就说明了集合中包含第k个节点；反之就没有包含。
例如3=binary(0011)表示包含了节点1和0的集合状态。对于大多数小规模的TSP问题而言，一个32位的整形就可以足够表示节点集合的状态了。

在程序中，我们用mask代表记载集合状态的整数，bit表示最后一个节点是哪个。于是有一个比较公式化的算法用来不断更新dp[mask][bit]：

for (int mask=0; mask<2^N; mask++)
  for (int bit=0; bit<N; bit++)
  {      
        pmask = mask删去bit节点;
        for (int i=0; i<N; i++)
        {
          dp[mask][bit] = min_{i}(dp[pmask][i]+graph[i][bit]);
          (where bit is contained in mask, and i is contained in pmask)
          update parent[mask][bit] if necessary;
        }
  }
其中比较精妙的point在于第一行的大循环：for (int mask=0; mask<2^N; mask++)，这样的循环顺序恰好保证了内循环中的dp[pmask][i]永远是已经在之前更新过了的（即已经赋值过的）。
原因简而言之，是因为pmask永远是mask的一个子集，因此我们在更新dp[mask]时，dp[pmask]总是已经ready了。

以上的代码循环结束之后，最终的答案存在dp[2^N-1][bit]之中。其中2^N-1表示所有的点都已经被访问并装在集合里面了，而我们需要遍历bit（也就是考察以哪个点结尾），能够得到最短的总路径。

以上的dp存储的只是最短路径的长度。那么怎么回溯构建整个路径呢？我们只需要给每个状态[mask][bit]再添加一个parent的记录，即k=parent[mask][bit]表示的是：
最优的dp[mask][bit]是通过dp[pmask][k]+graph[k][bit]得到的。于是我们就能够往上回溯一步了，下一步就递归来考察状态{pmask,k}。于是顺着parent的记录，我们最终能够到达全集合set0的状态.


The idea is simple: first, let's store the overlapping for each pair of words. Second, for DP, during each iteration, we look at words[i]; we need to find a unused words[j] and consider to merge the two words together.

For example, words[i] is 'abcde' and words[j] is 'cdef', the merging of the two words will be 'abcdef'. Out of all the possible outcomes, we take the one with minimum length during each iteration.

How do we find an unused word? We use bitmask to keep track of used/unused word. A bit '1' at position i means the words[i] has already been taken.

"""

import functools
import collections


class SolutionTony:
    def shortestSuperstring(self, words):
        n = len(words)
        # table = [[0 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         x, y = words[i], words[j]
        #         size = len(x)
        #         for k in range(1, size):
        #             if y.startswith(x[k:]):
        #                 table[i][j] = size - k
        #                 break
        table = [[0 for i in range(n)] for j in range(n)]
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                for k in range(min(len(word1), len(word2)))[::-1]:
                    # print(word1, word2, k, word1[-k:], word2[:k])
                    if word1[-k:] == word2[:k]:
                        table[i][j] = k
                        break

        full_mask = (1 << n) - 1
        @functools.lru_cache(None)
        def dfs(i, mask):
            if mask == full_mask:
                return words[i]

            res = '#' * 10000
            for j in range(n):
                if mask & (1 << j) == 0:
                    k = table[i][j]
                    string = dfs(j, mask | (1 << j))
                    res = min(res, words[i] + string[k:], key=len)
            return res

        res = '#' * 10000
        for i in range(n):
            res = min(res, dfs(i, 1 << i), key=len)
        return res




class Solution:
    def shortestSuperstring(self, words):
        n = len(words)
        graph = [[0 for i in range(n)] for j in range(n)]
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                for k in range(min(len(word1), len(word2)))[::-1]:
                    # print(word1, word2, k, word1[-k:], word2[:k])
                    if word1[-k:] == word2[:k]:
                        graph[i][j] = k
                        break

        @functools.lru_cache(None)
        def dfs(mask, i):
            if not (mask & (1 << i)):
                return ''

            if mask == (1 << i):
                return words[i]

            res = ''
            for j in range(n):
                if j != i and mask & (1 << j):
                    cand = dfs(mask ^ (1 << i), j) + words[i][graph[j][i]:]
                    if res == '' or len(cand) < len(res):
                        res = cand
            return res

        res = ''
        for i in range(n):
            cand = dfs((1 << n) - 1, i)
            if res == '' or len(cand) < len(res):
                res = cand
        return res



class SolutionDFS:
    def shortestSuperstring(self, A) -> str:
        n = len(A)
        graph = [[0 for i in range(n)] for j in range(n)]
        for i, word1 in enumerate(A):
            for j, word2 in enumerate(A):
                if i == j:
                    continue
                for k in range(min(len(word1), len(word2)))[::-1]:
                    print(word1, word2, k, word1[-k:], word2[:k])
                    if word1[-k:] == word2[:k]:
                        graph[i][j] = k
                        break
        memo = {}
        res = ''
        for k in range(n):
            cand = self.dfs(graph, A, (1 << n) - 1, k, memo)
            if res == '' or len(cand) < len(res):
                res = cand
        return res

    def dfs(self, graph, A, i, k, memo):
        n = len(graph)
        if (i, k) in memo:
            return memo[(i, k)]

        if not (i & (1 << k)):
            return ''

        if i == (1 << k):
            return A[k]

        res = ''
        for j in range(n):
            if j != k and i & (1 << j):
                cand = self.dfs(graph, A, i ^ (1 << k), j, memo) + A[k][graph[j][k]:]
                if res == '' or len(cand) < len(res):
                    res = cand
        memo[(i, k)] = res
        return memo[(i, k)]



class SolutionDP:
    def shortestSuperstring(self, A) -> str:
        # 计算两个字符串的最大重复前后缀，可以用 KMP 优化
        def overlap(s1, s2):
            for i in range(min(len(s1), len(s2)) - 1, 0, -1):
                if s1.endswith(s2[:i]):
                    return i
            return 0

        n = len(A)
        # 计算每两个字符串之间的重叠距离
        dist = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dist[i][j] = overlap(A[i], A[j])
                dist[j][i] = overlap(A[j], A[i])

        # TSP 旅行商问题,状态压缩 DP,时间复杂度 O(n^2*2^n)
        dp = [[0] * n for _ in range(1 << n)]
        path = [[0] * n for _ in range((1 << n))]
        for s in range(1 << n):
            #i is the last
            for i in range(n):
                if s >> i & 1:
                    for j in range(n):
                        if i != j and s >> j & 1:
                            if dp[s][j] <= dp[s ^ (1 << j)][i] + dist[i][j]:  # 这里要<=,不然没路径的path会出错
                                dp[s][j] = dp[s ^ (1 << j)][i] + dist[i][j]
                                path[s][j] = i  # 当前节点的上一个节点是 i

        # 获取路径的尾字符串
        # last = 0
        # for i in range(n):
        #     if dp[-1][i] >= dp[-1][last]:
        #         last = i
        last = dp[-1].index(max(dp[-1]))


        # 输出路径字符串
        res = A[last]
        s = (1 << n) - 1  # 这里要打括号，优先级问题
        for _ in range(n - 1):
            tmp = last
            last = path[s][last]
            res = A[last] + res[dist[last][tmp]:]
            s ^= (1 << tmp)
        return res




class SolutionBFS:
    def shortestSuperstring(self, A):
        def getDistance(s1, s2):
            for i in range(1, len(s1)):
                if s2.startswith(s1[i:]):
                    return len(s1) - i
            return 0

        def pathtoStr(A, graph, path):
            res = A[path[0]]
            for i in range(1, len(path)):
                res += A[path[i]][graph[path[i - 1]][path[i]]:]
            return res

        n = len(A)
        graph = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                graph[i][j] = getDistance(A[i], A[j])
                graph[j][i] = getDistance(A[j], A[i])

        distance = [[0 for i in range(n)] for _ in range(1 << n)]
        queue = collections.deque([(i, 1 << i, [i], 0) for i in range(n)])
        final_len = -1  # 记录最大的repeat_len
        final_path = []  # 记录对应的path
        while queue:
            node, mask, path, dis = queue.popleft()
            if dis < distance[mask][node]:
                continue
            if mask == (1 << n) - 1 and dis > final_len:
                final_path = path
                final_len = dis
                continue
            for i in range(n):
                newMask = mask | (1 << i)
                # case1: 不能走回头路，因为每个结点只能遍历一次
                # case2: 如果走当前这条路能够获得更大的重复长度，才继续考虑
                if newMask != mask and distance[mask][node] + graph[node][i] >= distance[newMask][i]:
                    distance[newMask][i] = distance[mask][node] + graph[node][i]
                    queue.append((i, newMask, path + [i], distance[newMask][i]))

        return pathtoStr(A, graph, final_path)




class SolutionTony:
    def shortestSuperstring(self, A):
        def getDistance(s1, s2):
            # suffix of s1 and prefix of s2
            for i in range(1, len(s1)):
                if s2.startswith(s1[i:]):
                    return len(s1) - i
            return 0

        n = len(A)
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                overlap[i][j] = getDistance(A[i], A[j])
                overlap[j][i] = getDistance(A[j], A[i])

        # distance = [[0 for i in range(n)] for _ in range(1 << n)]
        distance = collections.defaultdict(int)
        queue = collections.deque()
        for i in range(n):
            queue.append([i, 1 << i, [i], 0])
        # queue = collections.deque([(i, 1 << i, [i], 0) for i in range(n)])
        maxi = -1  # 记录最大的repeat_len
        final_path = []  # 记录对应的path
        while queue:
            node, state, path, dis = queue.popleft()
            if dis < distance[(state, node)]:
                continue
            if state == (1 << n) - 1 and dis > maxi:
                final_path = path
                maxi = dis
                continue
            for i in range(n):
                newState = state | (1 << i)
                # case1: 不能走回头路，因为每个结点只能遍历一次
                # case2: 如果走当前这条路能够获得更大的重复长度，才继续考虑

                if newState != state and distance[(state, node)] + overlap[node][i] >= distance[(newState, i)]:
                    distance[(newState, i)] = distance[(state, node)] + overlap[node][i]
                    queue.append((i, newState, path + [i], distance[(newState, i)]))

        res = A[final_path[0]]
        for i in range(1, len(final_path)):
            res += A[final_path[i]][overlap[final_path[i - 1]][final_path[i]]:]
        return res




A = ["catg","ctaagt","gcta","ttca","atgcatc"]
a = SolutionDFS()
print(a.shortestSuperstring(A))







