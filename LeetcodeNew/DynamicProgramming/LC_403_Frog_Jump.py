
"""
general DP(LIS) solution in Python
https://www.cnblogs.com/grandyang/p/5888439.html


A frog is crossing a river. The river is divided into x units and at each unit there may
or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units.
Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping
1 unit to the 2nd stone, then 2 units to the 3rd stone, then
2 units to the 4th stone, then 3 units to the 6th stone,
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as
the gap between the 5th and 6th stone is too large.
"""

"""
Following is my backtracking solution using dict for memorization.

The memo dict is using for save those dead end. 
So when we get to the same stone with the same speed we don't need to search further.
"""
import collections

class Solution1:
    def canCross(self, stones):
        self.memo = set()
        target = stones[-1]
        stones = set(stones)

        res = self.bt(stones, 1, 1, target)
        return res

    def bt(self, stones, cur, speed, target):
        # check memo
        if (cur, speed) in self.memo:
            return False

        if cur == target:
            return True

        if cur > target or cur < 0 or speed <= 0 or cur not in stones:
            return False
        # dfs
        candidate = [speed - 1, speed, speed + 1]
        for c in candidate:
            if (cur + c) in stones:
                if self.bt(stones, cur + c, c, target):
                    return True

        self.memo.add((cur, speed))
        return False


class Solution11:
    def canCross(self, stones):
        target, stones, memo = stones[-1], set(stones), set()
        return self.backtrack(stones, 1, 1, target, memo)

    def backtrack(self, stones, pos, jump, target, memo):
        if (pos, jump) in memo:
            return False
        if pos == target:
            return True
        if jump <= 0 or pos not in stones:
            return False
        for j in (jump - 1, jump, jump + 1):
            if self.backtrack(stones, pos + j, j, target, memo):
                return True
        memo.add((pos, jump))  # record bad position and jump
        return False


class Solution2:
    def canCross(self, stones):
        stone_set, fail = set(stones), set()
        stack = [(0, 0)]
        while stack:
            stone, jump = stack.pop()
            for j in (jump-1, jump, jump+1):
                s = stone + j
                if j > 0 and s in stone_set and (s, j) not in fail:
                    if s == stones[-1]:
                        return True
                    stack.append((s, j))
            fail.add((stone, jump))
        return False


class Solution3:
    def canCross(self, stones):
        # create a dictionary where the keys are the stones
        # and the values are empty sets that will contain
        # integers which represent the jump lengths that
        # can reach the stone represented by the key
        d = dict((x, set()) for x in stones)

        # catches a tricky test case: stones = [0,2]
        if stones[1] != 1:
            return False

        # the problems says that the first jump made is
        # always of length 1 and starts at stone 0. That
        # means the jump length that was used to reach
        # stone 1 is 1 so I add it into the set at stone 1
        d[1].add(1)

        # iterate over all the stones after 0
        for i in range(len(stones[1:])):

            # iterate over each jump length used to reach
            # the current stone
            for j in d[stones[i]]:

                # iterate over every jump length possible
                # (k-1, k, k+1) given the current jump length
                for k in range(j - 1, j + 2):

                    # if that jump length lands on a stone
                    if k > 0 and stones[i] + k in d:
                        # add that jump length used to get there to
                        # the set of jump lengths for the stone the
                        # jump puts the frog on
                        d[stones[i] + k].add(k)
        # if the last stone has any jump lengths in it's
        # set, that means that it is possible to get to
        # the last stone
        return d[stones[-1]] != set()

"""
The problem is a member of the longest increasing subsequence problems family which is called LIS usually. 
And its DP solution is also general. It looks very consice.
"""
class Solution4:
    def canCross(self, stones):
        N = len(stones)
        if N == 0 or (N > 1 and stones[1] != 1):
            return False

        dp = [False for _ in range(N)]  # dp[i] means whether stone i can be reached or not
        dp[0] = dp[1] = True
        next_jump = collections.defaultdict(list)  # to record the possible next jumps from stone i
        next_jump[1] = [0, 1, 2]

        for i in range(2, N):
            for j in range(1, i):
                need_jump = stones[i] - stones[j]
                if dp[j] and need_jump in next_jump[j]:
                    dp[i] = True
                    next_jump[i].extend([need_jump, need_jump + 1, need_jump - 1])

        return dp[N - 1]


class Solution5:
    def canCross(self, stones):
        dic = {s: set() for s in stones}
        dic[0].add(1)

        for s in stones:
            nex = dic[s]
            for step in nex:
                if s + step in dic:
                    if s + step == stones[-1]:
                        return True
                    if step - 1 > 0:
                        dic[s + step].add(step - 1)
                    dic[s + step].add(step)
                    dic[s + step].add(step + 1)
        return False

class Solution6:
    def canCross(self, stones):
        dp = [set() for item in stones]
        dp[0].add(1) #dp[i][j] means if starts from i, we can jump j steps
        for i in range(len(stones)):
            for j in range(i):
                k = stones[i]-stones[j]
                if k in dp[j]: #target distance exists in previous stones
                    dp[i].add(k)
                    dp[i].add(k+1)
                    dp[i].add(k-1) #if k-1<=0, we can skip this, but it doesn't matter
        return bool(dp[len(stones)-1])


