

"""
In a country popular for train travel, you have planned some train travelling one year in advance.
The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2,
then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.



Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.


Note:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000

"""
# Logic 1: Solving with Dynamic Programming
# This logic as inreference to the discuss thread - https://leetcode.com/problems/minimum-cost-for-tickets/discuss/228421/Python-solution

# Create dictionary for faster lookup of days

class Solution1:
    def mincostTickets(self, days, costs):

        dp=[0 for i in range(days[-1]+1)]

        for i in range(days[-1]+1):
             if i not in days:
                dp[i]=dp[i-1]
             else:
                dp[i]=min(dp[max(0,i-1)]  + costs[0],
                          dp[max(0,i-7)]  + costs[1],
                          dp[max(0,i-30)] + costs[2])
        return dp[-1]


"""
We construct a dp array with dp[i] recording the minimum cost up to days[i] (inclusive). 
We initialize dp[0] = costs[0], and iterate i in range(1, len(days)), for each i, we initialize a pointer j, 
and let it traverse backwards starting with i to find the first idx such that days[idx] is at least 1 day, 7 days, 
and 30 days ago respectively from days[i]. We find the minimum of the three values and let dp[i] be that value. 
Since for each i, j can go back by at most 30 indices, the total runtime is O(30*n) = O(n), and the space complexity is O(n).
"""


class Solution2:
    def mincostTickets(self, days, costs):
        n = len(days)
        dp = [0] * n
        dp[0] = costs[0]
        for i in range(1, n):

            # buy one-day ticket
            dp[i] = dp[i - 1] + costs[0]

            # what about buy seven-day ticket seven days ago
            j = i
            seven_ago = days[i] - 7
            while j >= 0 and days[j] > seven_ago:
                j -= 1
            if j >= 0:
                dp[i] = min(dp[i], dp[j] + costs[1])
            else:
                dp[i] = min(dp[i], costs[1])

            # what about buy thirty-day ticket thirty days ago
            thirty_ago = days[i] - 30
            while j >= 0 and days[j] > thirty_ago:
                j -= 1
            if j >= 0:
                dp[i] = min(dp[i], dp[j] + costs[2])
            else:
                dp[i] = min(dp[i], costs[2])

        return dp[-1]


"""
Another solution: We can initialize a dp array and fill in every entry between days[0] and days[-1] with the minimum costs up to the respective day. 
This will eliminate the need to use another pointer to traverse back to find the minimum costs 1 day, 7 days, and 30 days ago.

Time complexity: O(m), space complexity: O(m), where m is the range of days in days. 
We see that when days covers a wide range of days (m large n small), e.g., days = [1, 365], 
the first algorithm performs better, and when len(days) is large but covers a relative small range of days (n large m small), 
e.g., days = [4,6,8,9,10,12,15,20], the second algorithhm performs better.
"""

class Solution3:
    def mincostTickets(self, days, costs):
        dp = [0]*366
        j = 0
        for i in range(days[0], 366):
            if i == days[j]:
                dp[i] = dp[i-1] + costs[0]
                if i >= 7:
                    dp[i] = min(dp[i-7] + costs[1], dp[i])
                else:
                    dp[i] = min(dp[i], costs[1])
                if i >= 30:
                    dp[i] = min(dp[i-30] + costs[2], dp[i])
                else:
                    dp[i] = min(dp[i], costs[2])
                j += 1
                if j == len(days):
                    return dp[i]
            else:
                if i > 0:
                    dp[i] = dp[i-1]

class Solution4:
    def mincostTickets(self, days, costs):
        dp=[0]*366
        for d in range(366):
            if d not in days:
                dp[d]=dp[d-1]
                continue
            # 1-day pass on day d
            mincost=dp[d-1]+costs[0]
            # 7-day pass ending on or after day d
            mincost=min(mincost,dp[max(0,d-7)]+costs[1])
            # 30-day pass ending on or after day d
            mincost=min(mincost,dp[max(0,d-30)]+costs[2])
            dp[d]=mincost
        return dp[-1]


class Solution5:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        # min cost for travelling till day i
        dp = [float('inf')] * (days[-1] + 1)
        dp[0] = 0
        travel_days = set(days)
        for i in range(1, days[-1] + 1):
            if i not in travel_days:
                dp[i] = dp[i - 1]
            else:
                # 1-day pass
                dp[i] = min(dp[i], dp[i - 1] + costs[0])

                # 7-day pass
                if i <= 7:
                    dp[i] = min(dp[i], costs[1])
                else:
                    dp[i] = min(dp[i], dp[i - 7] + costs[1])

                # 30-day pass
                if i <= 30:
                    dp[i] = min(dp[i], costs[2])
                else:
                    dp[i] = min(dp[i], dp[i - 30] + costs[2])
        return dp[-1]

