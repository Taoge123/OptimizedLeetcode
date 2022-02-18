
"""
https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/83091/Python-10-Lines-(Recursive-and-DP-solutions)


"""


class SolutionRika2:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        memo = {}
        return self.dfs(n, 0, set(), memo)

    def dfs(self, n, i, visited, memo):
        if i in memo:
            return memo[i]
        if i == n:
            return 1

        res = 1
        for num in range(0, 10):
            if i == 0 and num == 0:  # no leading zero
                continue
            if num in visited:  # de-duplicated
                continue
            visited.add(num)
            res += self.dfs(n, i + 1, visited, memo)
            visited.remove(num)
        memo[i] = res
        return res

    

class SolutionRika:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        memo = {}
        return self.dfs(n, 0, [0] * 10, memo)

    def dfs(self, n, i, visited, memo):
        if i in memo:
            return memo[i]
        if i == n:
            return 1

        res = 1
        for num in range(0, 10):
            if i == 0 and num == 0:  # no leading zero
                continue
            if visited[num]:  # de-duplicated
                continue
            visited[num] = True
            res += self.dfs(n, i + 1, visited, memo)
            visited[num] = False
        memo[i] = res
        return res



class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        nums = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1
        for i in range(min(n, 10)):
            product *= nums[i]
            ans += product
        return ans


"""
1
9
81
81 * 8

"""


class SolutionDFS1:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        # @cache
        def dfs(i):
            if i == 0:
                ## Base case
                # only 0 for [0, 1) interval
                return 1

            elif i == 1:
                ## Base case
                # only 0 ~ 9 for [0, 10) interval
                return 10

            else:
                ## General case:
                # cur count = current count of unique digits contributed from [ 10^(k-1), 10^k ) interval
                # count(k-1) = count of unique digits contributed from [0, 10^(k-1) ) interval
                # count(k-1) + cur count = count of unique digits from [0, 10^k ) interval

                count = 9
                for j in range(1, i):
                    count = count * (10 - j)

                return dfs(i - 1) + count

        return dfs(n)



