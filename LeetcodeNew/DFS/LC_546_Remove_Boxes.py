
"""

Given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left.
Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1),
remove them and get k*k points.
Find the maximum points you can get.

Example 1:
Input:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
Output:
23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)
Note: The number of boxes n would not exceed 100.


动态规划（Dynamic Programming）

首先把连续相同颜色的盒子进行合并，得到数组color以及数组length，分别表示合并后盒子的颜色和长度

dp[l][r][k]表示第l到第r个合并后的盒子，连同其后颜色为color[r]的长度k一并消去所能得到的最大得分

https://translate.google.com/translate?hl=en&sl=zh-CN&u=http://www.cnblogs.com/grandyang/p/6850657.html&prev=search


Note: The number of boxes n would not exceed 100.

When I first started reading this question, I felt like the Zuma Game before,
so I wrote a brute force method, and the result was TLE.
In desperation, I had to search the Internet for the solution of the gods,
and I read the post written by fun4LeetCode.
The previous Reverse Pairs was the reference to the fun4LeetCode Great God's post.
It was so amazing that this time it was so wonderful, please accept it. My knees.
Then the following solution is mostly explained with reference to the post of
fun4LeetCode .
In the previous post, Reverse Pairs , the Great God summarized two modes of reproduction.
We also tried to see if it could be applied. The ability to abstract modeling
is very important for such a problem that seems to have no idea.
For the specific scenes in the topic,
we can ignore the specific representation of things,
which can help us to approach the essence of the problem.
The essence of this problem is an array.
We eliminate one or more numbers each time and get corresponding The score,
let us ask for the highest score. The previous Zuma Game also gave an array,
et us add a number to a certain position, so that at least 3 of the same number
can be eliminated. The two are not very similar,
but the solution is quite different.
The reason why the brute force crack is no problem
is because the length of the array and the number of given numbers are limited,
and they are relatively small numbers, so even if you traverse all the cases,
there will not be much calculation. And this question is not the same,
since it can not be brute force, then for the problem of playing arrays
and sub-arrays, the old drivers who brush the questions will give priority to using DP
to do it. Since you want to play a subarray,
you must limit the range of the subarray,
then at least it should be a two-dimensional dp array,
where dp[i][j] represents the highest score that can be obtained in the subarray [i, j] range.
Then, finally we return dp[0][n-1] is the result of the request.

So for dp[i][j] we think that if we remove the number boxes[i],
then the total score should be 1 + dp[i+1][j],
but by analyzing the examples in the title,
we can get The trick of high integration is that after removing one or a few numbers,
if the same number that is not continuous is changed, the continuous number is dropped,
because the more numbers are removed at the same time, the higher the score is. .
So if there is a position m in the middle of [i, j],
making boxes[i] and boxes[m] equal, then we should not just remove the number of boxes[i],
but should also consider removing them directly [ The number on the interval i+1, m-1]
makes boxes[i] and boxes[m] directly adjacent,
then the score we get is dp[i+1][m-1], then what are we left? ,
boxes[i] and boxes[m, j] interval numbers,
at this point we can't process sub-arrays [m, j],
because some of our information is not included in our dp array,
such topics are summarized as not themselves The sub-problems included,
the solution depends on information other than sub-problems .
Such problems usually do not have a well-defined recurring relationship,
so it is not easy to recursively solve.
In order to solve such problems, we need to modify the definition of the problem
so that it contains some external information,
which becomes a self-contained sub-problem .

So for this question, the boxes[m, j]
interval cannot be processed because it lacks key information.
We don't know the number k of the same number on the left side of boxes[m].
Only know this information, then the position of m It makes sense,
so our dp array should be a three-dimensional array dp[i][j][k],
which represents the maximum integral that can be obtained in the interval [i, j].
When there are k numbers on the left of boxes[i] They are equal,
then our goal is to ask dp[0][n-1][0],
and we can also introduce dp[i][i][k] = (1+k) * (1+k) This equation.
Then we will derive the recurrence relationship. For dp[i][j][k],
if we remove boxes[i], then we get (1+k)*(1+k) + dp[i+1] [j][0].
For the case mentioned above, when a position m, with boxes[i] == boxes[m],
we should also consider removing [i+1,m-1] first, we get the points Dp[i+1][m-1][0],
and then process the remaining part to get the integral dp[m][j][k+1],
where k is added 1 point because the middle is removed After the part,
the boxes[i] that are not adjacent to boxes[m] are now adjacent,
and because the two values ​​are the same, k should be incremented by 1,
because the definition of k is the number of numbers on the left.
Speaking of this, then the most difficult recursive formula of the DP method is also obtained,
then the code is not difficult to write.

刚开始看这道题的时候，感觉跟之前那道Zuma Game很像，于是就写了一个暴力破解的方法，结果TLE了。
无奈之下只好上网搜大神们的解法，又看了fun4LeetCode大神写的帖子，
之前那道Reverse Pairs就是参考的fun4LeetCode大神的帖子，惊为天人，这次又是这般精彩，
大神请收下我的膝盖。那么下面的解法就大部分参考fun4LeetCode大神的帖子来讲解吧。
在之前帖子Reverse Pairs的讲解中，大神归纳了两种重现模式，我们这里也试着看能不能套用上。
对于这种看来看去都没思路的题来说，抽象建模的能力就非常的重要了。对于题目中的具体场景啊，
具体代表的东西我们都可忽略不看，这样能帮助我们接近问题的本质，这道题的本质就是一个数组，
我们每次消去一个或多个数字，并获得相应的分数，让我们求最高能获得的分数。
而之前那道Zuma Game也是给了一个数组，让我们往某个位置加数字，使得相同的数字至少有3个才能消除，
二者是不是很像呢，但是其实解法却差别很大。
那道题之所以暴力破解没有问题是因为数组的长度和给定的数字个数都有限制，而且都是相对较小的数，
那么即便遍历所有情况也不会有太大的计算量。而这道题就不一样了，既然不能暴力破解，
那么对于这种玩数组和子数组的题，刷题老司机们都会优先考虑用DP来做吧。既然要玩子数组，
肯定要限定子数组的范围，那么至少应该是个二维的dp数组，
其中dp[i][j]表示在子数组[i, j]范围内所能得到的最高的分数，
那么最后我们返回dp[0][n-1]就是要求的结果。

那么对于dp[i][j]我们想，如果我们移除boxes[i]这个数字，那么总得分应该是1 + dp[i+1][j]，
但是通过分析题目中的例子，能够获得高积分的trick是，移除某个或某几个数字后，
如果能使得原本不连续的相同数字变的连续是坠好的，因为同时移除的数字越多，那么所得的积分就越高。
那么假如在[i, j]中间有个位置m，使得boxes[i]和boxes[m]相等，
那么我们就不应该只是移除boxes[i]这个数字，而是还应该考虑直接移除[i+1, m-1]区间上的数，
使得boxes[i]和boxes[m]直接相邻，那么我们获得的积分就是dp[i+1][m-1]，那么我们剩余了什么，
boxes[i]和boxes[m, j]区间的数，此时我们无法处理子数组[m, j]，
因为我们有些信息没有包括在我们的dp数组中，此类的题目归纳为不自己包含的子问题，
其解法依赖于一些子问题以外的信息。这类问题通常没有定义好的重现关系，所以不太容易递归求解。
为了解决这类问题，我们需要修改问题的定义，使得其包含一些外部信息，从而变成自包含子问题。

那么对于这道题来说，无法处理boxes[m, j]区间是因为其缺少了关键信息，
我们不知道boxes[m]左边相同数字的个数k，只有知道了这个信息，那么m的位置才有意义，
所以我们的dp数组应该是一个三维数组dp[i][j][k]，表示区间[i, j]中能获得的最大积分，
当boxes[i]左边有k个数字跟其相等，那么我们的目标就是要求dp[0][n-1][0]了，
而且我们也能推出dp[i][i][k] = (1+k) * (1+k)这个等式。那么我们来推导重现关系，
对于dp[i][j][k]，如果我们移除boxes[i]，那么我们得到(1+k)*(1+k) + dp[i+1][j][0]。
对于上面提到的那种情况，当某个位置m，有boxes[i] == boxes[m]时，
我们也应该考虑先移除[i+1,m-1]这部分，我们得到积分dp[i+1][m-1][0]，然后再处理剩下的部分，
得到积分dp[m][j][k+1]，这里k加1点原因是，移除了中间的部分后，
原本和boxes[m]不相邻的boxes[i]现在相邻了，又因为二者值相同，所以k应该加1，
因为k的定义就是左边相等的数字的个数。讲到这里，那么DP方法最难的递推公式也就得到了，
那么代码就不难写了

我们定义dp[l][r][k]表示在[l, r]区间并且在后面包含了k个与boxes[r]相同颜色的boxes的情况下，
可以获得的最大得分，显然题目要求的就是dp[0][boxes.size() - 1][0]。
在实现的过程中，我们采用DFS + memorization来进行状态转移，即如果需要计算一个子问题，
我们首先查看原来是不是已经计算过了，如果是，则直接拿来用；否则才用DFS进行计算。那么怎么计算呢？

首先将dp[l][r][k]的值初始化为dp[l][r - 1][0] + (k + 1)^2，表示首先消除l到r-1之间的boxes,
然后将boxes[r]连同后面的k个boxes一起消除。

然后就尝试对dp[l][r][k]进行更新了：如果在l到r-1区间内有boxes[i]和boxes[r]相同的字符，
那么可以尝试首先将区间[i + 1, r - 1]消除，这样i就和后面的k + 1个boxes连起来了，
其可以获得分数就是需要进一步计算的dp[l][i][k + 1]。

class Solution {
public:
    int removeBoxes(vector<int>& boxes) {
        return DFS(boxes, 0, boxes.size() - 1, 0);
    }
private:
    int DFS(vector<int>& boxes, int l,int r,int k) {
        if (l > r) {
            return 0; 
        }
        if (dp[l][r][k]) {
            return dp[l][r][k];                                    // if we have calculated this DFS result, return it
        }
        dp[l][r][k] = DFS(boxes, l, r - 1, 0) + (k + 1) * (k + 1); // box[l][r] result is box[l][r-1]+(k+1)^2
        for (int i = l; i < r; ++i) {                              // go through each box from left
            if (boxes[i] == boxes[r]) {                            // check for same color box as boxes[r]
                // if we found same color box, then we have a chance to get a higher value by group 
                // boxes[l] ~ boxes[i] and boxes[r] together, plus the value from boxes[i+1] ~ boxes[r-1]
                dp[l][r][k] = max(dp[l][r][k], DFS(boxes, l, i, k + 1) + DFS(boxes, i + 1, r - 1, 0));
            }
        }
        return dp[l][r][k];
    }
    int dp[100][100][100];  // initialized to 0, dp[left][right][k] means value from boxes[left]~boxes[right] followed by 
                            // k same color boxes. Follow does not mean strictly consecutive boxes, for example, 
                            // [1, 3, 2, 3, 4], 3 can be followed by the other 3 because we can remove 2 first.

---------------------
作者：魔豆Magicbean
来源：CSDN
原文：https://blog.csdn.net/magicbean2/article/details/78866298
版权声明：本文为博主原创文章，转载请附上博文链接！
---------------------
"""
class Solution:
    def removeBoxes(self, A):
        N = len(A)
        memo = [[[0] * N for _ in range(N)] for _ in range(N)]

        def dp(i, j, k):
            if i > j: return 0
            if not memo[i][j][k]:
                m = i
                while m + 1 <= j and A[m + 1] == A[i]:
                    m += 1
                i, k = m, k + m - i
                ans = dp(i + 1, j, 0) + (k + 1) ** 2
                for m in range(i + 1, j + 1):
                    if A[i] == A[m]:
                        ans = max(ans, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))
                memo[i][j][k] = ans
            return memo[i][j][k]

        return dp(0, N - 1, 0)

class Solution2:
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        N = len(boxes)
        self.boxes = boxes
        self.dp = [[[0] * N for _ in range(N)] for _ in range(N)]
        return self.search(0, N - 1, 0)

    def search(self, l, r, k):
        if l > r:
            return 0

        if self.dp[l][r][k]:
            return self.dp[l][r][k]

        while l < r and self.boxes[r] == self.boxes[r - 1]:
            r -= 1
            k += 1

        #Case 1
        self.dp[l][r][k] = self.search(l, r - 1, 0) + (k + 1) * (k + 1)

        #Case 2
        for i in range(l, r):
            if self.boxes[i] == self.boxes[r]:
                self.dp[l][r][k] = max(self.dp[l][r][k], self.search(l, i, k + 1) + self.search(i + 1, r - 1, 0))

        return self.dp[l][r][k]




