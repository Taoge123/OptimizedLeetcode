
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





