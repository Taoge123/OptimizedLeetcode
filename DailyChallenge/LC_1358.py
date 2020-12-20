

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        res = 0
        left = 0
        count = collections.Counter()

        for right in range(len(s)):
            count[s[right]] += 1
            while all(count[c] > 0 for c in 'abc'):
                count[s[left]] -= 1
                left += 1
            res += left
        return res


