"""
https://www.youtube.com/watch?v=8TU3WceDlzI

"""



import functools

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




