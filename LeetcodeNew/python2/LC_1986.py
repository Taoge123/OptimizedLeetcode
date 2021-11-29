"""
https://www.youtube.com/watch?v=8TU3WceDlzI

"""



import functools


class SolutionTony1:  # 11111 ---> 00000, subset
    def minSessions(self, tasks, sessionTime):
        # pre-processing: for loop each state to get the hours needed for finishing tasks under the state -- > timeNeed
        # for loop each state to see if timeNeed < sessionTime, res +1, get min res

        n = len(tasks)
        timeNeed = [0] * (1 << n)
        for state in range(1 << n):
            for i in range(n):
                if state & (1 << i):
                    timeNeed[state] += tasks[i]

        @functools.lru_cache(None)
        def dfs(state):
            if state == 0:
                return 0

            res = float('inf')
            substate = state
            while substate:
                if timeNeed[substate] <= sessionTime:
                    res = min(res, dfs(state ^ substate) + 1)
                substate = (substate - 1) & state

            return res

        return dfs((1 << n) - 1)



class SolutionTony2:
    def minSessions(self, tasks, sessionTime):
        if sum(tasks) <= sessionTime:
            return 1
        n = len(tasks)

        @functools.lru_cache(None)
        def dfs(state, remainTime):
            if state == (1 << n) - 1:
                return 0
            res = float('inf')
            if remainTime != sessionTime:
                res = dfs(state, sessionTime) + 1

            for i, time in enumerate(tasks):
                if remainTime >= time and (state & (1 << i)) == 0:
                    res = min(res, dfs(state | (1 << i), remainTime - time))

            return res

        return dfs(0, 0)


class SolutionSlow:
    def minSessions(self, tasks, sessionTime):

        n = len(tasks)
        full_mask = (1 << n) - 1

        @functools.lru_cache(None)
        def dfs(mask, remainTime):
            if mask == full_mask:
                return 0

            res = float('inf')
            for i in range(n):
                if mask & (1 << i) == 0:
                    if tasks[i] <= remainTime:
                        res = min(res, dfs(mask | (1 << i), remainTime - tasks[i]))
                    else:
                        res = min(res, 1 + dfs(mask | (1 << i), sessionTime - tasks[i]))

            return res

        return dfs(0, 0)



class Solution1:  # 11111 ---> 00000, subset
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # pre-processing: for loop each state to get the hours needed for finishing tasks under the state -- > timeNeed
        # for loop each state to see if timeNeed < sessionTime, res +1, get min res

        n = len(tasks)
        timeNeed = [0] * (1 << n)
        for state in range(1 << n):
            for i in range(n):
                if state & (1 << i):
                    timeNeed[state] += tasks[i]

        memo = {}
        return self.dfs(timeNeed, sessionTime, (1 << n) - 1, memo)

    def dfs(self, timeNeed, sessionTime, state, memo):
        if state in memo:
            return memo[state]

        if state == 0:
            return 0

        res = float('inf')
        substate = state
        while substate:
            if timeNeed[substate] <= sessionTime:
                res = min(res, self.dfs(timeNeed, sessionTime, state ^ substate, memo) + 1)
            substate = (substate - 1) & state

        memo[state] = res
        return memo[state]


class Solution2:  # TLE  0000 --> 111
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        if sum(tasks) <= sessionTime:
            return 1
        n = len(tasks)
        timeNeed = [0] * (1 << n)
        for state in range(1 << n):
            for i in range(n):
                if state & (1 << i):
                    timeNeed[state] += tasks[i]

        memo = {}
        return self.dfs(n, timeNeed, sessionTime, 0, memo)

    def dfs(self, n, timeNeed, sessionTime, state, memo):
        if state in memo:
            return memo[state]

        if state == (1 << n) - 1:
            return 0

        res = float('inf')
        for nxtstate in range((1 << n) - 1, state, -1):
            if nxtstate == state or nxtstate & state != state:
                continue
            if timeNeed[nxtstate] - timeNeed[state] <= sessionTime:
                res = min(res, self.dfs(n, timeNeed, sessionTime, nxtstate, memo) + 1)

        memo[state] = res
        return memo[state]


class Solution:
    def minSessions(self, tasks, sessionTime):
        if sum(tasks) <= sessionTime:
            return 1
        n = len(tasks)

        memo = {}
        return self.dfs(n, tasks, sessionTime, 0, 0, memo)

    def dfs(self, n, tasks, sessionTime, state, remainTime, memo):
        if (remainTime, state) in memo:
            return memo[(remainTime, state)]

        if state == (1 << n) - 1:
            return 0
        res = float('inf')
        if remainTime != sessionTime:
            res = self.dfs(n, tasks, sessionTime, state, sessionTime, memo) + 1

        for i, time in enumerate(tasks):
            if remainTime >= time and (state & (1 << i)) == 0:
                res = min(res, self.dfs(n, tasks, sessionTime, state | (1 << i), remainTime - time, memo))

        memo[(remainTime, state)] = res
        return memo[(remainTime, state)]

