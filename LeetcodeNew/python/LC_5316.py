class Solution:
    def printVertically(self, s: str):
        """
        CONTEST IS COMING
        i
               j
        """
        string = s.split(' ')
        string = [list(i) for i in string]
        n = max(len(i) for i in string)

        for i, val in enumerate(string):
            temp = len(val)
            if temp < n:
                string[i].extend([' '] * (n - temp))

        string = [i[::-1] for i in string]
        res = []
        for i in range(n):
            again = []
            for i, val in enumerate(string):
                again.append(string[i].pop())

            while again[-1] == ' ':
                again.pop()

            res.append("".join(again))

        return res





s = "CONTEST IS COMING"
a = Solution()
print(a.printVertically(s))


