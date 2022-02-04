
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





