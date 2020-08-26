
"""
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)



Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""


Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
"""

import collections

class SolutionTLE:
    def longestDupSubstring(self, S):
        left, right = 0, len(S) - 1
        res = ''

        while left < right:
            mid = (left + right) // 2
            temp = self.check(mid, S)
            if not temp:
                right = mid
            else:
                left = mid + 1
                res = temp
        return res

    def check(self, num, S):
        visited = set()
        for i in range(len(S) - num + 1):
            if S[i:i+num] in visited:
                return S[i: i+num]
            visited.add(S[i: i+num])
        return None




class Solution:
    def longestDupSubstring(self, s: str) -> str:
        left, right = 0, len(s)
        res = ''

        while left < right:
            mid = left + (right - left) // 2
            temp = self.check(s, mid)

            if not temp:
                right = mid
            else:
                res = temp
                left = mid + 1

        return res


    def check(self, s, k):
        MOD = (1 << 61) - 1
        BASE = 26
        D = pow(BASE, k - 1, MOD)
        chash = 0
        visited = collections.defaultdict(list)

        for i in range(len(s)):
            if i >= k:
                l_chval = ord(s[i - k]) - ord('a')
                chash = (chash - l_chval * D) % MOD

            chval = ord(s[i]) - ord('a')
            chash = (chash * BASE + chval) % MOD

            if i >= k - 1:
                if chash in visited:
                    substr_i = s[i - k + 1:i + 1]
                    for j in visited[chash]:
                        substr_j = s[j - k + 1:j + 1]
                        if substr_i == substr_j:
                            return substr_i

                visited[chash].append(i)

        return ''


"""
ban: (1 * 26^2 + 0 * 26^1 + 13 * 26^0) % 31 = 7
ana: (0 * 26^2 + 13 * 26^1 + 0 * 26^0) % 31 = 28
nan: (13 * 26^2 + 0 * 26^1 + 13 * 26^0) % 31 = 28
ana: (0 * 26^2 + 13 * 26^1 + 0 * 26^0) % 31 = 28


ban for example：
i = 0 : b
hash_ = 0 * 26 + num[i] = 1
i = 1 : a
hash_ = 1 * 26 + nums[i] = 26 
i = 2 : n
hash_ = 26 * 26 + nums[i] = 39

aL = 26 * mid (18)

xxxxxxxxxxxxxxxxxxxxxx
 s         start+mid-1
  
"""


class SolutionOfficial:

    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        self.nums = [ord(S[i]) - ord('a') for i in range(n)]

        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if self.search(S, mid) != -1:
                left = mid + 1
            else:
                right = mid - 1

        start = self.search(S, left - 1)
        return S[start: start + left - 1]

    def search(self, S, len_):
        n = len(S)
        base = 26
        MOD = 2 ** 32

        # compute the hash of string S[:mid]
        hash_ = 0
        for i in range(len_):
            hash_ = (hash_ * base + self.nums[i]) % MOD

        # already visited hashes of strings of length mid
        visited = {hash_}
        # const value to be used often : a**mid % mod
        for start in range(1, n - len_ + 1):
            # compute rolling hash in O(1) time
            hash_ = (hash_ * base - self.nums[start - 1] * pow(base, len_, MOD) + self.nums[start + len_ - 1]) % MOD
            if hash_ in visited:
                return start
            visited.add(hash_)
        return -1


S = "bababababbababababbababbanannababbab"
a = SolutionOfficial()
print(a.longestDupSubstring(S))


