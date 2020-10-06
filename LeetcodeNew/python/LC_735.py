
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for num in asteroids:
            if num > 0:
                stack.append(num)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(num):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(num)
                elif num + stack[-1] == 0:
                    stack.pop()

        return stack


class Solution2:
    def asteroidCollision(self, asteroids):
        res = []
        for num in asteroids:
            while res and num < 0 < res[-1]:
                if res[-1] < abs(num):
                    res.pop()
                    continue
                elif res[-1] == abs(num):
                    res.pop()
                break
            else:
                res.append(num)
        return res





