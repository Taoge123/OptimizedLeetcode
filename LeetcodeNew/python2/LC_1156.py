"""
https://massivealgorithms.blogspot.com/2019/09/leetcode-1156-swap-for-longest-repeated.html


"""
import collections

class Solution:
    def maxRepOpt1(self, s: str) -> int:
        res = 0
        table = collections.Counter(s)
        count = collections.Counter()
        left = 0
        maxi = 0

        for right in range(len(s)):
            count[s[right]] += 1
            # maxi is the longest ch in this window
            maxi = max(maxi, count[s[right]])
            # window size - largest character > 1, means we need to flip it more than 1
            if right - left + 1 - maxi > 1:
                count[s[left]] -= 1
                left += 1
            # example: aaabaaa
            # if there are only 6 a
            # above code will return 7 by change b to a, we need to take the min count
            res = max(res, min(right - left + 1, table[s[right]]))
        return res




text = "ababa"
a = Solution()
print(a.maxRepOpt1(text))

class SolutionToBeModify:
    def maxRepOpt1(self, s: str) -> int:
        n = len(s)

        def dfs(i, k, prev):
            if i >= n:
                return 0

            keep = 0
            change = 0
            if s[i] == prev:
                keep = dfs(i + 1, k, prev) + 1
            else:
                if k == 1:
                    change = dfs(i + 1, k - 1, prev) + 1
            skip = dfs(i + 1, k, s[i])
            return max(keep, change, skip)

        return dfs(0, 1, '#')
