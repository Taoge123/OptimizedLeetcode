"""
https://www.youtube.com/watch?v=xFlO0H1l2oQ

Key point
Don't calculate the score for K=0, we don't need it at all.
(I see almost all other solutions did)
The key point is to find out how score changes when K++

Time complexity:
“A will have length at most 20000.”
I think it means you should find a O(N) solution.

How dosen score change when K++ ?

Get point
Each time when we rotate, we make index 0 to index N-1, then we get one more point.
We know that for sure, so I don't need to record it.

Lose point
(i - A[i] + N) % N is the value of K making A[i]'s index just equal to A[i].
For example, If A[6] = 1, then K = (6 - A[6]) % 6 = 5 making A[6] to index 1 of new array.
So when K=5, we get this point for A[6]
Then if K is bigger when K = (i - A[i] + 1) % N, we start to lose this point, making our score -= 1
All I have done is record the value of K for all A[i] where we will lose points.

A[i]=0
Rotation makes no change for it, becasue we alwars have 0 <= index.
However, it is covered in "get point" and "lose point".

Explanation of codes

Search the index where score decrease and record this changement to a list change.
A simple for loop to calculate the score for every K value.
score[K] = score[K-1] + change[K]
In my codes I accumulated changes so I get the changed score for every K value compared to K=0
Find the index of best score.
"""

"""
val <= index, then get points

0123456
xxxx2xx
2222222    
0011111


A[i] <= i
0:           111....
i-(A[i]-1):  000....
i+1       :  111....

diff[k]: the score difference between moving k steps and moving k-1 steps
0 <= k < n
diff[0] += 1
diff[i-(A[i]-1)] -= 1
diff[i+1] += 1


"""


class Solution:
    def bestRotation(self, nums) -> int:
        n = len(nums)
        # [0, n-1]
        diff = [0] * n
        for i in range(n):
            if nums[i] <= i:
                diff[0] += 1
                diff[(i - nums[i] + 1) % n] -= 1
                diff[(i + 1) % n] += 1
            else:
                diff[0] += 0
                diff[(i + 1) % n] += 1
                diff[(i + 1 + n - nums[i]) % n] -= 1

        score = 0
        max_score = 0
        res = 0
        for i in range(n):
            score += diff[i]
            if score > max_score:
                max_score = score
                res = i
        return res








