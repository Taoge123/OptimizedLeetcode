class Solution:

    def countArrangement(self, N):
        visited = [False] * (N + 1)
        count = [0]
        self.helper(visited, N, 1, count)
        return count[0]

    def helper(self, visited, N, i, count):
        if i > N:
            count[0] += 1
            return
        for n in range(1, N + 1):
            divisible = (n % i == 0) or (i % n == 0)
            if not visited[n] and divisible:
                visited[n] = True
                self.helper(visited, N, i + 1, count)
                visited[n] = False




cache = {}
class Solution(object):
    def countArrangement(self, N):
        def helper(i, X):
            if i == 1:
                return 1
            key = (i, X)
            if key in cache:
                return cache[key]
            total = 0
            for j in range(len(X)):
                if X[j] % i == 0 or i % X[j] == 0:
                    total += helper(i - 1, X[:j] + X[j + 1:])
            cache[key] = total
            return total
        return helper(N, tuple(range(1, N + 1)))


class Solution3:
    def countArrangement(self, N):
        def count(i, X):
            if i > N:
                return 1
            return sum(count(i + 1, X - {x})
                       for x in X
                       if x % i == 0 or i % x == 0)

        return count(1, set(range(1, N + 1)))

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if not N or N < 1:
            return 0

        visited = [False]*N
        count = [0]
        self.helper(visited, N, 0, count)

        return count[0]

    def helper(self, visited, N, i, count):
        if i == N:
            count[0] += 1
            return

        for n in range(N):
            divisible = ((n+1) % (i+1) == 0) or ((i+1) % (n+1)== 0)
            if not visited[n] and divisible:
                visited[n] = True
                self.helper(visited, N, i+1, count)
                visited[n] = False


class Solution(object):
    def countArrangement(self, N):
        # memoization
        self.mymap = {}

        used = [False] * (N + 1)
        return self.backtracking(1, used, N)

    def backtracking(self, pos, used, N):
        # number of beautiful arrangements we can have from now on
        count = 0

        # transform bool array into integer to store it in hash table
        key = self.to_string(used)

        # check if we already have the answer
        if key in self.mymap:
            return self.mymap[key]

        # if at the end
        if pos == N + 1:
            return 1

        for i in range(1, N + 1):
            if not used[i] and (i % pos == 0 or pos % i == 0):
                used[i] = True
                count += self.backtracking(pos + 1, used, N)
                used[i] = False

        self.mymap[key] = count
        return count

    # transform function
    def to_string(self, arr):
        ans = 0
        for i in arr:
            if i: ans |= 1
            ans <<= 1
        return ans
