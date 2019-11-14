class Solution:
    def maxProfit(self, prices):


        n = len(prices)
        ans = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]

        return ans


"""[7,1,5,3,6,4]

dp=[           ] 


"""

"""
  [7,1,5,3,6,4]
1  0 0 4 4 5 5      for k in range(i): max(dp[i][j-1], price[i] - price[k]) 
2  0 0 4 4 7 7      for k in range(i): max(dp[i][k]+price[j] - price[k] ])
3  0 0 4 4 7 7
4  0
5  0 


"""
