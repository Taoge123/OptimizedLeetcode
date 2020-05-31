
class Cashier:
    def __init__(self, n: int, discount: int, products, prices):
        self.price = {pro : pri for pro, pri in zip(products, prices)}
        self.discount = discount
        self.n = n
        self.count = 0

    def getBill(self, product, amount) -> float:
        self.count += 1
        res = 0
        for p, a in zip(product, amount):
            res += self.price[p] * a

        if self.count == self.n:
            self.count = 0
            res -= (self.discount * res) / 100

        return res



