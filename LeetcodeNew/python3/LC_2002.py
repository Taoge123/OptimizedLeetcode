
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)

        def isPal(word):
            i, j = 0, len(word ) -1
            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True
        def dfs(i, w1, w2):
            if i >= n:
                if isPal(w1) and isPal(w2):
                    self.res = max(self.res, len(w1) + len(w2))
                return

            dfs( i +1, w1, w2)
            dfs( i +1, w1 + s[i], w2)
            dfs( i +1, w1, w2 + s[i])

        self.res = 0
        dfs(0, "", "")
        return self.res



