"""
https://leetcode.com/problems/stickers-to-spell-word/discuss/743124/DP-example-with-intuitive-figures-explanation-python-code

1125

691.Stickers-to-Spell-Word
设置状态数组dp[i],dp的大小是 N = 2^n, 其中n是target的大小。怎么理解？将dp的索引i进行二进制拆解，
i的每一个bit表示的是target对应位置的字符是否得到了满足。比如n=3时，dp数组的大小N=8，
对应的状态有 000,001,010,011,100,101,110,111. 举个例子，i=3 (即011)表示target的末两位的字符得到了满足，
但第一位的字符还没有得到满足。dp[i]表示在状态i下，需要的sticker的最少数目。

注意：这种状态的排列有一个非常好的性质。任何状态，只可能由位于其前面的状态转移得到，不可能从后面的状态转移得到。
比如i=3(即 011)这个状态，只可能从i=0,1,2转移过来（通过使用某些合适的sticker）；再比如i=4(即100)这个状态，只可能从i=0转移过来。
这种状态转移的性质，非常适合dp根据i从前往后的遍历。

所以，dp的大循环就是 for (i=0; i<n; i++). 对于该状态i，我们尝试每一个sticker[k]，
计算状态i经过sticker[k]的帮助后得到的状态j（注意已经分析过j肯定是大于i的），
那么dp[j]就可以得到更新dp[j]=min(dp[j], dp[i]+1) if dp[j]!=-1

所有的状态i都遍历过之后，答案的输出就是 dp[N-1]

"""

import collections
import functools



class SolutionDFSShort:
    def minStickers(self, stickers, target: str) -> int:

        table = collections.Counter(target)
        self.res = float('inf')

        def dfs(target, i, count):
            n = len(target)
            if i == n:
                self.res = min(self.res, count)
                return

            if self.res == count:
                return

            if table[target[i]] <= 0:
                dfs(target, i + 1, count)
            else:
                for stick in stickers:
                    if target[i] in stick:
                        for s in stick:
                            table[s] -= 1
                        dfs(target, i + 1, count + 1)
                        for s in stick:
                            table[s] += 1

        dfs(target, 0, 0)
        return self.res if self.res < float('inf') else -1



# --> backtracking --> updated needs in original needs
class SolutionRika:
    def minStickers(self, stickers, target: str) -> int:
        # pre-processing
        counts = []
        for i, sticker in enumerate(stickers):
            sticker_count = collections.Counter(sticker)
            counts.append(sticker_count)

        self.res = float('inf')

        @functools.lru_cache(None)
        def dfs(target, count):
            needs = collections.Counter(target)
            if not needs:
                self.res = min(self.res, count)
                return

            for i in range(len(counts)):
                new_target = ''
                valid_sticker = False
                for char in needs.keys():
                    if char in counts[i]:
                        valid_sticker = True
                        if counts[i][char] < needs[char]:
                            new_target += (char * (needs[char] - counts[i][char]))
                    else:
                        new_target += (char * needs[char])

                if not valid_sticker:
                    continue
                if valid_sticker:
                    dfs(new_target, count + 1)

        dfs(target, 0)
        return self.res if self.res < float('inf') else -1



class SolutionMemoBitMask:
    def minStickers(self, stickers, target):
        n = len(target)
        state = (1 << n) - 1

        @functools.lru_cache(None)
        def dfs(state):
            if state == 0:
                return 0

            x = 0
            while (1 << x) & state == 0:
                x += 1

            first_ch = target[x]

            res = -1
            for word in stickers:
                count = collections.Counter(word)
                if first_ch not in count:
                    # 每次只选包含边界上字符的单词，缩减枚举量，避免出现 stat1, stat2, stat3 和 stat2 stat1 stat3 这样的等效序列
                    # 有了这个剪枝条件，性能提升了10倍
                    continue

                newState = state
                for i in range(len(target)):
                    if newState & (1 << i) and target[i] in count and count[target[i]] > 0:
                        count[target[i]] -= 1
                        newState &= ~(1 << i)

                    if newState != state:
                        val = dfs(newState)
                        if val != -1 and (res == -1 or 1 + val < res):
                            res = val + 1
            return res

        return dfs(state)



