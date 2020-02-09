'''
three windows size==k:w1,w2,w3,can just keep 3 adjacent windows move.
just like dp,since 3 is small, we can do it manually,
update maxw1 if w1>maxw1=> update maxw2 if maxw1+w2>maxw2=>update maxw3 if maxw2+w3>maxw3
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/166159/Clear-O(n)-Python
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/462642/Python-O(N)-1-pass-beats-100
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/203666/python-sliding-windows-O(n)O(1)

'''

class Solution:
    def maxSumOfThreeSubarrays(self,nums, k):
        w1,w2,w3=sum(nums[:k]),sum(nums[k:2*k]),sum(nums[2*k:3*k])
        mw1,mw2,mw3=w1,w1+w2,w1+w2+w3
        mw1index,mw2index,mw3index=[0],[0,k],[0,k,2*k]#mw1,mw2,mw3's index.
        for i in range(1,len(nums)-3*k+1):#last index for w1 window will be n-3k
            w1+=nums[i-1+k]-nums[i-1]
            w2+=nums[i-1+2*k]-nums[i-1+k]
            w3+=nums[i-1+3*k]-nums[i-1+2*k]
            if w1>mw1:
                mw1,mw1index=w1,[i]
            if mw1+w2>mw2:
                mw2,mw2index=mw1+w2,mw1index+[i+k]
            if mw2+w3>mw3:
                mw3,mw3index=mw2+w3,mw2index+[i+2*k]
        return mw3index


class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        best1 = 0
        best2 = [0, k]
        best3 = [0, k, 2 * k]

        sum1 = sum(nums[: k])
        sum2 = sum(nums[k: 2 * k])
        sum3 = sum(nums[2 * k: 3 * k])

        best_sum1 = sum1
        best_sum2 = sum1 + sum2
        best_sum3 = sum1 + sum2 + sum3

        p1, p2, p3 = 1, k + 1, 2 * k + 1
        while p3 <= len(nums) - k:
            sum1 = sum1 + nums[p1 + k - 1] - nums[p1 - 1]
            sum2 = sum2 + nums[p2 + k - 1] - nums[p2 - 1]
            sum3 = sum3 + nums[p3 + k - 1] - nums[p3 - 1]

            if sum1 > best_sum1:
                best1 = p1
                best_sum1 = sum1

            if best_sum1 + sum2 > best_sum2:
                best2 = [best1, p2]
                best_sum2 = best_sum1 + sum2

            if best_sum2 + sum3 > best_sum3:
                best3 = best2 + [p3]
                best_sum3 = best_sum2 + sum3

            p1 += 1
            p2 += 1
            p3 += 1

        return best3

"""
1, Convert nums to windws
That is, convert array of numbers into array of sum of windows. For example:

nums = [1, 2, 3], w_size = 2
windows = [1 + 2, 2 + 3] = [3, 5]
So the problem now is to choose 3 values from the window array and the difference of the indexes of these values must >=k

2, Define 3 arrays
take1[i]= biggest result we can get if only take 1 value from win[0] ... win[i]
take2[i]= biggest result we can get if only take 2 values from win[0] ... win[i]
take3[i]= biggest result we can get if only take 3 values from win[0] ... win[i]
3, Update 3 arrays dynamically
For take1, because only 1 window can be taken, so we just choose the current value or the previous value, depends on which one is bigger.
So take1[i] = max(take1[i - 1], win[i])

For take2, we need to select 2 windows, so we can either keep the previous selection, or we can take the current window and the biggest window in [0 ~ i - k], which is take1[i - k].
So take2[i] = max(take2[i - 1], win[i] + take1[i - k])

Same idea, take3[i] = max(take3[i - 1], win[i] + take2[i - k])

4, Remember the selection
If the problem is to return the biggest value, then step1~3 would be suffice, but we need to return the selection, so we need to remember not only the biggest value but also the index of selected window.

Just modify to array to be:

take = [value, [indexes]]
and when we update the value, we update the [indexes] too.

5, Code
"""

class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        subsum = sum(nums[:k])
        take1 = [(0, ()) for _ in range(len(nums))]
        take2 = [(0, ()) for _ in range(len(nums))]
        take3 = [(0, ()) for _ in range(len(nums))]

        for i in range(k - 1, len(nums)):
            subsum = subsum - nums[i - k] + nums[i]

            # update take 1
            if subsum > take1[i - 1][0]:
                take1[i] = (subsum, (i - k + 1,))
            else:
                take1[i] = take1[i - 1]

            # update take 2
            if subsum + take1[i - k][0] > take2[i - 1][0]:
                newval = subsum + take1[i - k][0]
                newidx = take1[i - k][1] + (i - k + 1,)
                take2[i] = (newval, newidx)
            else:
                take2[i] = take2[i - 1]

            # update take 3
            if subsum + take2[i - k][0] > take3[i - 1][0]:
                newval = subsum + take2[i - k][0]
                newidx = take2[i - k][1] + (i - k + 1,)
                take3[i] = (newval, newidx)
            else:
                take3[i] = take3[i - 1]

        return take3[-1][1]

    




