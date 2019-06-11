
"""
Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B. The integer B denotes that from any place (suppose the index is i) in the array A, you can jump to any one of the place in the array A indexed i+1, i+2, …, i+B if this place can be jumped to. Also, if you step on the index i, you have to pay Ai coins. If Ai is -1, it means you can’t jump to the place indexed i in the array.

Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed N using the minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should take to get to the place indexed N using minimum coins.

If there are multiple paths with the same cost, return the lexicographically smallest such path.

If it's not possible to reach the place indexed N then you need to return an empty array.

Example 1:

Input: [1,2,4,-1,2], 2
Output: [1,3,5]


Example 2:

Input: [1,2,4,-1,2], 1
Output: []


Note:

Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm, if and only if at the first i where Pai and Pbi differ, Pai < Pbi; when no such i exists, then n < m.
A1 >= 0. A2, ..., AN (if exist) will in the range of [-1, 100].
Length of A is in the range of [1, 1000].
B is in the range of [1, 100].

"""
"""
这道题给了我们一个数组A，又给了我们一个整数B，表示能走的最大步数，数组上的每个数字都是cost值，如果到达某个位置，
就要加上该位置上的数字，其实位置是在第一个数字上，目标是到达末尾位置，我们需要让总cost值最小，
并输入路径，如果cos相同的话，输出字母顺序小的那个路径。还有就是如果数组上的某个位置为-1的话，
表示到达该位置后不能再去下一个位置，而且数组末位置不能为-1。博主最开始写了一个递归的解法，结果MLE了，
看来这道题对内存使用的管控极为苛刻。所以我们不能将所有的候选路径都存在内存中，而是应该建立祖先数组，
即数组上每个位置放其父结点的位置，有点像联合查找Union Find中的root数组，再最后根据这个祖先数组来找出正确的路径。
由于需要找出cost最小的路径，所以我们可以考虑用dp数组，其中dp[i]表示从开头到位置i的最小cost值，但是如果我们从后往前跳，
那么dp[i]就是从末尾到位置i的最小cost值。

我们首先判断数组A的末尾数字是否为-1，是的话直接返回空集。否则就新建结果res数组，dp数组，和pos数组，
其中dp数组都初始化为整型最大值，pos数组都初始化为-1。然后将dp数组的最后一个数字赋值为数组A的尾元素。
因为我们要从后往前跳，那我们从后往前遍历，如果遇到数字-1，说明不能往前跳了，直接continue继续循环，
然后对于每个遍历到的数字，我们都要遍历其上一步可能的位置的dp[j]值来更新当前dp[i]值，由于限制了步数B，
所以最多能到i+B，为了防止越界，要取i+B和n-1中的较小值为界限，如果上一步dp[j]值为INT_MAX，说明上一个位置无法跳过来，
直接continue，否则看上一个位置dp[j]值加上当前cost值A[i]，如果小于dp[i]，说明dp[i]需要更新，
并且建立祖先数组的映射pos[i] = j。最后在循环结束后，我们判断dp[0]的值，如果是INT_MAX，说明没有跳到首位置，
直接返回空集，否则我们就通过pos数组来取路径。我们从前往后遍历pos数组来取位置，直到遇到-1停止。另外要说明的就是，
这种从后往前遍历的模式得到的路径一定是字母顺序最小的， zestypanda大神的帖子中有证明，不过博主没太看懂-.-|||，
可以带这个例子尝试：

A = [0, 0, 0], B = 2

上面这个例子得到的结果是[1, 2, 3]，是字母顺序最小的路径，而相同的cost路径[1, 3]，就不是字母顺序最小的路径，
参见代码如下：


下面这种方法是正向遍历的解法，正向跳的话就需要另一个数组len，len[i]表示从开头到达位置i的路径的长度，
如果两个路径的cost相同，那么一定是路径长度大的字母顺序小，可以参见例子 A = [0, 0, 0], B = 2。

具体的写法就不讲了，跟上面十分类似，参考上面的讲解，需要注意的就是更新的判定条件中多了一个t == dp[i] && len[i] < len[j] + 1，
就是判断当cost相同时，我们取长度大路径当作结果保存。还有就是最后查找路径时要从末尾往前遍历，
只要遇到-1时停止，参见代码如下：

"""


"""
I used DP. 
dp[i] represent the best path found to get to the place indexed i + 1 and dp[i][0] is the cost of the path.
dp[0] is initialized as [A[0], 1] and the others are initialized as [infinity].
"""
import heapq, collections

class SolutionLee:
    def cheapestJump(self, A, B):
        if not A or A[0] == -1:
            return []
        dp = [[float('inf')] for _ in A]
        dp[0] = [A[0], 1]
        for j in range(1, len(A)):
            if A[j] == -1:
                continue
            dp[j] = min([dp[i][0] + A[j]] + dp[i][1:] + [j + 1] for i in range(max(0, j - B), j))
        return dp[-1][1:] if dp[-1][0] < float('inf') else []


# Same idea,but a top-bottom recursive solution:)

class SolutionLee2:
    def cheapestJump(self, A, B):
        memo={len(A)-1:[A[-1],len(A)]}
        def dp(i):
            if i not in memo:
                memo[i]=[float('inf')]
                for j in range(1,B+1):
                    if i+j<len(A) and A[i+j]!=-1:
                        memo[i]=min([A[i]+dp(i+j)[0]]+[i+1]+dp(i+j)[1:],memo[i])
            return memo[i]
        return dp(0)[1:]


class Solution3:
    def cheapestJump(self, A, B):
        # some trick part
        dp = collections.defaultdict(list)
        heapq.heappush(dp[0], (A[0], [1]))
        for i in range(1, len(A)):
            if A[i] == -1:
                continue
            j = i - 1
            while j >= 0 and i - j <= B:
                if A[j] == -1 or len(dp[j]) == 0:
                    j -= 1
                    continue
                # for elem in dp[i]:
                # print(i,j)
                # print(dp)
                heapq.heappush(dp[i], (dp[j][0][0] + A[i], dp[j][0][1] + [i + 1]))
                j -= 1

        if len(dp[len(A) - 1]) == 0:
            return []
        else:
            return dp[len(A) - 1][0][1]


"""
题目大意：
给定数组A和整数B，A表示N枚硬币的面值，-1表示硬币不存在。

从第1枚硬币出发，每次可以选择其右边的1 - B枚硬币。选择第i枚硬币的开销为A[i]

求最终选择第N枚硬币时，开销最小的选择方案；若存在并列的情况，则选择硬币标号字典序较小的方案。

解题思路：
动态规划（Dynamic Programming）

数组cost[i]表示以第i枚硬币结尾时的最小开销。

数组path[i]表示以第i枚硬币时的最佳选择方案。

若cost[i] > cost[j] + A[i] 或者 cost[i] == cost[j] + A[i] && path[i] > path[j] + [i]

则令cost[i] = cost[j] + A[i], path[i] = path[j] + [i]
"""
class Solution4:
    def cheapestJump(self, A, B):
        N = len(A)
        cost = [0x7FFFFFFF] * (N + 1)
        cost[1] = A[0]
        path = [[] for x in range(N + 1)]
        path[1] = [1]
        for x in range(2, N + 1):
            if A[x - 1] == -1: continue
            for y in range(1, B + 1):
                z = x - y
                if z < 1: break
                if A[z - 1] == -1: continue
                if cost[x] > cost[z] + A[x - 1] or cost[x] == cost[z] + A[x - 1] and path[x] > path[z] + [x]:
                    cost[x] = cost[z] + A[x - 1]
                    path[x] = path[z] + [x]
        return path[-1]


