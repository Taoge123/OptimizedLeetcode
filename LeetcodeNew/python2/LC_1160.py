import collections


class Solution:
    def countCharacters(self, words, chars: str) -> int:
        count = collections.Counter(chars)
        res = 0
        for word in words:
            w = collections.Counter(word)
            if w == w & count:
                res += len(word)
        return res


