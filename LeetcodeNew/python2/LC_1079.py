"""
491 https://leetcode.com/problems/increasing-subsequences/

"""

import itertools
import collections


class SolutionRika:
    def numTilePossibilities(self, tiles: str) -> int:
        # subset + permutation
        res = []
        tiles = sorted(list(tiles))
        tiles = ''.join(tiles)
        self.dfs(tiles, "", res)
        return len(res) - 1

    def dfs(self, s, path, res):
        res.append(path)
        visited = set()
        for i in range(len(s)):
            if s[i] in visited:
                continue
            visited.add(s[i])
            self.dfs(s[:i] + s[i + 1:], path + s[i], res)



class SolutionRika2:
    def numTilePossibilities(self, tiles: str) -> int:
        # subset + permutation

        self.res = 0
        tiles = sorted(list(tiles))
        tiles = ''.join(tiles)
        self.dfs(tiles)
        return self.res - 1

    def dfs(self, s):

        self.res += 1

        visited = set()
        for i in range(len(s)):
            if s[i] in visited:
                continue
            visited.add(s[i])
            self.dfs(s[:i] + s[i + 1:])


class Solution3:
    def numTilePossibilities(self, tiles: str) -> int:
        # subset + permutation

        self.res = 0
        tiles = sorted(list(tiles))
        tiles = ''.join(tiles)
        self.dfs(tiles, set())
        return self.res - 1

    def dfs(self, s, used):

        self.res += 1

        visited = set()
        for i in range(len(s)):
            if s[i] in visited:
                continue
            if i in used:
                continue
            visited.add(s[i])
            used.add(i)
            self.dfs(s, used)
            used.remove(i)


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len({s[:i] for s in itertools.permutations(tiles) for i in range(8)}) - 1


class Solution2:
    def numTilePossibilities(self, tiles: str) -> int:
        count = collections.Counter(tiles)
        return self.dfs(count)

    def dfs(self, count):
        summ = 0
        for i in count.keys():
            if count[i] == 0:
                continue

            count[i] -= 1
            summ += 1
            summ += self.dfs(count)
            count[i] += 1

        return summ


"""
math permutation problem.
overall number=sum(all possible frequency case for each letters)=sum(num(f1,f2,....,fn))
num(f1,f2,...fn)=(f1+f2+...fn)!/f1!f2!...*fn!
fi=0 to fre_of_letter,when fre==0, since 0!==1, thus formula is also good.
"""


class Solution2:
    def numTilePossibilities(self, tiles):
        pos = self.dfs(tiles, "", set())
        return len(pos)

    def dfs(self, tiles, path, res):
        if not tiles:
            return res

        for i, tile in enumerate(tiles):
            temp = path + tile
            res.add(temp)
            self.dfs(tiles[:i] + tiles[i + 1:], temp, res)

        return res




# class Solution:
#     def numTilePossibilities(self, tiles):
#         res = set()
#
#         self.helper(tiles, "", res)
#         return len(res) - 1
#
#     def helper(self, pos, path, res):
#         if len(pos) == 0:
#             res.add(path)
#             return
#         for i in range(len(pos)):
#             self.helper(pos[:i] + pos[i + 1:], path + pos[i], res)
#         self.helper(pos[1:], path, res)
#
#




