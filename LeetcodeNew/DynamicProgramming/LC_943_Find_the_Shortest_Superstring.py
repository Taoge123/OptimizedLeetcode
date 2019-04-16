
"""
https://leetcode.com/problems/find-the-shortest-superstring/discuss/195487/python-bfs-solution-with-detailed-explanation(with-extra-Chinese-explanation)
https://leetcode.com/problems/find-the-shortest-superstring/discuss/195203/Python-AC-concise-solution-~132-ms
https://leetcode.com/problems/find-the-shortest-superstring/discuss/194932/Travelling-Salesman-Problem
https://buptwc.com/2018/11/19/Leetcode-943-Find-the-Shortest-Superstring/
https://www.geeksforgeeks.org/shortest-superstring-problem/


Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.

Example 1:

Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"

Note:

1 <= A.length <= 12
1 <= A[i].length <= 20
"""

"""
you can get Chinese explanation here

First, we convert this problem into a graph problem.
for instance, A = ["catg","ctaagt","gcta","ttca","atgcatc"]
we regard each string in A as a node, and regard the repeat_length of two string as edge weight. then ,we get this graph G:
image

for G[2][1] = 3, it means that we can save 3 characters length by place node 1 behind node 2, etc gctaagt.

In the end, the more we save, the shorter string length we will get.

So, the question now is:
In a given graph, we can start in any node, and traverse all node in this graph excatly once, to get the maximum save length.
(Note that although there is no connection between 1,3, you can still go from node 1 to node 3.)

first we construct the graph:

def getDistance(s1, s2):
        for i in range(1, len(s1)):
            if s2.startswith(s1[i:]):
                return len(s1) - i
        return 0

n = len(A)
G = [[0]*n for _ in xrange(n)]
for i in range(n):
    for j in range(i+1, n):
        G[i][j] = getDistance(A[i], A[j])
        G[j][i] = getDistance(A[j], A[i])
        
if we consider all possible case, it will be n*(n-1)*(n-2)*...*1 = n! possible cases. Obviously it won’t work.
We need to make some optimizations, look at these two cases：
2->1->3->... and 1->2->3->...
Both cases traverse three nodes 1, 2, and 3, and is currently at the node 3.
for 2->1->3->..., we assume the save length now is L1
for 1->2->3->..., we assume the save length now is L2
if L2 < L1, regardless of how the strategy is adopted afterwards, the second case cannot be better than the first case. 
So we can discard the second case.

Based on this idea, we difine d[mask][node] represent the now save length in the status (mask, node).
mask represent the node we have traversed, 10011 means traversed node 0,1,4
node represent the current node.

In BFS solution, such a data structure is stored in the queue (node, mask, path, s_len)
path means the order of traversed nodes.
s_len means the save length.

Once mask == (1<<n)-1, it means that all nodes have been traversed. Now we find the maximum s_len and get the corresponding path.
Finally, we construct the answer via path.

python bfs code:
"""
import collections

class Solution1:
    def shortestSuperstring(self, A):
        def getDistance(s1, s2):
            for i in range(1, len(s1)):
                if s2.startswith(s1[i:]):
                    return len(s1) - i
            return 0

        def pathtoStr(A, G, path):
            res = A[path[0]]
            for i in range(1, len(path)):
                res += A[path[i]][G[path[i-1]][path[i]]:]
            return res

        n = len(A)
        G = [[0]*n for _ in xrange(n)]
        for i in range(n):
            for j in range(i+1, n):
                G[i][j] = getDistance(A[i], A[j])
                G[j][i] = getDistance(A[j], A[i])

        d = [[0]*n for _ in xrange(1<<n)]
        Q = collections.deque([(i, 1<<i, [i], 0) for i in xrange(n)])
        l = -1 # record the maximum s_len
        P = [] # record the path corresponding to maximum s_len
        while Q:
            node, mask, path, dis = Q.popleft()
            if dis < d[mask][node]: continue
            if mask == (1<<n) - 1 and dis > l:
                P,l = path,dis
                continue
            for i in xrange(n):
                nex_mask = mask | (1<<i)
                # case1: make sure that each node is only traversed once
                # case2: only if we can get larger save length, we consider it.
                if nex_mask != mask and d[mask][node] + G[node][i] >= d[nex_mask][i]:
                    d[nex_mask][i] = d[mask][node] + G[node][i]
                    Q.append((i, nex_mask, path+[i], d[nex_mask][i]))

        return pathtoStr(A,G,P)


