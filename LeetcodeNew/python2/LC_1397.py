class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        self.memo = {}
        self.lps = self.compute_LPS_arr(evil)
        return self.dfs(n, s1, s2, evil, 0, True, True, 0)

    def dfs(self, n, s1, s2, evil, index, pre1, pre2, pre_evil):
        if (index, pre1, pre2, pre_evil) in self.memo:
            return self.memo[(index, pre1, pre2, pre_evil)]

        if pre_evil == len(evil):
            self.memo[(index, pre1, pre2, pre_evil)] = 0
            return 0

        if index == n:
            self.memo[(index, pre1, pre2, pre_evil)] = 1
            return 1

        first = ord(s1[index]) if pre1 else ord('a')
        last = ord(s2[index]) if pre2 else ord('z')

        ans = 0
        for ci in range(first, last + 1):
            c = chr(ci)

            """        0123456789
                curr = aaabaaabaaaa
                              i

                       01234567
                evil = aaabaaaa
                 lps = 01201233
                              j
            """
            # update pre_evil using kmp
            j = pre_evil
            while j and c != evil[j]:
                j = self.lps[j - 1]
            if c == evil[j]:
                j += 1

            # update pre1 and pre2
            _pre1 = pre1 and ci == first
            _pre2 = pre2 and ci == last

            ans = (ans + self.dfs(n, s1, s2, evil, index + 1, _pre1, _pre2, j)) % (10 ** 9 + 7)

        self.memo[(index, pre1, pre2, pre_evil)] = ans
        return ans

    def compute_LPS_arr(self, pattern):
        M = len(pattern)
        lps = [0] * M
        i, j = 1, 0
        while i < M:
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps







