import collections
import functools


class SolutionMemo:
    def pyramidTransition(self, bottom: str, allowed):
        table = collections.defaultdict(set)
        for triangle in allowed:
            table[triangle[:2]].add(triangle[2])

        @functools.lru_cache(None)
        def dfs(base, top, i):
            # found it
            if len(base) == 1:
                return True
            # need to check the new line
            if i == len(base) - 1:
                return dfs(top, '', 0)

            node = base[i:i + 2]
            # if can't continue, return False
            if node not in table:
                return False

            for ch in table[node]:
                # If found a solution, return early
                if dfs(base, top + ch, i + 1):
                    return True

        return dfs(bottom, '', 0)




class Solution:
    def pyramidTransition(self, bottom: str, allowed) -> bool:
        table = collections.defaultdict(set)

        for s in allowed:
            pre = s[:2]
            table[pre].add(s[2:])
        return self.dfs(bottom, [], table, 1)

    def dfs(self, cur, nxt, table, i):
        if len(cur) == 1:
            return True

        if len(nxt) + 1 == len(cur):
            return self.dfs(nxt, [], table, 1)

        node = "".join(cur[i - 1:i + 1])
        for ch in table[node]:
            if self.dfs(cur, nxt + [ch], table, i + 1):
                return True
        return False



class SolutionHard:
    def pyramidTransition(self, bottom, allowed):
        table = collections.defaultdict(list)
        for nums in allowed:
            table[nums[:2]].append(nums[2])

        @functools.lru_cache(None)
        def dfs(base):
            if len(base) == 2 and base in table:
                return True
            options = []
            for i in range(len(base) - 1):
                if base[i:i + 2] in table:
                    options.append(table[base[i:i + 2]])
                else:
                    return False
            for bot in itertools.product(*options):
                if dfs(''.join(bot)):
                    return True
            return False

        return dfs(bottom)


