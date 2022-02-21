import collections


class SolutionTony:
    def countSteppingNumbers(self, low, high):
        res = []
        if low == 0:
            res.append(0)

        def dfs(num):
            if num > high:
                return
            if num >= low:
                res.append(num)

            last = num % 10
            if last > 0:
                dfs(10 * num + last - 1)
            if last < 9:
                dfs(10 * num + last + 1)

        for num in range(1, 10):
            dfs(num)

        res = sorted(res)
        return res





class SolutionRika:
    def countSteppingNumbers(self, low, high):
        minsize = len(str(low))
        maxsize = len(str(high))

        res = []
        if low == 0:
            res.append(0)
        self.dfs(low, high, '', res, minsize, maxsize)
        res = sorted(res)
        return res

    def dfs(self, low, high, path, res, minsize, maxsize):

        if len(path) >= minsize and low <= int(path) <= high:
            res.append(int(path))

        for num in range(10):
            if not path and num == 0:  # no leading zero
                continue
            if not path or abs(int(path[-1]) - num) == 1:
                if len(path) <= maxsize and int(path + str(num)) <= high:
                    self.dfs(low, high, path + str(num), res, minsize, maxsize)




class Solution:
    def countSteppingNumbers(self, low: int, high: int):
        res = []
        if low == 0:
            res.append(0)

        queue = collections.deque()
        for i in range(1, 10):
            queue.append(i)

        while queue:
            num = queue.popleft()
            if num >= low and num <= high:
                res.append(num)

            last = num % 10
            num = num * 10

            if num < high:
                # if the last digit is more than 0 then, we can reduce one from it and add the new digit to our list
                if last != 0:
                    queue.append(num + last - 1)
                # if the last digit is less than 9, then we can add one value and add it to the list
                if last != 9:
                    queue.append(num + last + 1)

        return res



