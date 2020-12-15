
class Solution:
    def confusingNumberII(self, N: int) -> int:
        valid = [0, 1, 6, 8, 9]
        table = {0 :0, 1 :1, 6 :9, 8 :8, 9 :6}

        self.res = 0
        def dfs(num, rotation, pos):
            if num != rotation:
                self.res += 1
            for digit in valid:
                if num == 0 and digit == 0:
                    continue
                # generate new number
                new_num = num * 10 + digit
                # check if number within given range
                if new_num <= N:
                    # generate its rotation using the previous rotation and recently added digit
                    new_rot = table[digit] * pos + rotation
                    dfs(new_num, new_rot, pos * 10)

        dfs(0, 0, 1)
        return self.res



