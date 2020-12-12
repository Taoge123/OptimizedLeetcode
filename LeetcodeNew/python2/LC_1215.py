import collections

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



