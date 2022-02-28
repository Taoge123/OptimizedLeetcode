
class SolutionRikaFast:
    def closestCost(self, baseCosts, toppingCosts, target):
        self.minn = float('inf')
        self.res = 0
        for base in baseCosts:
            self.dfs(toppingCosts, target, 0, base)
        return self.res

    def dfs(self, toppingCosts, target, i, summ):  # i is for current topping cst is cost till now
        diff = abs(target - summ)

        if summ > target and diff > self.minn:
            return

        if diff == self.minn:
            self.res = min(self.res, summ)
        if diff < self.minn:
            self.minn = diff
            self.res = summ

        if i >= len(toppingCosts):
            return

        self.dfs(toppingCosts, target, i + 1, summ)
        self.dfs(toppingCosts, target, i + 1, summ + toppingCosts[i])
        self.dfs(toppingCosts, target, i + 1, summ + toppingCosts[i] * 2)



class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):

        toppings = [0]
        n = len(toppingCosts)

        def dfs(i, total):
            if i == n:
                toppings.append(total)
                return
            dfs(i + 1, total + 2 * toppingCosts[i])
            dfs(i + 1, total + toppingCosts[i])
            dfs(i + 1, total)

        dfs(0, 0)
        possible = []
        for topping in toppings:
            for base in baseCosts:
                possible.append([base + topping, abs(target - (base + topping))])
        possible.sort(key=lambda x: [x[1], x[0]])
        return possible.pop(0)[0]





