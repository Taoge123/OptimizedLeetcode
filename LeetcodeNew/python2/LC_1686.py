"""
1686.Stone-Game-VI
对于Alice而言，什么才是最优的决策吗？是优先选择自己能得到的最大值吗？并不是，通过这个例子就可以看出来：

Alice: 1 2
Bob:   3 1
如果Alice优先选择第二个元素的话，那么Bob选择第一个元素反而会有更高的总分。于是我们显然发现，对于Alice而言，每一步的决策不仅要使自己的得分高，而且需要使对手的得分低。对于Alice而言，如果选择了第二个元素，那么Alice得了2分，Bob失去了一个得1分的机会，这一反一正差距是3分。同理，对于Bob而言，如果选择了第一个元素，那么自己得了3分，Alice失去了一个得1分的机会，这一反一正就是4分。

所以，不管对哪个选手而言，一个元素的价值其实体现在了这个一反一正上。即使我自己得的分少，如果能让你失去了得高分的机会，也是一个成功的策略。

所以本题的算法很简单，将所有元素按照AliceValues[i]+BobValues[i]的大下排列。然后Alice和Bob轮流选取，对它们而言就是最优的决策。

"""



import heapq

class Solution:
    def stoneGameVI(self, aliceValues, bobValues) -> int:
        nums = []
        for i in range(len(aliceValues)):
            nums.append((-aliceValues[i] - bobValues[i], aliceValues[i], bobValues[i]))
        heapq.heapify(nums)
        alice, bob = 0, 0
        # n = len(nums)
        i = 0

        while nums:
            if i % 2 == 0:
                alice += heapq.heappop(nums)[1]
            else:
                bob += heapq.heappop(nums)[2]
            i += 1

        if alice > bob:
            return 1
        elif alice == bob:
            return 0
        else:
            return -1



