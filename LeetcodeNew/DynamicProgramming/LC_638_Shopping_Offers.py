
"""
https://blog.csdn.net/fuxuemingzhu/article/details/82504050
https://blog.csdn.net/XX_123_1_RJ/article/details/81269165


In LeetCode Store, there are some kinds of items to sell. Each item has a price.

However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given the each item's price, a set of special offers, and the number we need to buy for each item.
The job is to output the lowest price you have to pay for exactly certain items as given,
where you could make optimal use of the special offers.

Each special offer is represented in the form of an array,
the last number represents the price you need to pay for this special offer,
other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.

Example 1:
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation:
There are two kinds of items, A and B. Their prices are $2 and $5 respectively.
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B.
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
Example 2:
Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation:
The price of A is $2, and $3 for B, $4 for C.
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C.
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C.
You cannot add more items, though only $9 for 2A ,2B and 1C.
Note:
There are at most 6 kinds of items, 100 special offers.
For each item, you need to buy at most 6 of them.
You are not allowed to buy more items than you want, even if that would lower the overall price.
"""
import sys

class Solution1:
    def shoppingOffers(self, price, special, needs):
        d = {}

        def dfs(cur):
            val = sum(cur[i] * price[i] for i in range(len(needs)))  # cost without special
            for spec in special:
                tmp = [cur[j] - spec[j] for j in range(len(needs))]
                if min(tmp) >= 0:  # skip deals that exceed needs
                    val = min(val, d.get(tuple(tmp), dfs(tmp)) + spec[-1])  # .get check the dictionary first for result, otherwise perform dfs.
            d[tuple(cur)] = val
            return val

        return dfs(needs)


class Solution2:
    def find_lowest_price(self, price, special, needs):
        # Memorization
        if tuple(needs) in self.dp:
            return self.dp[tuple(needs)]
        # Don't take offers
        cost = 0
        for i, need in enumerate(needs):
            cost += need * price[i]

        # Take one offer
        for offer in special:
            # Make sure it can take at least one offer
            for i, need in enumerate(needs):
                if need < offer[i]:
                    break
            else:
                new_needs = [need - offer[i] for i, need in enumerate(needs)]
                # Update cost
                cost = min(cost, offer[-1] + self.find_lowest_price(price, special, new_needs))
        self.dp[tuple(needs)] = cost
        return cost

    def shoppingOffers(self, price, special, needs):

        self.dp = {}
        return self.find_lowest_price(price, special, needs)


"""
regular DFS
the only difference is that in the dfs search start with
picking special offer 2, we don't need to picking special offer 1 again as the combination would be already calculated.
example:
pick sp1,sp1,sp2 is the same as pick sp2, sp1, sp1
"""

class Solution3:
    def shoppingOffers(self, price, special, needs):

        self.res = sys.maxint
        self.dfs(needs, special, price, 0, 0)
        return self.res

    def dfs(self, needs, special, price, currentprice, specialindex):
        if needs == [0 for x in range(len(needs))]:
            self.res = min(self.res, currentprice)
            return
        for x in range(specialindex, len(special)):
            vaild = True
            for y in range(len(needs)):
                if needs[y] < special[x][y]:
                    vaild = False
                    break
            if vaild == True:
                nextneeds = [needs[a] - special[x][a] for a in range(len(needs))]
                self.dfs(nextneeds, special, price, currentprice + special[x][-1], x)
        for z in range(len(needs)):
            if needs[z] >= 1:
                currentprice += price[z] * needs[z]
        self.res = min(self.res, currentprice)


"""
Just recursively try every possible combination.
Compare how much it costs among retail price (no offer) and using each offer.
Terminate when
(1) The condition met: return accumulated value
(2) The condition violated: not an option, hence infinity
"""

class Solution4:
    def shoppingOffers(self, price, special, needs):
        def dfs(remain, acc):
            if all(x == 0 for x in remain):
                return acc
            elif any(x < 0 for x in remain):
                return float('inf')
            ans = sum(map(lambda x, y: x * y, remain, price))
            for spc in special:
                ans = min(ans, dfs(map(lambda x, y: x - y, remain, spc[:-1]), spc[-1]))
            return ans + acc

        return dfs(needs, 0)


"""
DFS
明显是DP的题目，但DFS没超时的话可以使用DFS解。

我们定义DFS返回的是对于当前的needs需要付出的最小价格。

因为这个题允许多次使用同一个套餐，所以这次dfs不需要像permutation一样记录位置，只需要保留我们如果直接购买或者套餐之后，剩余的商品数目即可。

dfs的做法是这样：求出直接购买这些商品的价格，然后遍历所有的套餐，看能不能使用这个套餐
（判断的方式是使用套餐之后仍然还有剩余物品），保存所有情况下的最小值返回即可。

这种做法在remains全部是0的情况下，也会做一次遍历。但是注意不能改成min(remains) > 0的情况下才去继续遍历，
因为有一个needs已经为0了的情况下，我们还要确保其他的needs都是0才可以。

我在写下面这个代码的时候，犯了一个大错：计算local_min的时候写成了
local_min = min(local_min, spec[-1]) + self.dfs(price, special, remains)，这个错误不可饶恕啊！！

"""


class Solution11:
    def shoppingOffers(self, price, special, needs):

        return self.dfs(price, special, needs)

    def dfs(self, price, special, needs):
        local_min = self.directPurchase(price, needs)
        for spec in special:
            remains = [needs[j] - spec[j] for j in range(len(needs))]
            if min(remains) >= 0:
                local_min = min(local_min, spec[-1] + self.dfs(price, special, remains))
        return local_min

    def directPurchase(self, price, needs):
        total = 0
        for i, need in enumerate(needs):
            total += price[i] * need
        return total

# 使用记忆化搜索可以加速计算，代码如下：
class Solution22:
    def shoppingOffers(self, price, special, needs):

        return self.dfs(price, special, needs, {})

    def dfs(self, price, special, needs, d):
        val = sum(price[i] * needs[i] for i in range(len(needs)))
        for spec in special:
            remains = [needs[j] - spec[j] for j in range(len(needs))]
            if min(remains) >= 0:
                val = min(val, d.get(tuple(needs), spec[-1] + self.dfs(price, special, remains, d)))
        d[tuple(needs)] = val
        return val

# 其实不用定义一个新的函数dfs()，因为我们可以看出dfs的参数和原函数一样的，所以直接用原函数进行递归更方便
class Solution33:
    def shoppingOffers(self, price, special, needs):

        N = len(needs)
        res = sum(p * n for p, n in zip(price, needs))
        for sp in special:
            if all(sp[i] <= needs[i] for i in range(N)):
                remain = [needs[i] - sp[i] for i in range(N)]
                if min(remain) >= 0:
                    res = min(res, sp[-1] + self.shoppingOffers(price, special, remain))
        return res