"""
题目大意：
一只青蛙过河。河流分成x个单元，每一个单元可能会有石头。青蛙可以跳到石头上，但是不能跳入水中。

给定一列石头的位置（以单元数计），顺序递增，判断青蛙是否可以跳到最后一块石头上。
初始时，青蛙站在第一块石头上并且假设只能向前跳1个单元。

如果青蛙上一次跳过k个单元，那么它下一次只能跳 k - 1, k, 或者 k + 1 个单元。注意青蛙只能向前跳。

注意：

石头的个数在[2, 1100)之间。

每一个石头的位置都是一个非负整数 < 2^31。

第一块石头的位置永远是0。

解题思路：
广度优先搜索（BFS）

利用元组(x, y)表示青蛙跳跃的状态：x表示位置, y表示上一跳的单元数。

初始将(0, 0)加入队列q，利用二维数组v记录元组(x, y)是否被访问过。

循环遍历队列q，根据队头状态扩展队列，直到队列为空。
"""
class Solution7:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        q = collections.deque()
        v = collections.defaultdict(lambda : collections.defaultdict(bool))
        stoneSet = set(stones)
        q.append((0, 0))
        v[0][0] = True
        while q:
            x, y = q.popleft()
            if x == stones[-1]: return True
            for z in (y - 1, y, y + 1):
                if z > 0 and not v[x + z][z] and x + z in stoneSet:
                    v[x + z][z] = True
                    q.append((x + z, z))
        return False

"""
思路
这个题我们最简单的dp思路，就是dp(i, k)表示在第i个石头上，且从上一个石头跳k单位长度过来，
是否可行。但是由于k每次可以加1，它最大可以到O(n^2)，复杂度过高我们可以进一步简化dp，
其实第i个石头必然是从前i-1个石头上跳过来的，上一个定了，k也就定了，所以k的范围可以被缩小到O(n)，
状态定义就是dp(i, j)表示在第i个石头上，且从第j个石头跳过来，是否可行进一步，考虑dp(i, j)有效的可能不多，
所以用一个hash set存储可行的方案，当然这步我也不确定是否可以加速，因为没有本质上降低复杂度，
且hash set插入时开新内存空间可能慢一些。
"""
"""
我们也可以用迭代的方法来解，用一个哈希表来建立每个石头和在该位置上能跳的距离之间的映射，
建立一个一维dp数组，其中dp[i]表示在位置为i的石头青蛙的弹跳力(只有青蛙能跳到该石头上，
dp[i]才大于0)，由于题目中规定了第一个石头上青蛙跳的距离必须是1，为了跟后面的统一，
我们对青蛙在第一块石头上的弹跳力初始化为0(虽然为0，但是由于题目上说青蛙最远能到其弹跳力+1的距离，
所以仍然可以到达第二块石头)。我们用变量k表示当前石头，然后开始遍历剩余的石头，
对于遍历到的石头i，我们来找到刚好能跳到i上的石头k，如果i和k的距离大于青蛙在k上的弹跳力+1，
则说明青蛙在k上到不了i，则k自增1。我们从k遍历到i，如果青蛙能从中间某个石头上跳到i上，
我们更新石头i上的弹跳力和最大弹跳力。这样当循环完成后，
我们只要检查最后一个石头上青蛙的最大弹跳力是否大于0即可"""

"""
与一般DP不同的是 青蛙能跳k-1，k，k+1步三种不同的情况 
所以用字典存储跳到这个石头上所用的步数
"""
class Solution8:
    def canCross(self, stones):

        #maxJumpstep 记录的是上一次跳过来的步数
        if len(stones)<=1: return True
        elif stones[1]!=1: return False
        else:
            maxJumpstep={s:set() for s in stones}
            maxJumpstep[1].add(1)
            for s in stones[1:-1]:
                for j in maxJumpstep[s]:
                        for jump in (j-1,j,j+1):
                            if jump>0 and s+jump in maxJumpstep:
                                maxJumpstep[s+jump].add(jump)
            return len(maxJumpstep[stones[-1]])>0


"""
思路:
无脑dp即可.

dp[i][j]是一个bool值,表示青蛙能否到达第i个石头,并且刚才的最后一跳的距离是j.

dp[i][j] = dp[k][j-1] || dp[k][j] || dp[k][j+1] (其中k<i)

答案就是any( dp[n-1][j] ) (其中j要枚举所有最后一跳的距离)



由于距离可以是个很大的值,因此dp数组的第二维j没法直接用数组表示,我们可以用平衡树或者hash表代替.

对一个石头来说,它前面最多有O(n)个石头,也就是说最多有O(n)个最后一跳的距离j.

因此,dp的复杂度是O(n2logn)或者O(n2).


有趣的是,倒着推dp居然TLE,顺着推dp才能AC.

可能是因为倒着推dp是实打实的O(n2logn),而顺着推的dp是玄学的O(n2logn).

总结:
dp,dp[i][j]表示能否到达第i个石头,并且最后一跳距离为j.
"""












