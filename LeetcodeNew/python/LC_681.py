

class Solution:
    def nextClosestTime(self, time):
        digits = [int(y) for x in time.split(':') for y in x]
        h, m = time.split(':')
        while True:
            h, m = (str(int(h) + 1), '00') if int(m) == 59 else (h, str(int(m) + 1))
            h = '00' if int(h) > 23 else h
            h = '0' + h if len(h) == 1 else h
            m = '0' + m if len(m) == 1 else m
            if all([int(x) in digits for x in h + m]):
                return h + ':' + m



