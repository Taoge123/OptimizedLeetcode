"""
1.
LC 198. House Robber
LC 213. House Robber II
LC 123.Best Time to Buy and Sell Stock III
LC 309.Best Time to Buy and Sell Stock with Cooldown
LC 376.Wiggle Subsequence
LC 276. Paint Fence
LC 1186. Maximum Subarray Sum with One Deletion
903.Valid Permutations for DI Sequence

2.
LC 300. Longest Increasing Subsequence
LC 368. Largest Divisible Subset
LC 1105. Filling Bookcase Shelves
983.Minimum Cost For Tickets

3.
LC1143: Longest Common Subsequences
LC1092: Shortest Common Supersequences
LC72: Edit Distance
LC97: Interleaving String
LC115. Distinct Subsequences
LC 727.Minimum Window Subsequence

LCS/SCS的变种：换汤不换药
LC 583. Delete Operation for Two Strings
问：从字符串s和t中总共最少删除多少个字符能使得它们相等。
LC 712. Minimum ASCII Delete Sum for Two Strings
问：从字符串s和t中总共最少删除多少ASCII码值的字符能使得它们相等。
LC 1035. Uncrossed Lines
两个数组s和t之间相等的数字可以连线。连线不能交叉。问最多可以有几条连线。

LC 1216. Valid Palindrome III
问一个字符串s最少删除多少个字符能变成回文串。
LC 1312. Minimum Insertion Steps to Make a String Palindrome
问一个字符串s最少需要添加多少个字符能变成回文串。

LC1092: Shortest Common Supersequences


4.
LC 1278. Palindrome Partitioning III
LC 813. Largest Sum of Averages
LC 410. Split Array Largest Sum
LC 1335. Minimum Difficulty of a Job Schedule

5.
LC 516. Longest Palindromic Subsequence
LC 312. Burst Balloons
LC 375. Guess Number Higher or Lower II
LC 1246. Palindrome Removal

6.
LC 494. Target Sum
LC 1049. Last Stone Weight II
LC 474.Ones and Zeroes
LC 879. Profitable Schemes
LC 956. Tallest Billboard
518.Coin Change 2

状态压缩
LC 691. Stickers to Spell Word
LC 1125. Smallest Sufficient Team
LC 1349. Maximum Students Taking Exam
943.Find the Shortest Superstring


1 & 2
LC 1000. Minimum Cost to Merge Stones
546.Remove Boxes

弃坑型：887.Super Egg Drop, 920.Number of Music Playlists


DP套路(1): 第一类基本型

LC 213. House Robber II
0:这轮我抢的最大收益
1:这轮我不抢的最大收益

for (int i=1; i<=N; i++)
            {
                dp[i][0] = dp[i-1][1]+val[i];
                dp[i][1] = max(dp[i-1][0], dp[i-1][1])
            }

	Ans = max (dp[N][0], dp[N][1])


LC 123.Best Time to Buy and Sell Stock III
for (int i=1; i<=N; i++)
            {
                dp[i][0] = max(dp[i-1][0], -val[i]);
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]+val[i])
                dp[i][2] = max(dp[i-1][2], dp[i-1][1]-val[i])
                dp[i][3] = max(dp[i-1][3], dp[i-1][2]+val[i])
            }

	 Ans = max {dp[N][i]}  (i=0,1,2,3)



LC 309.Best Time to Buy and Sell Stock with Cooldown
for (int i=1; i<=N; i++)
            {
                dp[i][0] = max(dp[i-1][2]-val[i]);
                dp[i][1] = max(dp[i-1][1], dp[i-1][0])
                dp[i][2] = max(dp[i-1][2], dp[i-1][1]+val[i])
   	   }

	 Ans = max {dp[N][i]}  (i=0,1,2,3)


LC 376.Wiggle Subsequence
for (int i=1; i<=N; i++)
            {
	       if (nums[i] < nums[i-1])
                	dp[i][0] = dp[i-1][1] + 1;
	       if (nums[i] < nums[i-1])
                	dp[i][1] = dp[i-1][0] + 1;
   	   }

	 Ans = max {dp[N][i]}  (i=0,1)


LC 276. Paint Fence

for (int i=1; i<=N; i++)
            {
	       dp[i][j] = min { dp[i-1][j’] } + cost[i][j]; (j’=1,2,3..,K but j’!=j)
   	   }

	 Ans = min {dp[N][j]}  (i=0,1,2,...,K)

思考题
给N个房子，涂白色和涂黑色的花费分别是a,b。要求不能有连续三间房子涂同一种颜色。求喷涂所有房子的最小价格。
0: 结尾有连续1间为黑色  <= 2,3 + black
1: 结尾有连续2间为黑色  <= 0 + black
2: 结尾有连续1间为白色 <= 0,1 + white
3: 结尾有连续2间为白色 <= 2 + white


LC 487. Max Consecutive Ones II

for (int i=1; i<=N; i++)
{
	       if (nums[i]==0) {
                	 dp[i][1] = dp[i-1][0]+1;
                	 dp[i][0] = 0;
                 }
                 else {
                	 dp[i][0] = dp[i-1][0]+1;
                	 dp[i][1] = dp[i-1][1]+1;
                 }
   	   }

	 Ans = max {dp[i][j]}
(for all possible i and j=0,1)


LC 1186. Maximum Subarray Sum with One Deletion

for (int i=1; i<=N; i++)
{
	dp[i][0] = max(dp[i-1][0] + nums[i], nums[i]);

         dp[i][1] =  max(dp[i-1][0], dp[i-1][1] + nums[i]);
}

Ans = max {dp[i][j]}
(for all possible i and j=0,1)




"""






