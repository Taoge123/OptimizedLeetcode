"""
https://leetcode-cn.com/problems/parallel-courses-ii/solution/bfsxian-guo-by-sun-man-man/

每个阶段k门课, 几个阶段修完
1->2
3->4->7
5->6->8->9


d[state] --> 状态压缩 -》 2^15
dp[111...111]
dp[000...001]
dp[000...101]

preState -> state
1. preState is a subset of state
2. countOne(state) - countOne(preStatet) <= k
3. preState must contain prerequisite of state

for state in range(0, (1<<n)):
    dp[state] = min(dp[state], dp[preState] + 1)

1494.Parallel-Courses-II
此题乍看贪心法可解。如果想要得到一个合法的课程顺序，必然利用拓扑排序的手段，首先完成那些入度为0的课程。但是本题特别之处在于，如果入度为0的课程多余k个，那么第一轮该优先选取哪k个，才能保证最终用最少的轮数完成所有课程？事实上，并没有任何有效的贪心策略能够帮助挑选这k个课程。优先有序节点总数多的课程，或者优先后续节点深度多的课程，都是没有道理的。

事实上这是一道NP问题，并没有多项式时间的解法。所以只好用暴力的方法去解决。状态压缩DP就是比较“高效”的暴力方法。事实上，题目给出n<=15的条件，就暗示了应该用这种方法。

我们用整形变量state的各个bit位来代表是否完成了某门课程，比如说第i个bit位是1就表示完成了第i门课程。dp[state]表示完成对应的这些课程需要最少多少轮。显然，我们需要考虑前一轮的状态prevState是什么？显然我们找一个最小的dp[prevState]然后加1，就可以得到最优的dp[state]。

我们知道prevState必然是state的子集。我们可以用暴力搜索所有它的子集，这里有一个比较高效的循环语句值得收藏：

for (int subset=state; subset>0; subset=(subset-1)&state)
这样得到的subset是比较高效的。

那么接下来我们就要判断这个subset对应的状态，是否能够通过新一轮的课程学习，达到state对应的状态。这里需要几个条件：

state的课程数目不能比subset的课程数目多余k。这可以用C++的内置函数来实现：
__builtin_popcount(state) - __builtin_popcount(subset) <= k
state的课程的先修课程，必须全部囊括在subset里面。也就是说，subset必须是state先修课程的超集。我们需要提前计算出state的先修课程集合prevState[state]，然后判断是否
prevState[state] & subset == prevState[state]
满足这两个条件的话，那么就说明subset是可以转移到state的。故有dp[state]=dp[subset]+1

此外，我们可以提前处理数据，计算所有状态的prevState。这个不难做到，只要将state的每一门课程的先修课程取并集即可。
"""
import functools
import itertools

import collections



class SolutionWisdomTLE:
    def minNumberOfSemesters(self, n: int, dependencies, k: int) -> int:
        dp = [float('inf')] * (1<<n)
        prevCourse = [0] * n
        prereq = [0] * (1<<n)

        for u, v in dependencies:
            prevCourse[v-1] += (1<<(u-1))

        for state in range(1<<n):
            prereq[state] = 0
            for i in range(n):
                if (state >> i)&1:
                    prereq[state] |= prevCourse[i]

        dp[0] = 0
        for state in range(1<<n):
            subset = state
            while subset >= 0:
                # (bin(state)[2:].count('1') - bin(subset)[2:].count('1')) <= k is condition 2 and (subset & prereq[state]) == prereq[state] is condition 2
                if (bin(state)[2:].count('1') - bin(subset)[2:].count('1')) <= k and (subset & prereq[state]) == prereq[state]:
                    dp[state] = min(dp[state], dp[subset] + 1)

                if subset == 0:
                    break
                subset = (subset-1) & state
        return dp[(1<<n) - 1]




class SolutionTLE2:
    def minNumberOfSemesters(self, n: int, dependencies, k: int) -> int:
        prereq = [0] * n
        for u, v in dependencies:
            prereq[v - 1] |= (1 << (u - 1))  # 利用或的关系记录所有的前置课程，prereq[j-1]的i-1位为1代表课程i为课程j的前置课程

        set_prereq = [0] * (1 << n)
        valid = [0] * (1 << n)  # 判断当前组合是否合法

        def countOne(n):  # 计算二进制数n有多少位是1
            count = 0
            while n > 0:
                n &= (n - 1)
                count += 1
            return count

        for mask in range(
                1 << n):  # 此段为筛选出所有可以使用k个课程的组合，讲所需的所有相关前置课程都存储在 set_prereq中，若所有前置课程和当前组合不存在重复，则当前组合合法（以防出现环），即可以在同一学期学完
            if countOne(mask) <= k:
                for i in range(n):
                    if mask & (1 << i):
                        set_prereq[mask] |= prereq[i]
                valid[mask] = (set_prereq[mask] & mask == 0)

        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            subset = mask
            while subset:  # 枚举所有的当前组合的子集，进行动态规划
                if valid[subset] and ((mask & set_prereq[subset]) == set_prereq[subset]):
                    dp[mask] = min(dp[mask], dp[mask ^ subset] + 1)  # 异或即除去当前子集的集合
                subset = (subset - 1) & mask  # 枚举子集

        return dp[(1 << n) - 1]  # (1 << n) -1 代表该二进制从1位到n位全部为1




