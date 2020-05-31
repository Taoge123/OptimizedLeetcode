"""
https://massivealgorithms.blogspot.com/2019/09/leetcode-1156-swap-for-longest-repeated.html


"""
import collections

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        res = 0
        table = collections.Counter(text)
        count = collections.Counter()
        left = 0
        maxi = 0

        for right in range(len(text)):
            count[text[right]] += 1
            maxi = max(maxi, count[text[right]])
            if right - left + 1 - maxi > 1:
                count[text[left]] -= 1
                left += 1
            res = max(res, min(right - left + 1, table[text[right]]))
        return res





