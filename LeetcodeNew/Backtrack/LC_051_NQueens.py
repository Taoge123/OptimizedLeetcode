

class Solution:

    def solveNQueens(self, n):
        res = []
        self.dfs([-1] * n, 0, [], res)
        return res

    # nums is a one-dimension array, like [1, 3, 0, 2] means
    # first queen is placed in column 1, second queen is placed
    # in column 3, etc.
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return  # backtracking
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):  # pruning
                tmp = "." * len(nums)
                self.dfs(nums, index + 1, path + [tmp[:i] + "Q" + tmp[i + 1:]], res)

    # check whether nth queen can be placed in that column
    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True

class Solution2:
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            """
            temp = [["." * i + "Q" + "." * (n - i - 1) for i in queens]]
            for t in temp:
                for tt in t:
                    print(tt)
                print("\n")
            print("\n")
            """

            p = len(queens) # p is the index of row
            if p == n:
                result.append(queens)
                return None
            for q in range(n): # q is the index of col
                # queens stores those used cols, for example, [0,2,4,1] means these cols have been used
                # xy_dif is the diagonal 1
                # xy_sum is the diagonal 2
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


class Solution3:
    def solveNQueens(self, n):
        """
        :param n:
        :return:
        """
        res = []
        def dfs(queens, ddiff, ssum):
            p = len(queens)
            if p == n:
                queens = ['.' * i + 'Q' + '.' * (n - 1 - i) for i in queens]
                res.append(queens)
                return
            for q in range(n):
                if q in queens or p - q in ddiff or p + q in ssum: continue
                dfs(queens + [q],
                    ddiff + [p - q],
                    ssum + [p + q])
        dfs([], [], [])
        return res


a = Solution()
c = a.solveNQueens(4)
for i in c:
    print(i)











