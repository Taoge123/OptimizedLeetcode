class Solution(object):
    def strWithout3a3b(self, A, B):
        res = []
        while A or B:
            if len(res) >= 2 and res[-1] == res[-2]:
                writeA = res[-1] == 'b'
            else:
                writeA = A >= B

            if writeA:
                A -= 1
                res.append('a')
            else:
                B -= 1
                res.append('b')

        return "".join(res)



class Solution2:
    def strWithout3a3b(self, A: int, B: int) -> str:
        res = []
        if A > B:
            diff = A - B
            for i in range(B):
                res.append('a')
                if diff > 0:
                    res.append('a')
                    diff -= 1
                res.append('b')

            for i in range(diff):
                res.append('a')
        else:
            diff = B - A
            for i in range(A):
                res.append('b')
                if diff > 0:
                    res.append('b')
                    diff -= 1
                res.append('a')

            for i in range(diff):
                res.append('b')
        return "".join(res)