"""
Many thanks to @ygt2016. The original code is here. 
I converted the code to recursion, which might be a little easier to understand. Hope this is helpful.
The general idea is:

1. Build a (dense) graph whose node i is the ith word in A. The weight on the arc i-->j is graph[i][j], 
   representing the length of the overlapping part between A[i] and A[j].
2. Then, our goal is to find an ordering of the words (nodes) 0,1,2,...,n-1 
   such that when the words are concatenated in this order, the total length is the smallest. Define the state as (i,k), 
   where i is a number whose binary form indicates which nodes are included in the ordering; k denotes the last node in the ordering. 
   Let memo[i,k] be the shortest superstring when concatenating the words represented by the bits in i and with k as the last word. 
   (You may call memo as dp, if you want.)
3. The recursion part is memo[i,k]=min(i ^ (1 << k), j), for all the bits j in the ordering i excluding k itself.
4. Finally, what we are looking for is just the best result within memo[(i << n) - 1, k], for all the k in {0,1,2,...,n-1}.
"""
class Solution2:
    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        # Building the graph
        graph = [[0] * n for _ in range(n)]
        for i, word1 in enumerate(A):
            for j, word2 in enumerate(A):
                if i == j: continue
                for k in range(min(len(word1), len(word2)))[::-1]:
                    if word1[-k:] == word2[:k]:
                        graph[i][j] = k
                        break

        # Recursion. i is a mask to represent the ordering. k is the last node in the ordering.
        memo = {}

        def search(i, k):
            if (i, k) in memo: return memo[i, k]
            if not (i & (1 << k)): return ''
            if i == (1 << k): return A[k]
            memo[i, k] = ''
            for j in range(n):
                if j != k and i & (1 << j):
                    candidate = search(i ^ (1 << k), j) + A[k][graph[j][k]:]
                    if memo[i, k] == '' or len(candidate) < len(memo[i, k]):
                        memo[i, k] = candidate
            return memo[i, k]

        # Finding the best
        res = ''
        for k in range(n):
            candidate = search((1 << n) - 1, k)
            if res == '' or len(candidate) < len(res):
                res = candidate
        return res


class Solution3:
    def shortestSuperstring(self, A):

        # construct a directed graph
        #   node i => A[i]
        #   weights are represented as an adjacency matrix:
        #   shared[i][j] => length saved by concatenating A[i] and A[j]
        n = len(A)
        shared = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(min(len(A[i]), len(A[j])), -1, -1):
                    if A[i][-k:] == A[j][:k]:
                        shared[i][j] = k
                        break

        # The problem becomes finding the shortest path that visits all nodes exactly once.
        # Brute force DFS would take O(n!) time.
        # A DP solution costs O(n^2 2^n) time.
        #
        # Let's consider integer from 0 to 2^n - 1.
        # Each i contains 0-n 1 bits. Hence each i selects a unique set of strings in A.
        # Let's denote set(i) => {A[j] | j-th bit of i is 1}
        # dp[i][k] => shortest superstring of set(i) ending with A[k]
        #
        # e.g.
        #   if i = 6 i.e. 110 in binary. dp[6][k] considers superstring of A[2] and A[1].
        #   dp[6][1] => the shortest superstring of {A[2], A[1]} ending with A[1].
        #   For this simple case dp[6][1] = concatenate(A[2], A[1])
        dp = [[''] * 12 for _ in range(1 << 12)]
        for i in range(1 << n):
            for k in range(n):
                # skip if A[k] is not in set(i)
                if not (i & (1 << k)):
                    continue
                # if set(i) == {A[k]}
                if i == 1 << k:
                    dp[i][k] = A[k]
                    continue
                for j in range(n):
                    if j == k:
                        continue
                    if i & (1 << j):
                        # the shortest superstring if we remove A[k] from the set(i)
                        s = dp[i ^ (1 << k)][j]
                        s += A[k][shared[j][k]:]
                        if dp[i][k] == '' or len(s) < len(dp[i][k]):
                            dp[i][k] = s

        min_len = float('inf')
        result = ''

        # find the shortest superstring of all candidates ending with different string
        for i in range(n):
            s = dp[(1 << n) - 1][i]
            if len(s) < min_len:
                min_len, result = len(s), s
        return result


