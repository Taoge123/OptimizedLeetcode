
class Solution:
    def camelMatch(self, queries, pattern: str):
        res = []
        for query in queries:
            res.append(self.isMatch(query, pattern))
        return res


    def isMatch(self, query, pattern):
        i = 0
        for char in query:
            if i < len(pattern) and char == pattern[i]:
                i += 1
            elif char.isupper():
                return False

        return i == len(pattern)

