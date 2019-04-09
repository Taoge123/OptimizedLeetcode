
"""
https://blog.csdn.net/fuxuemingzhu/article/details/79404220

A sequence of number is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""

class Solution1:
    def numberOfArithmeticSlices(self, A):

        opt, i = [0, 0], 1
        for j in range(2, len(A)):
            if A[j] - A[j - 1] == A[j - 1] - A[j - 2]:
                opt.append(opt[j - 1] + i)
                i += 1
            else:
                opt.append(opt[j - 1])
                i = 1
        return opt[-1]



class Solution2:
    def numberOfArithmeticSlices(self, A):

        ans = 0
        k = 2
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                k += 1
                if i == len(A)-1:
                    ans += (k-1)*(k-2)//2
            else:
                if k > 2:
                    ans += (k-1)*(k-2)//2
                k = 2
        return ans



class Solution3:
    def numberOfArithmeticSlices(self, A):
        # equal difference array,min length==3
        # 1 3 5->7
        # dp[i]=dp[i-1]+S(i),S(i):when A[i]-A[i-1]==A[i-1]-A[i-2],S(i)=
        n = len(A)
        if n <= 2:
            return 0
        dp = [0] * n  # dp[i] means numbers of end by A[i]'s arithmetic slic.
        for end in range(2, n):
            if A[end] - A[end - 1] == A[end - 1] - A[end - 2]:
                dp[end] = dp[end - 1] + 1
        return sum(dp)


"""
There won't be any intercept between sequences as their increase ratio will differ. 
Otherwise, we can merge both sequence. We will simply add arithmetic sequences 
when increase between current and previous element breaks sequnce increase.

- if length of list less than 3, we cannot create sequence, so return 0
- Add dummy infinity tail to list for breaking arithmetic sequence for checking untill last element
- Initialize arithmetic increase, start index of sequence, and result
- Starting from index 2, if increase breaks sequence rule, check how many seq. slices can be added
- Update new start index and arithmetic increase
- Return result
"""
class Solution4:
    def numberOfArithmeticSlices(self, A):
        if len(A) < 3:
            return 0
        A.append(float("inf"))
        d, l, n, res = A[1] - A[0], 0, len(A), 0
        for i in range(2, n):
            if d != A[i] - A[i - 1]:
                diff = i - l - 2
                if diff > 0:
                    res += diff * (diff + 1) // 2
                d, l = A[i] - A[i - 1], i - 1
        return res


"""
a means the number of slice which NOT end with A[i]
b means the number of slice which ends with A[i]
"""
class Solution5:
    def numberOfArithmeticSlices(self, A):
        if len(A) < 3:return 0
        a,b= 0,0
        for i in range(2,len(A)):
            a,b = a+b,[0,b+1][A[i]-A[i-1]==A[i-1]-A[i-2]]
        return a+b


"""
Solution
Find every at least length > 3 A.P. (arithmetic progression)

And in the case of example, we can found that if there is a 4 length A.P. . 
Count of all sub-A.P. will be (n-1)(n-2)/2 .
"""

"""
我的想法是通过扫描一遍数组就能得到结果，所以得先知道如果扫描发现下一个数字能够加入到等差数列中，那么总的数目会有怎样的变化。
因此，我列出了下表：

数组	        等差数列的数目	    与上一数组的等差数列数目比较
1 2 3	            1	                    1 - 0 = 1
1 2 3 4	            3	                    3 - 1 = 2
1 2 3 4 5	        6	                    6 - 3 = 3
1 2 3 4 5 6	        10	                    10 - 6 = 4
1 2 3 4 5 6 7	    15	                    15 - 10 = 5
1
2
3
4
5
6
可以看出等差数列的数目是二阶等差数列。

观察就能发现两个等差数列数目之差（表格第三列）就是[1,2, 3, 4, 5……]这个序列，因此每次增加一个等差数列的元素，
总的等差数列的数目就会增加[1,2, 3, 4, 5……]中对应的数值。

按照这一点，在代码实现时就设置一个变量addend，表示增加的数目，它对应着[1,2, 3, 4, 5……]这个序列，
如果下一个数组元素能够加入到等差数列中，addend就自增1，然后总的数目就增加addend。
如果下一个数组元素不能加入到等差数列中，addend就重置为0。这样通过一个循环就能获得结果。

为什么要把addend设置成0呢？因为题目要求能构成等差数列的子串的数目。设置成0开始计算后面的子串能够成等差数列的数目了。

时间复杂度是O(N)
"""

class Solution6:
    def numberOfArithmeticSlices(self, A):

        count = 0
        addend = 0
        for i in range(len(A) - 2):
            if A[i + 1] - A[i] == A[i + 2] - A[i + 1]:
                addend += 1
                count += addend
            else:
                addend = 0
        return count


# 二刷，上面的做法其实就是DP的空间复杂度优化，真正的DP方法如下：
class Solution7:
    def numberOfArithmeticSlices(self, A):

        N = len(A)
        dp = [0] * N
        for i in range(1, N - 1):
            if A[i - 1] + A[i + 1] == A[i] * 2:
                dp[i] = dp[i - 1] + 1
        return sum(dp)








