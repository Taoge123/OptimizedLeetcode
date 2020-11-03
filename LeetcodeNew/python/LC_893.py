class Solution:
    def numSpecialEquivGroups(self, A) -> int:
        def count(A):
            table = [0] * 52
            for i, ch in enumerate(A):
                table[ord(ch) - ord('a') + 26 * (i % 2)] += 1
            return tuple(table)

        res = set()
        for word in A:
            res.add(count(word))
        return len(res)


