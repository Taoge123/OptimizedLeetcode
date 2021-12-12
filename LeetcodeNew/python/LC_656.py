
import functools


class SolutionMemo:
    def cheapestJump(self, nums, maxJump):
        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i):
            if nums[i - 1] == -1:
                return float('inf'), []
            if i == n:
                return nums[i - 1], [i]
            final_cost, final_path = float('inf'), []
            for j in range(i + 1, min(i + maxJump, n) + 1):
                cost, path = dfs(j)
                if cost + nums[i - 1] < final_cost:
                    final_cost = nums[i - 1] + cost
                    final_path = [i] + path
            if final_cost == float('inf'):
                return [float('inf'), []]
            else:
                return [final_cost, final_path]

        return dfs(1)[1]



class SolutionMemo2:
    def cheapestJump(self, nums, maxJump):
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i):
            if nums[i - 1] == -1:
                return float('inf'), []
            if i == n:
                return nums[i - 1], [i]
            final_cost, final_path = float('inf'), []
            for j in range(i + 1, min(i + maxJump, n) + 1):
                cost, path = dfs(j)
                if cost < final_cost:
                    final_cost = cost
                    final_path = path
            if final_cost == float('inf'):
                return [float('inf'), []]
            else:
                return [nums[i - 1] + final_cost, [i] + final_path]

        return dfs(1)[1]


class Solution:
    def cheapestJump(self, A, B: int):
        n = len(A)
        next_pos = [-1] * n

        @functools.lru_cache(None)
        def dfs(i):
            if i == n - 1 and A[i] >= 0:
                return A[i]

            res = float('inf')
            for j in range(i + 1, min(i + B, n - 1) + 1):
                if A[j] >= 0:
                    cost = A[i] + dfs(j)
                    if cost < res:
                        res = cost
                        next_pos[i] = j
            return res

        dfs(0)
        i = 0
        res = []
        while i < n and next_pos[i] > 0:
            res.append(i + 1)
            i = next_pos[i]
        if i == n - 1 and A[i] >= 0:
            res.append(n)
        else:
            return []
        return res



class SolutionTonyIncorrect:
    def cheapestJump(self, A, B: int):
        n = len(A)
        next_pos = [-1] * n

        @functools.lru_cache(None)
        def dfs(i):
            if i == n - 1 and A[i] >= 0:
                return A[i], i

            final_cost = float('inf')
            final_path = []
            for j in range(i + 1, min(i + B, n - 1) + 1):
                if A[j] >= 0:
                    cost, path = dfs(j)
                    if cost + A[i] < final_cost:
                        final_cost = cost + A[i]
                        final_path += [j]
            return final_cost, final_path

        final_cost, final_path = dfs(0)
        return final_path



class SolutionDFS:
    def cheapestJump(self, A, B: int):
        n = len(A)
        pos = [-1] * n
        memo = {}
        self.dfs(A, B, 0, pos, memo)
        i = 0
        res = []
        while i < n and pos[i] > 0:
            res.append(i + 1)
            i = pos[i]
        if i == n - 1 and A[i] >= 0:
            res.append(n)
        else:
            return []
        return res

    def dfs(self, A, B, i, pos, memo):
        n = len(A)
        if i in memo and memo[i] > 0:
            return memo[i]

        if i == n - 1 and A[i] >= 0:
            return A[i]

        res = float('inf')
        for j in range(i + 1, min(i + B, n - 1) + 1):
            if A[j] >= 0:
                cost = A[i] + self.dfs(A, B, j, pos, memo)
                if cost < res:
                    res = cost
                    pos[i] = j

        memo[i] = res
        return res




class Solution:
    def cheapestJump(self, A, B: int):
        if A[-1] == -1:
            return []

        n = len(A)
        pos = [-1] * n
        dp = [float('inf')] * n

        dp[-1] = A[-1]

        for i in range( n -2, -1, -1):
            if A[i] == -1:
                continue

            for j in range( i +1, min( i +B, n- 1) + 1):
                if dp[j] == float('inf'):
                    continue
                if A[i] + dp[j] < dp[i]:
                    dp[i] = A[i] + dp[j]
                    pos[i] = j

        if dp[0] == float('inf'):
            return []

        res = []
        i = 0

        while i != -1:
            res.append(i + 1)
            i = pos[i]
        return res



