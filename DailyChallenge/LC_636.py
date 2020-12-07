class Solution:
    def exclusiveTime(self, n, logs):
        res = [0] * n
        stack = []
        prev = 0

        for log in logs:
            ID, typ, time = log.split(':')
            ID, time = int(ID), int(time)

            if typ == 'start':
                if stack:
                    res[stack[-1]] += time - prev
                stack.append(ID)
                prev = time
            else:
                res[stack.pop()] += time - prev + 1
                prev = time + 1

        return res


