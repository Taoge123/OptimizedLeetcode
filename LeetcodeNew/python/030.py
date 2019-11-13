import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        k = len(words[0])
        res = []

        for left in range(k):
            d = collections.Counter(words)

            for right in range(left + k, len(s) + 1, k):
                word = s[right - k: right]
                d[word] -= 1

                while d[word] < 0:
                    d[s[left:left + k]] += 1
                    left += k

                if left + k * len(words) == right:
                    res.append(left)
        return res

