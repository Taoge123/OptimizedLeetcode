
"""
https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247543/O(n)-Java-Solution-using-sliding-window

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.
Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
"""

"""
Intuition
Translation:
Find the longest subarray with at most K zeros.

Explanation
For each A[j], try to find the longest subarray.
If A[i] ~ A[j] has zeros <= K, we continue to increment j.
If A[i] ~ A[j] has zeros > K, we increment i.
"""

class Solution1:
    def longestOnes(self, A, K):
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1


"""
change while K<0 to if K<0 save 50 ms ( totally 200 ms)
Because when j-i has reached maximum, 
such as [5,9], you don't bother to judge [6,9] [7,9] etc..
you can jump directly to [6,10]
"""

class Solution2:
    def longestOnes(self, A, K):
        res = i = 0
        for j in range(len(A)):
            K -= A[j] == 0
            if K < 0:
                K += A[i] == 0
                i += 1
            res = j - i + 1
        return res


"""
I think the question is a simplified version of 424. Longest Repeating Character Replacement
My solution is changed from Java 12 lines O(n) sliding window solution with explanation

public int longestOnes(int[] A, int K) {
        int zeroCount=0,start=0,res=0;
        for(int end=0;end<A.length;end++){
            if(A[end] == 0) zeroCount++;
            while(zeroCount > K){
                if(A[start] == 0) zeroCount--;
                start++;
            }
            res=Math.max(res,end-start+1);
        }
        return res;
    }
"""


"""
Question is basically a sliding window question.
Just register zero indexes in zeros array
Iterate over zeros array and find the max length of A array we can get by checking endpoints.
The bottleneck of the problem is finding the correct range of endpoints.
    For example if we can change 2 zeros to one, take into consideration of 4 consecutive index in zeros array.
    We can cover the length of 4th zero index - 1th zero index except those endpoints.
Finally, if we have change (K) more than zeros, just return length of A.
"""



