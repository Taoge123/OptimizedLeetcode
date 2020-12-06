"""
1262. Greatest Sum Divisible by Three
https://leetcode.com/problems/greatest-sum-divisible-by-three/

dfs + memo
https://leetcode.com/problems/largest-multiple-of-three/discuss/517755/dfs%2Bmemo-(c%2B%2B)

solution 1:
if totalsum%3 == 0: select all digits
if totalsum%3 == 1:
    exclude the smallest element (%3==1)
    exclude two smallest element (%3==2)
if totalsum%3 == 2:
    exclude the smallest element (%3==2)
    exclude two smallest element (%3==1)


solution2: DP
dp[i][j] : the largest string (%3=j) we can construct using digits[1:i]

X X X X X i
dp[i][0]
dp[i][1]
dp[i][2]

1. do not pick digits[i]
    dp[i][j] = dp[i-1][j]
2. pick digits[i] (k==digits[i]%3)
    dp[i][j] = dp[i-1][j-k] + digits[i]

    dp[i][j] = better(dp[i-1][j], dp[i-1][j-k] + digits[i])

return dp[n][0]


Basic Math
999....999 % 3 == 0
1000....000 % 3 == 1
a000....000 % 3 == a % 3
abcdefghijk % 3 == (a+b+c+..+i+j+k) % 3


Explanation
Calculate the sum of digits total = sum(A)
If total % 3 == 0, we got it directly
If total % 3 == 1 and we have one of 1,4,7 in A:
we try to remove one digit of 1,4,7
If total % 3 == 2 and we have one of 2,5,8 in A:
we try to remove one digit of 2,5,8
If total % 3 == 2:
we try to remove two digits of 1,4,7
If total % 3 == 1:
we try to remove two digits of 2,5,8
Submit

Complexity
Time O(nlogn), where I use quick sort.
We can also apply counting sort, so it will be O(n)
Space O(sort)

"""


import collections


class Solution:
    def largestMultipleOfThree(self, nums):
        total = sum(nums)
        count = collections.Counter(nums)
        nums.sort(reverse=True)

        def f(i):
            if count[i]:
                nums.remove(i)
                count[i] -= 1
            if not nums:
                return ''
            if not any(nums):
                return '0'
            if sum(nums) % 3 == 0:
                return ''.join(map(str, nums))

        if total % 3 == 0:
            return f(-1)
        if total % 3 == 1 and count[1] + count[4] + count[7]:
            return f(1) or f(4) or f(7)
        if total % 3 == 2 and count[2] + count[5] + count[8]:
            return f(2) or f(5) or f(8)
        if total % 3 == 2:
            return f(1) or f(1) or f(4) or f(4) or f(7) or f(7)
        return f(2) or f(2) or f(5) or f(5) or f(8) or f(8)




class SolutionSort:
    def largestMultipleOfThree(self, digits) -> str:
        digits.sort(reverse=True)
        buket = [[], [], []]
        total = 0
        for i in digits:
            buket[i % 3].append(i)
            total += i
        remain = total % 3
        if remain:
            if buket[remain]:
                buket[remain].pop()
            elif len(buket[-remain]) > 1:
                buket[-remain].pop()
                buket[-remain].pop()
        res = []
        res += buket[0] + buket[1] + buket[2]
        res.sort(reverse=True)
        if len(res) == 0:
            return ""
        if res[0] == 0:
            return "0"
        return "".join(str(i) for i in res)