class SolutionDFS:
    def minStickers(self, stickers, target: str) -> int:

        table = collections.Counter(target)
        self.res = float('inf')
        self.dfs(stickers, target, 0, 0, table)
        return self.res if self.res < float('inf') else -1

    def dfs(self, stickers, target, pos, count, table):
        n = len(target)
        if pos == n:
            self.res = min(self.res, count)
            return

        if self.res == count:
            return

        if table[target[pos]] <= 0:
            self.dfs(stickers, target, pos + 1, count, table)
        else:
            for stick in stickers:
                if target[pos] in stick:
                    for s in stick:
                        table[s] -= 1
                    self.dfs(stickers, target, pos + 1, count + 1, table)
                    for s in stick:
                        table[s] += 1



#really fast
class SolutionTonyBFS:
    def minStickers(self, stickers, target: str) -> int:
        n = len(target)
        N = (1 << n) - 1
        table = collections.defaultdict(list)
        for i in range(n):
            table[target[i]].append(i)

        queue = collections.deque()
        queue.append([0, 0])
        visited = set()
        while queue:
            state, step = queue.popleft()
            if state == N:
                return step

            for sticker in stickers:
                newState = state
                for ch in sticker:
                    if ch not in table:
                        continue
                    for i in table[ch]:
                        # print(bin(newState), newState, 1<<i)
                        if not newState & (1 << i):
                            newState |= (1 << i)
                            break
                if newState in visited:
                    continue
                visited.add(newState)
                queue.append([newState, step + 1])
        return -1



class SolutionDP:
    def minStickers(self, stickers, target):
        n = len(target)
        N = (1 << n)
        dp = [float('inf') for i in range(N)]
        dp[0] = 0
        for i in range(N):
            if dp[i] == float('inf'):
                continue
            for sticker in stickers:
                # 状态 j + word 得到状态 i
                j = self.findNextState(i, sticker, target)
                dp[j] = min(dp[j], dp[i] + 1)

        if dp[N - 1] == float('inf'):
            return -1
        else:
            return dp[N - 1]

    def findNextState(self, state, sticker, target):
        n = len(target)
        for s in sticker:
            for k in range(n):
                # 如果state的第k位是空的, char可以填补上
                if ((state >> k) & 1) == 0 and target[k] == s:
                    state += (1 << k)
                    # state |= (1 << k)
                    break
        return state





class SolutionDFS:
    def minStickers(self, stickers, target: str) -> int:

        table = collections.Counter(target)
        self.res = float('inf')
        self.dfs(stickers, target, 0, 0, table)
        return self.res if self.res < float('inf') else -1

    def dfs(self, stickers, target, pos, count, table):
        n = len(target)
        if pos == n:
            self.res = min(self.res, count)
            return

        if self.res == count:
            return

        if table[target[pos]] <= 0:
            self.dfs(stickers, target, pos + 1, count, table)
        else:
            for stick in stickers:
                if target[pos] in stick:
                    for s in stick:
                        table[s] -= 1
                    self.dfs(stickers, target, pos + 1, count + 1, table)
                    for s in stick:
                        table[s] += 1


class SolutionTonyBFS:
    def minStickers(self, stickers, target: str) -> int:
        n = len(target)
        N = (1 << n) - 1
        table = collections.defaultdict(list)
        for i in range(n):
            table[target[i]].append(i)

        queue = collections.deque()
        queue.append([0, 0])
        visited = set()
        while queue:
            state, step = queue.popleft()
            if state == N:
                return step

            for sticker in stickers:
                newState = state
                for ch in sticker:
                    if ch not in table:
                        continue
                    for i in table[ch]:
                        # print(bin(newState), newState, 1<<i)
                        if not newState & (1 << i):
                            newState |= (1 << i)
                            break
                if newState in visited:
                    continue
                visited.add(newState)
                queue.append([newState, step + 1])
        return -1






class SolutionBFS:
    def minStickers(self, stickers, target):
        table = collections.defaultdict(list)
        n = len(target)
        N = (1 << n) - 1
        for i in range(n):
            table[target[i]].append(i)

        queue = collections.deque()
        queue.append([0, 0])
        visited = set()
        while queue:
            state, step = queue.popleft()
            if state == N:
                return step
            if state in visited:
                continue

            visited.add(state)
            for sticker in stickers:
                newState = self.apply(sticker, state, table)
                queue.append([newState, step + 1])

        return -1

    def apply(self, sticker, state, table):
        for s in sticker:
            if s not in table:
                continue
            for i in table[s]:
                if not state & (1 << i):
                    state |= (1 << i)
                    break
        return state




