import collections

class Solution:
    def minStickers(self, stickers, target: str) -> int:
        n = len(target)
        N = (1 << n)
        dp = [float('inf') for i in range(N)]
        dp[0] = 0
        for i in range(N):
            if dp[i] == float('inf'):
                continue
            for word in stickers:
                # 状态 j + word 得到状态 i
                j = self.findNextState(i, word, target)
                dp[j] = min(dp[j], dp[i] + 1)

        if dp[N - 1] == float('inf'):
            return -1
        else:
            return dp[N - 1]

    def findNextState(self, state, word, target):
        n = len(target)
        for char in word:
            for k in range(n):
                # 如果state的第k位是空的, char可以填补上
                if ((state >> k) & 1) == 0 and target[k] == char:
                    state += (1 << k)
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


