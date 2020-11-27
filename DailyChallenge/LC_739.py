
class SolutionTony:
    def dailyTemperatures(self, T):
        stack = []
        res = [0] * len(T)
        for i, num in enumerate(T):
            while stack and T[stack[-1]] < num:
                node = stack.pop()
                res[node] = i - node
            stack.append(i)
        return res