"""
https://leetcode-cn.com/problems/parallel-courses-ii/solution/bfsxian-guo-by-sun-man-man/
"""


class SolutionBFS:
    def minNumberOfSemesters(self, n: int, dependencies, k: int) -> int:
        # table[i] 代表要完成 第i课，一定要完成的课程
        table = collections.defaultdict(int)
        for u, v in dependencies:
            table[v] |= (1 << u)

        queue = collections.deque()
        queue.append([0, 0])
        visited = set()
        visited.add(0)
        while queue:
            state, step = queue.popleft()
            # 因为没有第0 门课，所以是-2
            if state == (1 << (n + 1)) - 2:
                return step
            nextState = state
            for i in range(1, n + 1):
                # 完成了state之后，i课程可以完成
                if state & table[i] == table[i]:
                    nextState |= (1 << i)
            # 完成了state的课程，可以在下一天完成的课程
            subset = nextState ^ state
            # 如果下一天完成的课程<=k个，就全完成
            if bin(subset).count("1") <= k and state + subset not in visited:
                visited.add(state + subset)
                queue.append((state + subset, step + 1))
            else:
                # 如果多于k个，就选其中的k个来完成
                while subset:
                    if bin(subset).count('1') == k and state + subset not in visited:
                        visited.add(state + subset)
                        queue.append((state + subset, step + 1))
                    # 相当于找nextState ^ state的子集
                    subset = (subset - 1) & (nextState ^ state)





class SolutionTonyDP:
    def minNumberOfSemesters(self, n: int, dep, k: int) -> int:
        reqs = [0] * n
        for u, v in dep:
            reqs[v - 1] |= 1 << (u - 1)

        dp = [n] * (1 << n)
        dp[0] = 0
        for state in range(1 << n):
            # in state of current state,we should choose extra courses now.
            # so,check for all the available courses.
            avail = []
            for i in range(n):
                if state & (1 << i) == 0 and state & reqs[i] == reqs[i]:
                    avail.append(i)

            # state & (1<<v) tells which courses are not yet taken in state of state
            # state & reqs[v] tells if reqs[v] is a subset of courses taken.
            for choice in itertools.combinations(avail, min(k, len(avail))):
                newState = state  # courses taken
                for j in choice:
                    newState |= (1 << j)

                # now,we have newState = (courses taken in state + available courses)
                # now do the PUSH-DP work
                # since we are adding k new courses to the previous courses(state),we might endup taking a new semester => dp[state]+1
                # but dp[newState] might have been acheived in lesser semessters in another order i.e might have been reached newState
                # by another state. In that case,we dont want to increase the no of semesters we need.
                # so,we choose the minimum of either.
                dp[newState] = min(dp[newState], 1 + dp[state])

        # finally return how many min semesters it takes to take all courses i.e dp[(1<<n)-1] which is of form 0b111111
        return dp[-1]



class SolutionDFSBest:
    def minNumberOfSemesters(self, n, dependencies, k):
        table = [0] * n
        N = (1 << n) - 1

        for u, v in dependencies:
            table[v - 1] |= (1 << u - 1)

        def dp(state):
            if state in memo:
                return memo[state]

            if state == N:
                memo[state] = 0
                return 0

            can_study = []
            for i in range(n):
                if state & (1 << i):
                    continue  # alr learnt

                # check is i's prerequisites are already taken, if so, then we can take i
                if (table[i] & state) == table[i]:
                    can_study.append(i)
            # print can_study
            res = float('inf')
            for to_study in itertools.combinations(can_study, min(k, len(can_study))):
                newState = state
                for i in to_study:
                    newState |= 1 << i
                res = min(res, 1 + dp(newState))

            memo[state] = res
            return res

        memo = {}
        return dp(0)




class SolutionDFS2:
    def minNumberOfSemesters(self, n: int, dependencies, k: int) -> int:
        dep = {}  # 记录依赖于某节点的节点列表
        for a, b in dependencies:
            if a not in dep:
                dep[a] = []
            dep[a].append(b)

        @functools.lru_cache(typed=False, maxsize=128000000)
        def dp(stat):
            if stat == 0:
                return 0

            all_nodes = []
            for i in range(1, n + 1):
                if stat & (1 << i):  # 通过stat获取，当前考虑的所有课程（在不考虑依赖关系的情况下）
                    all_nodes.append(i)

            nodes = []
            dep_cnt = {node: 0 for node in all_nodes}
            for node in all_nodes:
                if node in dep:
                    for next in dep[node]:
                        if next in dep_cnt:
                            dep_cnt[next] += 1

            for node, cnt in dep_cnt.items():  # 筛选当前学期可供选择的所有课程
                if cnt == 0:
                    nodes.append(node)

            if len(nodes) <= k:  # 若课程数量小于k,则当前学期上所有的课程
                new_stat = stat
                for node in nodes:
                    new_stat &= ~(1 << node)  # 可用异或代替
                ans = 1 + dp(new_stat)
                return ans
            else:
                ans = float('inf')
                for combi in combinations(nodes, k):  # 枚举所有数量为k的子集
                    new_stat = stat
                    for node in combi:
                        new_stat &= ~(1 << node)
                    ans = min(ans, 1 + dp(new_stat))

                return ans

        return dp((1 << (n + 1)) - 2)  # 剪2是因为去掉最低向和最高项，因为此代码的循环是从1到n,最小左移为1，最大左移为n