"""
Travelling Salesman Problem

graph[i][j] means the length of string to append when A[i] followed by A[j]. eg. 
A[i] = abcd, A[j] = bcde, then graph[i][j] = 1
Then the problem becomes to: find the shortest path in this graph which visits every node exactly once. 
This is a Travelling Salesman Problem.
Apply TSP DP solution. Remember to record the path.
Time complexity: O(n^2 * 2^n)
"""
"""
Solution 1: Search + Pruning
Try all permutations. Pre-process the cost from word[i] to word[j] and store it in g[i][j].
"""

"""
Solution 2: DP
g[i][j] is the cost of appending word[j] after word[i], or weight of edge[i][j].

We would like find the shortest path to visit each node from 0 to n – 1 once 
and only once this is called the Travelling sells man’s problem which is NP-Complete.

We can solve it with DP that uses exponential time.

dp[s][i] := min distance to visit nodes (represented as a binary state s) once and only once and the path ends with node i.

e.g. dp[7][1] is the min distance to visit nodes (0, 1, 2) and ends with node 1, the possible paths could be (0, 2, 1), (2, 0, 1).

Time complexity: O(n^2 * 2^n)

Space complexity: O(n * 2^n)
"""

"""
Approach 1: Dynamic Programming
Intuition

We have to put the words into a row, where each word may overlap the previous word. This is because no word is contained in any word.

Also, it is sufficient to try to maximize the total overlap of the words.

Say we have put some words down in our row, ending with word A[i]. 
Now say we put down word A[j] as the next word, where word j hasn't been put down yet. The overlap increases by overlap(A[i], A[j]).

We can use dynamic programming to leverage this recursion. 
Let dp(mask, i) be the total overlap after putting some words down (represented by a bitmask mask), 
for which A[i] was the last word put down. 
Then, the key recursion is dp(mask ^ (1<<j), j) = max(overlap(A[i], A[j]) + dp(mask, i)), 
where the jth bit is not set in mask, and i ranges over all bits set in mask.

Of course, this only tells us what the maximum overlap is for each set of words. 
We also need to remember each choice along the way (ie. the specific i that made dp(mask ^ (1<<j), j) achieve a minimum) 
so that we can reconstruct the answer.

Algorithm

Our algorithm has 3 main components:

- Precompute overlap(A[i], A[j]) for all possible i, j.
- Calculate dp[mask][i], keeping track of the "parent" i for each j as described above.
- Reconstruct the answer using parent information.
Please see the implementation for more details about each section.
"""

