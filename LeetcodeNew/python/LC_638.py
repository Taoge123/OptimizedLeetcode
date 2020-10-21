class Solution:
    def shoppingOffers(self, price, special, needs):
        return self.dfs(price, special, needs)

    def dfs(self, price, special, needs):
        res = self.directPurchase(price, needs)
        for offer in special:
            # remains = [needs[j] - offer[j] for j in range(len(needs))]
            remains = []
            for j in range(len(needs)):
                remains.append(needs[j] - offer[j])
            if min(remains) >= 0:
                res = min(res, offer[-1] + self.dfs(price, special, remains))
        return res

    def directPurchase(self, price, needs):
        total = 0
        for i, need in enumerate(needs):
            total += price[i] * need
        return total



class Solution2:
    def shoppingOffers(self, price, special, needs):

        return self.dfs(price, special, needs, {})

    def dfs(self, price, special, needs, memo):
        if tuple(needs) in memo:
            return memo[tuple(needs)]

        res = self.directPurchase(price, needs)
        for spec in special:
            remains = [needs[j] - spec[j] for j in range(len(needs))]
            if min(remains) >= 0:
                res = min(res, spec[-1] + self.dfs(price, special, remains, memo))
            memo[tuple(remains)] = res
        return memo[tuple(remains)]

    def directPurchase(self, price, needs):
        total = 0
        for i, need in enumerate(needs):
            total += price[i] * need
        return total





