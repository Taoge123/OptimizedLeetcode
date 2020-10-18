class Solution1:
    def maxDistToClosest(self, seats) -> int:
        n = len(seats)
        left = [n] * n
        right = [n] * n

        for i in range(n):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1

        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < n - 1:
                right[i] = right[i + 1] + 1

        res = 0
        for i in range(n):
            if seats[i] == 0:
                res = max(res, min(left[i], right[i]))

        return res



class Solution2:
    def maxDistToClosest(self, seats) -> int:
        n = len(seats)
        left = -1
        right = 0
        res = 0
        for i in range(n):
            if seats[i] == 1:
                left = i
            else:
                while right < n and seats[right] == 0 or right < i:
                    right += 1
                l = n if left == -1 else i - left
                r = n if right == n else right - i
                res = max(res, min(l, r))
        return res