class SolutionAwice:
    def shortestSuperstring(self, A):
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in xrange(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in xrange(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in xrange(1<<N)]
        parent = [[None] * N for _ in xrange(1<<N)]
        for mask in xrange(1, 1 << N):
            for bit in xrange(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in xrange(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1<<N) - 1
        i = max(xrange(N), key = dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1<<i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in xrange(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in xrange(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)


"""
思路

以字符串为节点，字符串之间的共同前缀后缀长度为边，建立有向图。问题转化为求有向图的最长哈密顿道路。

建图过程：对于字符串集合中的字符串a与字符串b, 如果a[-i:] == b[0:i]，
则从a向b连一条长度为i的有向边，表示a的后缀与b的前缀共用，b在a后；
同理，如果a[0:j] == b[-j:]，则从b向a连一条长度为j的有向边，表示b的后缀与a的前缀共用，a在b后。

最长哈密顿道路：回忆最短哈密顿道路的题目POJ 3311 Hie with the Pie（状压DP），我们用状态压缩动态规划求解。
同样，最长哈密顿道路也可以用状压DP求解。用dp[s][i]表示经过的节点组成的状态为s的时候，
到达节点i所经过的长度，其中(s & (1<<j))表示状态s是否经过节点j. 从1到(1<<n)-1遍历状态s，
最终取dp[(1<<n)-1][i](i=0,1,…,n-1)中的最大者，就是最长哈密顿道路。

回溯：由于题目要求输出路径，所以求出最长哈密顿道路的长度之后，还要回溯找到最长哈密顿道路的各个节点的顺序，按顺序输出。
采用的方法是令dp数组的元组为一个类，类属性包括道路长度和前驱节点，并置起始节点的前驱为-1，反向回溯直至遇到-1节点，
可以得到逆序的路径，再逆序输出即可。
"""


class Solution4:
    def shortestSuperstring(self, A):

        n = len(A)
        adj = [[0 for _ in range(n)] for _ in range(n)]

        def helper(s1, s2):
            ma = min(len(s1), len(s2))
            for k in range(ma, 0, -1):
                if s1[len(s1) - k:] == s2[:k]: return k
            return 0

        for i in range(n):
            for j in range(n):
                if i == j: continue
                adj[i][j] = helper(A[i], A[j])

        dp = [[-1 for _ in range(n)] for _ in range(2 ** n)]
        path = [[-1 for _ in range(n)] for _ in range(2 ** n)]
        for mask in range(2 ** n):
            for bit in range(n):
                if mask & (1 << bit):
                    mask2 = mask ^ (1 << bit)
                    if mask2 == 0:
                        dp[mask][bit] = 0
                        continue
                    for i in range(n):
                        if mask2 & (1 << i):
                            t = dp[mask2][i] + adj[i][bit]
                            if t > dp[mask][bit]:
                                dp[mask][bit] = t
                                path[mask][bit] = i
        mask = 2 ** n - 1
        s = dp[mask].index(max(dp[mask]))
        res = []
        while len(res) < n:
            res.append(s)
            s = path[mask][s]
            mask = mask ^ (1 << res[-1])
        res = res[::-1]

        s = A[res[0]]
        for i in range(1, n):
            s += A[res[i]][adj[res[i - 1]][res[i]]:]


"""
分析
（1）先建图：预处理计算出Cost，也就是一个节点到另一个节点的权重，这里的话,，g[i][j]表示将A[j]加到A[i]的后面，路径的长度:

(2) 题目转化为找一条访问过每个节点一次的最短的路径

(3) 记忆化DP:
dp[s][i] ：表示访问了节点集合s，且最后一个节点是i的最短的路径，注意这里s是一个Binary String，表示哪些节点已经访问过了，为1的节点是已经访问过的；

Assume we want to travel nodes: {n1, n2, n3, n4} then
i = 2 ^ n1 +2 ^ n2 +2 ^ n3 +2 ^ n4;

path[s][i]:表示访问了节点集合s，并且最后一个节点是i，i前面的一个节点； 记录路径中，i的前面的一个点，以便于重建途径的时候的回溯

(4) dp更新策略：
dp[s][i] = min(dp[s - 2^i][j] + g[j][i]) #将j加到i的后面

class Solution {
    public String shortestSuperstring(String[] A) {
        int n = A.length;
        int[][] graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = calCost(A, i, j);  //把j加到i后面的路径长度，即图中i->j的边长
                graph[j][i] = calCost(A, j, i);
            }
        }
        
        int[][] dp = new int[1 << n][n];  //dp[s][i] ：表示访问了节点集合s，且最后一个节点是i的最短的路径
        int[][] path = new int[1 << n][n];
        int min = Integer.MAX_VALUE, last = -1;
        
        for (int state = 1; state < (1 << n); state++) {  //枚举所有的节点集合组成状态
            Arrays.fill(dp[state], Integer.MAX_VALUE);
            for (int node = 0; node < n; node++) {
                if ((state & (1 << node)) > 0) { //判断node在不在节点集合中
                    int leftState = state - (1 << node);  //剩下的节点集合
                    if (leftState == 0) {  //如果只剩一个节点了，则当前长度就是node的长度
                        dp[state][node] = A[node].length();
                    } else {
                        for (int k = 0; k < n; k++) {  //dp更新
                            if (dp[leftState][k] != Integer.MAX_VALUE && 
                                dp[leftState][k] + graph[k][node] < dp[state][node]) {  //如果访问过了leftState且经过k点的路径更小，则更
                                dp[state][node] = dp[leftState][k] + graph[k][node];
                                path[state][node] = k;
                            }
                        }
                    }
                }
                if (state == (1 << n) - 1 && dp[state][node] < min) {
                    min = dp[state][node];
                    last = node;
                }
                //System.out.println(dp[state][node]);
            }
        }
        //建立路径        
        StringBuilder sb = new StringBuilder();
        int cur = (1 << n) - 1;
        Stack<Integer> stack = new Stack<>();
        while (cur > 0) {
            stack.push(last);
            int temp = cur;
            cur -= (1 << last);
            last = path[temp][last];
        }
                
        int i = stack.pop();
        sb.append(A[i]);
        while (!stack.isEmpty()) {
            int j = stack.pop();
            sb.append(A[j].substring(A[j].length() - graph[i][j]));
            i = j;
        }
        return sb.toString();
    }
    
    private int calCost(String[] A, int i, int j) {
        for (int pos = 1; pos < A[i].length(); pos++) {
            if (A[j].startsWith(A[i].substring(pos))) {
                return A[j].length() - A[i].length() + pos;
            }
        }
        return A[j].length();
    }
}



"""


