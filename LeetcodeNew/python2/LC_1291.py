
class SolutionDFS:
    def sequentialDigits(self, low: int, high: int):

        res = []
        queue = collections.deque()
        for i in range(1, 10):
            queue.append(i)

        while queue:
            node = queue.popleft()
            if low <= node <= high:
                res.append(node)
            if node > high:
                continue
            if node % 10 != 9:
                queue.append(node * 10 + (node % 10) + 1)
        return res



class Solution2:
    def sequentialDigits(self, low: int, high: int):
        sample = "123456789"
        n = 10
        nums = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length):
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    nums.append(num)

        return nums


