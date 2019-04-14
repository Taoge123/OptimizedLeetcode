
"""
Given an array of integers A, find the number of triples of indices (i, j, k) such that:

0 <= i < A.length
0 <= j < A.length
0 <= k < A.length
A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.


Example 1:

Input: [2,1,3]
Output: 12
Explanation: We could choose the following i, j, k triples:
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2

Note:

1 <= A.length <= 1000
0 <= A[i] < 2^16
"""

"""
I didn't figure this problem out during contest and solved it after contest ends.
After went through discussion, it seems there is no similar solution, so here is the code.
It might be not the fastest, hope you can find it helpful.

basic idea is:
since our goal requires you to select three numbers and make sure there is at least one "0" in each bit's three digits pool ( under binary form ).
thus we can convert this problem to be: find the total count of combinations where each bit's three digits pool is all "1".
finally return N^3 - count

steps are as follows:

convert each number into binary
loop each column and collect row index in set once you meet a "1"
loop each column again and update Venn diagram, here I put an example here:
suppose input = [2, 4, 7, 3]
we know that pool = ["010", "100", "111", "011"]
and one = {0: {1,2}, 1: {0,2,3}, 2: {2,3}}
Venn is initialized as defaultdict(list), and cnt = 0
now we start to update Venn diagram:

firstly we are at j = 0
cnt becomes 2^3
Venn[1] = [ {1,2} ]

then we are at j = 1
cnt change from 2^3 to be 2^3 + 3^3
(since we have three number with 1-th bit is "1", there is 3^3 combinations to fill three "box", 
however the intersection of 2^3 and 3^3 are counted twice, so we need to vanish the effect of intersection: one[0] & one[1] = {2} )
cnt change from 2^3 + 3^3 to be 2^3 + 3^3 - ( len( {2} ) )^3, it is 34
Venn[2] = [ {2} ] and Venn[1] = [ {1, 2}, {0,2,3} ]

lastly, we are at j = 2
cnt change from 34 to 34 + 2^3 = 42
next we remove the effect of intersecion between one[2] and each earlier set in Venn
1. for Venn[1]: one[2] & {1,2} = {2} and one[2] & {0,2,3} = {2,3}, so cnt updates to be 42-1-8 = 33
2. for Venn[2]: one[2] & {2} = {2}, so cnt updates to be 33 + 1 = 34 (pay attention to the "+" sign)
so finally, we return 4^3 - 34 = 30, that is what this problem requires.

last note:

for the sign problem above, for odd-th operation it is "-", for even-th operation it is "+", which follows the Venn Diagram rule.
for the order of updating, we can NOT update in ascending order, 
because when we are looping Venn[i], we are appending new results into Venn[i+1]. 
therefore we should use descending order when updating Venn dictionary.
code is here.
for clear, I didn't make it concise for example combining "for" loops etc.
thanks for your time, everyone.
"""

import collections

class Solution1:
    def countTriplets(self, A: 'List[int]') -> 'int':

        tmp = []
        maxlen = 0
        for a in A:
            tmp.append(bin(a)[2:])
            maxlen = max(maxlen, len(tmp[-1]))
        pool = []
        for s in tmp:
            extra = maxlen - len(s)
            pool.append('0' * extra + s)

        row, col = len(pool), len(pool[0])
        one = collections.defaultdict(set)
        for j in range(col):
            for i in range(row):
                if pool[i][j] == '1':
                    one[j].add(i)

        Venn = collections.defaultdict(list)
        cnt = 0
        for j in range(col):
            if len(one[j]) != 0:
                cnt += (len(one[j])) ** 3
                for i in range(j, 0, -1):
                    for prv in Venn[i]:
                        intersec = prv & one[j]
                        if len(intersec) != 0:
                            cnt += ((-1) ** i) * (len(intersec)) ** 3
                            Venn[i + 1].append(intersec)
                Venn[1].append(one[j])

        return row ** 3 - cnt


"""
Great idea, I was thinking of building a size-65536 directed acyclic graph 
and count the occurrence of the descendant for each node, 
but failed to come up with a efficient algorithm to deal with the over count. 
Your method using inclusion-exclusion principle is much better, thanks for sharing.

Here is my shorter implementation
"""

from math import ceil, log2

class Solution2:
    def countTriplets(self, A: 'List[int]') -> 'int':
        n, d = len(A), ceil(log2(max(A) + 1))
        aux = {j: {i for i, a in enumerate(A) if a & (1 << j)} for j in range(d)}

        Venn, cnt = collections.defaultdict(list), 0
        for j, one in aux.items():
            if len(one) == 0: continue
            cnt += len(one) ** 3
            for i in range(j, 0, -1):
                overlap = [prv & one for prv in Venn[i]]
                cnt += (-1) ** i * sum(len(x) ** 3 for x in overlap if x)
                Venn[i + 1] += [x for x in overlap if x]
            Venn[1].append(one)

        return n ** 3 - cnt


class Solution3Slow:
    class Solution:
        def countTriplets(self, A: 'List[int]') -> 'int':
            N = len(A)
            ans = 0
            count = collections.Counter()

            for i in range(N):
                for j in range(N):
                    count[A[i] & A[j]] += 1

            for k in range(N):
                for v in count:
                    if A[k] & v == 0:
                        ans += count[v]
            return ans

class SolutionSlow2:
    def countTriplets(self, A: 'List[int]') -> 'int':
        multi = collections.defaultdict(int)

        for i in range(len(A)):
            for j in range(len(A)):
                multi[A[i] & A[j]] += 1

        ans = 0
        for i in range(len(A)):
            for key in multi.keys():
                if key & A[i] == 0:
                    ans += multi[key]

        return ans



"""
题目大意
找出给定的数组中，有多少个三元组，使得这个三元组的位与等于0.

解题方法
看了下数组长度是1000，大概分析下这个题目的时间复杂度是O(N^2×log(N))以下。
同时注意到三元组的顺序并无要求，即同样的组合可能出现多次。

一个最省事的做法就是，先两重循环，计算任意两个数字之间的位与结果是多少，存储到字典中，
字典中保存的是位与出现的次数。然后再次对数组每个位置进行遍历，同时遍历字典中的每个元素，
即可分析出任意三个数字位与的结果和次数。

唯一需要注意的是字典保存的是两个数字位与后的结果出现的次数，
当第三个数字和两位数字位与结果进行位与的结果是0的时候，需要次数累加。

这个时间复杂度怎么分析？注意题目给出的每个元素的大小是216，
所以两个数字位与的结果不会超过216。因此，总的时间复杂度是O(N^2 + 2^16 * N).
"""


class Solution3:
    def countTriplets(self, A):
        dic = {}
        for i in A:
            for j in A:
                v = i & j
                dic[v] = dic.setdefault(v,0) + 1
        res = 0
        for i in A:
            for k,v in dic.items():
                if i & k == 0:
                    res += v
        return res



