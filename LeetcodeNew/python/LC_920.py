
"""
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


class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(i, count):
            if i == L:
                return count == N

            # we already used count songs, we can replay a song if k other songs were played
            res = dfs(i + 1, count) * max(0, count - K)
            # (n - count) is how many songs that we haven't used yet
            res += dfs(i + 1, count + 1) * (N - count)

            return res % mod

        return dfs(0, 0)



