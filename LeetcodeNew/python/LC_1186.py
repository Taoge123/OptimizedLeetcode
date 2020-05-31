"""
487. Max Consecutive Ones II
https://www.youtube.com/watch?v=NUjks0ZZBrg
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/discuss/377424/Simple-Python-DP-solution
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/discuss/378081/python-dp-solution

similar to maximum sum dp solution.
1:dp[i]=max(dp[i-1]+arr[i],arr[i])
2:dp1:ith end with one more deletion,ith end with no delete. dp0 still keep original formula.
delete happen in i or not in i=> dp1[i]=max(dp1[i-1]+arr[i],dp0[i-1])


"""


class Solution:
    def maximumSum(self, arr) -> int:
        if all(x <= 0 for x in arr):  # directly deal with corner case.
            return max(arr)

        n = len(arr)
        no_delete = [arr[i] for i in range(n)]
        delete = [0] * n

        for i in range(1, n):
            #no_delete is eligible to add the current and restart
            no_delete[i] = max(no_delete[i - 1] + arr[i], arr[i])
            #delete arr[i] then its no_delete[i - 1]
            #if i wanna delete from 0 - i-1, then its delete[i - 1] + arr[i]
            delete[i] = max(delete[i - 1] + arr[i], no_delete[i - 1])

        return max(delete + no_delete)



class Solution2:
    def maximumSum(self, arr):
        if all(x<=0 for x in arr):#directly deal with corner case.
            return max(arr)
        n = len(arr)
        res = no_delete = arr[0]
        delete = 0
        for i in range(1, n):
            delete = max(delete + arr[i], no_delete)
            #no_delete is identical to no regular
            no_delete = max(no_delete + arr[i], arr[i])
            res = max(delete, no_delete , res)
        return res

