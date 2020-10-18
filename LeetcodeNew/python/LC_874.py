
class Solution:
    def robotSim(self, commands, obstacles) -> int:
        Set = set()
        for obs in obstacles:
            Set.add((obs[0], obs[1]))

        # must be this order
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = 0
        x, y = 0, 0
        d = 0

        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d + 3) % 4
            else:
                while command > 0 and ( x +dirs[d][0], y+ dirs[d][1]) not in Set:
                    x += dirs[d][0]
                    y += dirs[d][1]
                    command -= 1

            res = max(res, x * x + y * y)

        return res






