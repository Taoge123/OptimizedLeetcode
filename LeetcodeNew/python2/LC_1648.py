"""
https://leetcode.com/problems/sell-diminishing-valued-colored-balls/discuss/927674/Python3-Greedy

10 8 6 4 2

9  8 6 4 2  + 10
8  8 6 4 2  + 9
7  7 6 4 2  + 8 * 2
6  6 6 4 2  + 7 * 2
5  5 5 4 2  + 6 * 3
4  4 4 4 2  + 5 * 3
3  3 3 3 2  + 4 * 4
2  2 2 2 2  + 3 * 4
1  1 1 1 1  + 2 * 5
0  0 0 0 0  + 1 * 5

解法1：数学贪心
本题的基本策略是：将所有的颜色按照数量从高到低排列。我们优先对当前数量最多（a）的颜色取一个球，这样总价值+a。然后再对当前剩余数量最多（b）的颜色取一个球（可能仍然是同一种颜色），这样总价值+b...直到我们操作的次数达到orders。

举个例子，我们将inventory从高到低排序之后，假设数组长这个样子：

10 7 4 3 2 1
第一回合：数值最大的10就是我们的操作目标，我们取一个球，总价值加10分。但是取完之后发现最大数量的颜色依然是它，但是9个球，意味着我们还可以再取一个球再增加9分。我们可以不断地取这个颜色，直至该颜色的数目和第二多的颜色数目持平（都是7）。所以这一轮我们的价值增加的是(10+9+8).

第二回合：当前数值最大的7就是我们的操作目标。注意这次我们可以取2个球：包括颜色数量排名第一和第二的两种颜色。此外，我们可以从+7，+6，一直取到+5（因为数量第三多的颜色数量是4），故增加的价值是(7+6+5)*2

可见每个回合，我们就推进了一种颜色。在处理第i种颜色时，我们可以一轮取i+1个球，这些球对应的分值是相同的，从inventory[i]、inventory[i]+1...直至inventory[i+1]+1。

这里有一个比较关键的地方，就是总球数达到orders的时候，我们必须停下来。在哪个回合的哪一轮停下来，“零头”是多少，需要好好处理。从上述可知，在第i回合中，每轮可以取i+1个球，可知需要进行q = orders/(i+1)轮，剩下的零头r = orders%(i+1)个球对应的分数就是inventory[i]-q.

另一个注意的点是，对于10 10 8....这种情况，根据上述的算法，第一回合其实不用做任何操作，因为第一和第二的颜色数目相同。在第二回合的操作里直接一并取两个球。

Algo
First, it should be clear that we want to sell from the most abundant balls as much as possible as it is valued more than less abundant balls. In the spirit of this, we propose the below algo

sort inventory in reverse order and append 0 at the end (for termination);
scan through the inventory, and add the difference between adjacent categories to answer.
Assume inventory = [2,8,4,10,6]. Then, we traverse inventory following 10->8->6->4->2->0. The evolution of inventory becomes
"""


class Solution:
    def maxProfit(self, nums, orders: int) -> int:
        nums.sort(reverse=True)
        nums.append(0)
        profit = 0
        width = 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if width * (nums[i] - nums[i + 1]) < orders:
                    profit += width * self.compute(nums[i + 1] + 1, nums[i])
                    orders -= width * (nums[i] - nums[i + 1])
                else:
                    whole, remaining = divmod(orders, width)
                    profit += width * self.compute(nums[i] - whole + 1, nums[i])
                    profit += remaining * (nums[i] - whole)
                    break
            width += 1
        return profit % (10 ** 9 + 7)

    def compute(self, lo, hi):
        return (hi * (hi + 1)) // 2 - (lo * (lo - 1)) // 2





class Solution2:
    def maxProfit(self, nums, orders: int) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        nums.append(0)
        mod = 10 ** 9 + 7
        res = 0

        for i in range(n):
            a = nums[i]
            b = nums[i + 1]

            total = (a - b) * (i + 1)

            if total <= orders:
                res += (a + b + 1) * (a - b) // 2 * (i + 1)
                orders -= total
                res %= mod

            else:
                k = orders // (i + 1)
                res += (a + a - k + 1) * k // 2 * (i + 1)
                res %= mod

                remain = orders % (i + 1)
                res += (a - k) * remain
                res %= mod
                break

            if orders <= 0:
                break
        return res


