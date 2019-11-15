
# class Solution:
#     def combine(self, n, k):
#         res = []
#         self.backtrack(n, k, 0, [], res)
#         return res
#
#     def backtrack(self, n, k, index, path, res):
#
#         if len(path) == k:
#             res.append(path)
#             return
#
#         for i in range(index+1, n+1):
#             self.backtrack(n, k, i, path + [i], res)

class Solution:
    def combine(self, n, k):

        res = []
        self.backtrack(n, k, 1, [], res)
        return res

    def backtrack(self, n, k, index, path, res):
        if len(path) == k:
            res.append(path[:])
        for i in range(index, n + 1):
            path.append(i)
            self.backtrack(n, k, i + 1, path, res)
            path.pop()





