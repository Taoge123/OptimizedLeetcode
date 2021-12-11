
"""
https://buptwc.github.io/2018/10/08/Leetcode-920-Number-of-Music-Playlists/
https://leetcode.com/problems/number-of-music-playlists/discuss/1579179/Python-or-Top-Down-DP-or-Well-Commented-and-easy-to-understand
len, count

option 1: pick one of the already used song
    (len+1, count) * max(0, count - K)
option 2: pick one of the already unused song
    (len+1, count+1) * (N - count)


length =
count = number of unique songs

https://www.youtube.com/watch?v=uvjn6UDXVrY

"""

import functools


class SolutionMemo:  # super fast
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # 建一个播放清单，总共n首歌，要播放goal首歌，每播放不同的k首歌才能重播播放前面的歌， 求有几种方式建立播放清单
        # 每首歌都需要播放至少一次，可以重复播放
        # goal >= n
        # length + unique
        # TWO CASES: add new song or add repeat song
        mod = 10 ** 9 + 7
        @functools.lru_cache(None)
        def dfs(count, unique):
            if count == goal:
                if unique == n:
                    return 1
                else:
                    return 0

            add_new = dfs(count + 1, unique + 1) * (n - unique)

            add_repeat = 0
            if unique > k:
                add_repeat = dfs(count + 1, unique) * (unique - k)

            return (add_new + add_repeat) % mod

        return dfs(0, 0)



class SolutionMemoSlow:  # slow
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # 建一个播放清单，总共n首歌，要播放goal首歌，每播放不同的k首歌才能重播播放前面的歌， 求有几种方式建立播放清单
        # 每首歌都需要播放至少一次，可以重复播放
        # goal >= n
        # length + unique
        # TWO CASES: add new song or add repeat song
        mod = 10 ** 9 + 7
        @functools.lru_cache(None)
        def dfs(count, unique):

            if count == goal:
                return unique == n
                #     return 1
                # else:
                #     return 0

            # not_repeat songs --> add new song from the remaining songs (n - unique)
            add_new = dfs(count + 1, unique + 1) * (n - unique)

            # repeat songs --> add repeat song from the selected sings (unique - k) --> must meet k criterial
            add_repeat = dfs(count + 1, unique) * max(0, unique - k)

            return (add_new + add_repeat) % mod

        return dfs(0, 0)




class SolutionRika1:  # slow
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # 建一个播放清单，总共n首歌，要播放goal首歌，每播放不同的k首歌才能重播播放前面的歌， 求有几种方式建立播放清单
        # 每首歌都需要播放至少一次，可以重复播放
        # goal >= n
        # length + unique
        # TWO CASES: add new song or add repeat song
        memo = {}
        return self.dfs(n, goal, k, 0, 0, memo)

    def dfs(self, n, goal, k, count, unique, memo):
        if (count, unique) in memo:
            return memo[(count, unique)]

        if count == goal:
            if unique == n:
                return 1
            else:
                return 0

        mod = 10 ** 9 + 7

        # not_repeat songs --> add new song from the remaining songs (n - unique)
        add_new = self.dfs(n, goal, k, count + 1, unique + 1, memo) * (n - unique)

        # repeat songs --> add repeat song from the selected sings (unique - k) --> must meet k criterial
        add_repeat = self.dfs(n, goal, k, count + 1, unique, memo) * max(0, unique - k)

        memo[(count, unique)] = (add_new + add_repeat) % mod
        return memo[(count, unique)]


class SolutionRika2:  # super fast
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # 建一个播放清单，总共n首歌，要播放goal首歌，每播放不同的k首歌才能重播播放前面的歌， 求有几种方式建立播放清单
        # 每首歌都需要播放至少一次，可以重复播放
        # goal >= n
        # length + unique
        # TWO CASES: add new song or add repeat song
        memo = {}
        return self.dfs(n, goal, k, 0, 0, memo)

    def dfs(self, n, goal, k, count, unique, memo):
        if (count, unique) in memo:
            return memo[(count, unique)]

        if count == goal:
            if unique == n:
                return 1
            else:
                return 0

        mod = 10 ** 9 + 7

        add_new = self.dfs(n, goal, k, count + 1, unique + 1, memo) * (n - unique)

        add_repeat = 0
        if unique > k:
            add_repeat = self.dfs(n, goal, k, count + 1, unique, memo) * (unique - k)

        memo[(count, unique)] = (add_new + add_repeat) % mod
        return memo[(count, unique)]


