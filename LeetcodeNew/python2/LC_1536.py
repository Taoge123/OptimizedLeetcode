"""
zeros[i] : how many trailling zeros in the i-th row
6 * 6

zeros : 1 3 3 6 4 7
target: 6 5 4 3 2 1

zeros_news[i] >= target[i]

plan A: -> 5 steps
[7] 1 3 3 [6] 4

plan B: -> 3 steps -> 1 step
6 1 3 3 4 7
[6] 1 3 3 [7] 4



"""


class Solution:
    def minSwaps(self, grid) -> int:
        n = len(grid)
        zeros = [0] * n
        for i in range(n):
            count = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] != 0:
                    break
                count += 1
            zeros[i] = count

        count = 0
        for i in range(n):
            target = n - 1 - i
            j = i
            while j < n:
                # 已经>=target， 直接下一个
                if zeros[j] >= target:
                    break
                j += 1
            # 找不到>=target的, 那就不行了
            if j == n:
                return -1
            # 找到了j我们就需要挪j-i次
            count += j - i
            # 暴力去挪, 存下j行
            temp = zeros[j]
            # 暴力挪到了i的位置
            for k in range(j, i - 1, -1):
                zeros[k] = zeros[k - 1]
            zeros[i] = temp
        return count



