
"""
题目 leetcode 1029 Two City Scheduling
输入一个长度是2*N的二维数组， a[i][0]表示第i个人分配到A城市的价格， a[i][1]表示第i个人分配到B城市的价格
把这2*N个数组分成长度相等的两份， 其中一半选择A， 另外一半选择B， 问总共最小的总共价格是多少？
刷题感悟
这个题目暴力肯定不行， 直接简单的贪心选择最小的也不对， 卡壳了好一会儿。
还好后来终于想出来了，感觉这样的题目能不能分析出来很没有把握。
解题思路分析
假设所有的人都选择城市A， 这时候sum=sum{a[i][0]},
然后要选择一半的人改成B， 这个时候, 选择某一个人对sum的影响是d=a[i][1]-a[i][0],
那么， 我们要让结果最小， 就需要让这个d最小， 那按照这个d对数组排序，然后选择最小的一半就好

"""

class Solution:
    def twoCitySchedCost(self, costs) -> int:
        dif = [cost[1]-cost[0] for cost in costs]
        res = sum([cost[0] for cost in costs])
        dif.sort()
        for i in range(len(costs)//2):
            res += dif[i]
        return res


