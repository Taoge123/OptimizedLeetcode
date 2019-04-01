
"""
https://leetcode.com/problems/interval-list-intersections/solution/
https://blog.csdn.net/fuxuemingzhu/article/details/87729287

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is either empty,
or can be represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution1:
    def intervalIntersection(self, A, B):
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i].start, B[j].start)
            hi = min(A[i].end, B[j].end)
            if lo <= hi:
                ans.append(Interval(lo, hi))

            # Remove the interval with the smallest endpoint
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1

        return ans


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        思路：
        S表示start， E表示end
        1. 建立一个栈s
        2. 遇到S，将s入栈，遇到E，s最上层pop出来
        3. 那么s栈内存在三种情况：空，一个S，两个S，不会出现三个（因为接下来必会遇到E）
        4. 如果s栈内有两个S，那么[S,E]是交集，如果只一个S，那么不是交集，直接扔掉
        """
        if not A or not B:
            return []
        a = []
        b = []
        s = []
        ret = []
        # 为了使用栈结构，反向
        A.reverse()
        B.reverse()
        while (A or a) and (B or b):
            if not a:
                a = A.pop()
                # 为了使用栈结构，先start 后end
                a = [a.end, a.start]
            if not b:
                b = B.pop()
                # 为了使用栈结构，先start 后end
                b = [b.end, b.start]
            c = a
            if a[-1] < b[-1]:
                c = a
            elif a[-1] > b[-1]:
                c = b
            else:
                # 如果值相等的话，优先使用start，也就是len()==2
                c = a if len(a)==2 else b
            if len(c)==2:
                s.append(c.pop())
            else:
                num = s.pop()
                num_end = c.pop()
                if len(s):
                    ret.append([num, num_end])
                else:
                    # 非交集，扔掉
                    pass
        return ret


"""
Inspired from finding the intersection of two sorted array, 
here we use two pointers to compare two sorted interval array.

Create the new Interval: the new start should be the maximum of two intervals 
and the new end should be the minimum of two intervals.
(If the new interval is vaild where end >= start, then we add it into our result)

Move the pointer: we are supposed to move the pointer whose end is smaller, 
since the larger one is likely to create a new interval with the next interval of the smaller one.
"""

class Solution3:
    def intervalIntersection(self, A, B):
        res = []
        i = j = 0
        while (i < len(A) and j < len(B)):
            it = Interval(max(A[i].start, B[j].start), min(A[i].end, B[j].end))
            if (it.start <= it.end):
                res.append(it)
            if A[i].end > B[j].end:
                j += 1
            else:
                i += 1
        return res




