
"""

Example 1:
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string,
which will cover the existing character 'a'.


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


https://blog.csdn.net/XX_123_1_RJ/article/details/81269165

这个题目，猛地一看，感觉无法下手，其实，仔细想想，一个深度优先搜索，是可以解决的。
现在先明确题目中的一个说明，就是你不可以购买超出待购清单的物品，即使更便宜，这个很重要，
可以进行减枝，加快计算。
在这里使用记忆化搜索(Search Memoization)方法。
1）令 dp[cur] = val，表示，在我们需要的商品数量为cur时，的最小花费为val。
例如dp[(1,2,1)] = val，表示我们需要的商品数cur = [1,2,1] 时的最小花费为val，
其中dp可以使用字典数据类型。
2）从上向下，进行递归，如下草图（黑色线表示下递归，红色虚线表示回溯底层最优解），
在最原始的状态上，遍历每一个礼包，获取最优值，每个礼包继续下递归，完成深度优先搜索。
在这个过程中，每次遍历的初始化状态就是，不使用礼包时的价格。所以递推方程为：

记忆化搜索(Search Memoization)
算法上依然是搜索的流程，但是搜索到的一些解用动态规划的那种思想和模式作一些保存。
一般说来，动态规划总要遍历所有的状态，而搜索可以排除一些无效状态。更重要的是搜索还可以剪枝，
可能剪去大量不必要的状态，因此在空间开销上往往比动态规划要低很多。
记忆化算法在求解的时候还是按着自顶向下的顺序，但是每求解一个状态，就将它的解保存下来，
以后再次遇到这个状态的时候，就不必重新求解了。这种方法综合了搜索和动态规划两方面的优点，
因而还是很有实用价值的[1]。
---------------------

 
dp[cur] = min(val, dp.get(tmp, dfs(tmp)) + spec[-1])

tmp为cur使用了某一个礼包之后的需要数， spec[-1] 对应这当前礼包的价格。
在同一层上遍历一边，获取最小的那个值。
---------------------
作者：GorillaNotes
来源：CSDN
原文：https://blog.csdn.net/XX_123_1_RJ/article/details/81269165
版权声明：本文为博主原创文章，转载请附上博文链接！
"""

class Solution:
    def shoppingOffers(self, price, special, needs):

        dp = {}  # 初始化，dp,用于保存每个状态的最优解

        def dfs(cur):
            val = sum(cur[i] * price[i] for i in range(len(needs)))  # 不用礼包时的价格
            for spec in special:
                tmp = [cur[j] - spec[j] for j in range(len(needs))]
                if min(tmp) >= 0:  # 过滤掉，礼包里面的商品多于需求的，礼包， 其中这个一步也相当于减枝
                    val = min(val, dp.get(tuple(tmp), dfs(tmp)) + spec[-1])  # 循环--递归--获取最优解
            dp[tuple(cur)] = val
            return val
        return dfs(needs)


if __name__ == '__main__':
    solu = Solution()
    price, special, needs = [2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]
    print(solu.shoppingOffers(price, special, needs))

"""
DFS
明显是DP的题目，但DFS没超时的话可以使用DFS解。

我们定义DFS返回的是对于当前的needs需要付出的最小价格。

因为这个题允许多次使用同一个套餐，所以这次dfs不需要像permutation一样记录位置，只需要保留我们如果直接购买或者套餐之后，
剩余的商品数目即可。

dfs的做法是这样：求出直接购买这些商品的价格，然后遍历所有的套餐，
看能不能使用这个套餐（判断的方式是使用套餐之后仍然还有剩余物品），保存所有情况下的最小值返回即可。

这种做法在remains全部是0的情况下，也会做一次遍历，稍微麻烦了一点。

我在写下面这个代码的时候，犯了一个大错：
计算local_min的时候写成了local_min = min(local_min, spec[-1]) + self.dfs(price, special, remains)，
这个错误不可饶恕啊！！
"""

"""
这道题说有一些商品，各自有不同的价格，然后给我们了一些优惠券，可以在优惠的价格买各种商品若干个，
要求我们每个商品要买特定的个数，问我们使用优惠券能少花多少钱，注意优惠券可以重复使用，而且商品不能多买。
那么我们可以先求出不使用任何商品需要花的钱数作为结果res的初始值，然后我们遍历每一个coupon，
定义一个变量isValid表示当前coupon可以使用，然后遍历每一个商品，如果某个商品需要的个数小于coupon中提供的个数，
说明当前coupon不可用，isValid标记为false。如果遍历完了发现isValid还为true的话，表明该coupon可用，
我们可以更新结果res，对剩余的needs调用递归并且加上使用该coupon需要付的钱数。最后别忘了恢复needs的状态：

"""
class Solution2:
    def shoppingOffers(self, price, special, needs):

        return self.dfs(price, special, needs)

    def dfs(self, price, special, needs):
        res = self.directPurchase(price, needs)
        for spec in special:
            remains = [needs[j] - spec[j] for j in range(len(needs))]
            if min(remains) >= 0:
                local_min = min(res, spec[-1] + self.dfs(price, special, remains))
        return res

    def directPurchase(self, price, needs):
        total = 0
        for i, need in enumerate(needs):
            total += price[i] * need
        return total

#Use cache
class Solution3:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        return self.dfs(price, special, needs, {})

    def dfs(self, price, special, needs, d):
        val = sum(price[i] * needs[i] for i in range(len(needs)))
        for spec in special:
            remains = [needs[j] - spec[j] for j in range(len(needs))]
            if min(remains) >= 0:
                val = min(val, d.get(tuple(needs), spec[-1] + self.dfs(price, special, remains, d)))
        d[tuple(needs)] = val
        return val













