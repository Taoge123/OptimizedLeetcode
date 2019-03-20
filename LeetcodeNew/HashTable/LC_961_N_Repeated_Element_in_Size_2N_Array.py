
"""
In a array A of size 2N, there are N+1 unique elements,
and exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""
import collections


class Solution1:
    def repeatedNTimes(self, A):
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k


class Solution2(object):
    def repeatedNTimes(self, A):
        for k in range(1, 4):
            for i in range(len(A) - k):
                if A[i] == A[i+k]:
                    return A[i]



class Solution3:
    def repeatedNTimes(self, A):
        print(collections.Counter(A))
        return collections.Counter(A).most_common(1)[0][0]

"""
a = collections.Counter(A)
a
Counter({5: 4, 1: 1, 2: 1, 3: 1, 4: 1})
a.most_common(1)
[(5, 4)]
a.most_common(1)[0]
(5, 4)
a.most_common(1)[0][0]
"""
Input = [5,1,5,2,5,3,5,4]
a = Solution3()
print(a.repeatedNTimes(Input))



