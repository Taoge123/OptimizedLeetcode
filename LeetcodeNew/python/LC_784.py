
import collections

class Solution:
    def letterCasePermutation(self, S):
        res = []
        self.helper(S, "", res)
        return res

    def helper(self, s, path, res):
        if not s:
            res.append(path)
            return

        if s[0].isdigit():
            self.helper(s[1:], path + s[0], res)
        else:
            self.helper(s[1:], path + s[0].lower(), res)
            self.helper(s[1:], path + s[0].upper(), res)




class SolutionBFS:
    def letterCasePermutation(self, S: str):
        if not S or len(S) == 0:
            return []

        queue = collections.deque()
        queue.append(S)

        for i in range(len(S)):
            if S[i].isdigit():
                continue
            size = len(queue)
            for j in range(size):
                cur = queue.popleft()
                node = list(cur)
                node[i] = node[i].lower()
                queue.append("".join(node))

                node[i] = node[i].upper()
                queue.append("".join(node))

        return queue

