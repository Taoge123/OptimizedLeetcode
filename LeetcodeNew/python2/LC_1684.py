
class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:

        need = set(allowed)
        res = 0
        for word in words:
            if all(char in need for char in word):
                res += 1
        return res



