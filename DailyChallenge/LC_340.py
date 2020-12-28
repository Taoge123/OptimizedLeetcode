
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        start = 0
        res = 0

        for i, char in enumerate(s):

            count[char] += 1
            while len(count) > k:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    del count[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res
