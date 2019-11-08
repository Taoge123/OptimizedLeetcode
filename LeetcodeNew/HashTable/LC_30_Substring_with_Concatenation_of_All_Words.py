import collections

class Solution:
    def findSubstring(self, s: str, words):
        if not words: return []
        k = len(words[0])
        res = []

        for left in range(k):
            table = collections.Counter(words)

            for right in range(left + k, len(s) + 1, k):
                word = s[right - k: right]
                table[word] -= 1

                while table[word] < 0:
                    table[s[left:left + k]] += 1
                    left += k

                if left + k * len(words) == right:
                    res.append(left)
        return res









