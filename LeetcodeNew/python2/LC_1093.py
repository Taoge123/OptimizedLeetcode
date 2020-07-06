

class Solution:
    def sampleStats(self, count):
        mini = 256
        maxi = 0
        summ = 0
        num = 0
        maxCount = 0
        mode = 0
        for i in range(256):
            if count[i] == 0:
                continue
            mini = min(mini, i)
            maxi = max(maxi, i)
            summ += count[i] * i
            num += count[i]
            if count[i] > maxCount:
                maxCount = count[i]
                mode = i

        t = 0
        a, b = -1, -1
        for i in range(256):
            t += count[i]
            if num % 2 == 0:
                if t >= num / 2 and a == -1:
                    a = i
                if t >= num / 2 + 1 and b == -1:
                    b = i
                if a != -1 and b != -1:
                    median = (a + b) * 1 / 2
                    break
            else:
                if t >= num / 2 + 1:
                    median = i
                    break
        return [mini, maxi, summ / num, median, mode]




