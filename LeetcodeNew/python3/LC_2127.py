
"""
2127.Maximum-Employees-to-Be-Invited-to-a-Meeting
我们设想一下从任意一个人出发，不停地沿着“舔狗链”传递，最终会出现什么情况？一定会出现一个环。因为本题里规定了所有的人都有出度（即有喜欢的人），否则没有环的话那就一定有出度为0的dead end。所以题目中构造出的图，一定长得是这样的模式：一个连通图以一个环为主体，另外可能有若干单链指向环上的节点。当然，这种连通图可能会有多个（即彼此不相连）。

此时我们可以想到的是，选择这些环一定是满足条件的策略。因为只有环才能满足每个人都与喜欢的人相邻，否则引入任何其他分支（单链）都无法满足条件（因为在接入点处，会有一个出度，两个入度，但每个人在圆桌上只允许有两个邻居）。于是，选择其中最大的环，似乎就是最佳选择。

但是以上的分析只适用于环的节点个数>=3的时候。如果存在一个节点数为2的环（即两个人A和B互相喜欢），那么任何指向A的单链和指向B的单链加入其中，依然是合法的圆桌策略。所以我们需要考虑这一种可能：大小为2的环，加上两个节点所外接的各自最长单链。更神奇的时候，事实上我们把所有这种“二元环+二单链”模式的连通图的节点都围坐起来，依然是一个合法的策略。

所以本题的答案应该是max{“最大的多元环”的大小，所有“二元环+二单链模式”的大小之和}.

具体的做法如下：

利用拓扑排序，把所有非环的外围单链砍掉。同时有一个附加的好处，我们从每个入度为0的点开始标记深度，待拓扑排序结束后，我们就能得到所有环上的节点所外接的其中最长单链的长度。
将剩余的节点（一定都在环上）任取一个开始遍历，可以得到一个完整的环的大小。由此遍历所有的环。每遍历一个环，需要考察是二元环还是多元环。
输出答案：max{“最大的多元环”的大小，“所有二元环+二单链模式”的大小之和}.

https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/discuss/1661178/Explanation-with-pictures.
https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/discuss/1661147/Python-or-Discuss-cycle-size-greater-3-or-size-2-with-visualized-explanation
https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/discuss/1661824/Python-or-Simple-Step-by-Step-Explained-or-O(n)-with-only-topological-sort-or-1100-ms

"""





