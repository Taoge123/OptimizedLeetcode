
# O(n*3) space
def minCost1(self, costs):
    if not costs:
        return 0
    r, c = len(costs), len(costs[0])
    dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
    dp[0] = costs[0]
    for i in xrange(1, r):
        dp[i][0] = costs[i][0] + min(dp[ i -1][1:3])
        dp[i][1] = costs[i][1] + min(dp[ i -1][0], dp[ i -1][2])
        dp[i][2] = costs[i][2] + min(dp[ i -1][:2])
    return min(dp[-1])

# change original matrix
def minCost2(self, costs):
    if not costs:
        return 0
    for i in xrange(1, len(costs)):
        costs[i][0] += min(costs[ i -1][1:3])
        costs[i][1] += min(costs[ i -1][0], costs[ i -1][2])
        costs[i][2] += min(costs[ i -1][:2])
    return min(costs[-1])

# O(1) space
def minCost3(self, costs):
    if not costs:
        return 0
    dp = costs[0]
    for i in xrange(1, len(costs)):
        pre = dp[:] # here should take care
        dp[0] = costs[i][0] + min(pre[1:3])
        dp[1] = costs[i][1] + min(pre[0], pre[2])
        dp[2] = costs[i][2] + min(pre[:2])
    return min(dp)

# O(1) space, shorter version, can be applied
# for more than 3 colors
def minCost(self, costs):
    if not costs:
        return 0
    dp = costs[0]
    for i in xrange(1, len(costs)):
        pre = dp[:] # here should take care
        for j in xrange(len(costs[0])):
            dp[j] = costs[i][j] + min(pre[:j ] +pre[ j +1:])
    return min(dp)


