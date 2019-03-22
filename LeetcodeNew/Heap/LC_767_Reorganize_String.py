
"""
https://leetcode.com/problems/reorganize-string/discuss/113457/Simple-python-solution-using-PriorityQueue

Given a string S, check if the letters can be rearranged
so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
"""
"""
Find the count of each character, and use it to sort the string by count.

If at some point the number of occurrences of some character is greater than (N + 1) / 2, the task is impossible.

Otherwise, interleave the characters in the order described above."""

import heapq
import collections

class Solution00:
    def reorganizeString(self, S):
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            #This code turns out to be superfluous, but explains what is happening
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')

class Solution:
    def reorganizeString(self, S):
        res = ""
        heap = []
        counter = collections.Counter(S)
        #build a max heap
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))

        p_a, p_b = 0, ''
        while heap:
            a, b = heapq.heappop(heap)
            res += b
            if p_a < 0:
                heapq.heappush(heap, (p_a, p_b))
            a += 1
            p_a, p_b = a, b

        if len(res) != len(S): return ""
        return res


class Solution22:
    def reorganizeString(self, S):
        if len(S) == 1:
            return S
        count = collections.Counter(S)
        digit0 = max(count.keys(), key=lambda x: count[x])

        an = [digit0 for _ in range(count[digit0])]
        i = 0
        for digit in count:
            if digit != digit0:
                for _ in range(count[digit]):
                    an[i % len(an)] += digit
                    i += 1

        return ''.join(an) if i >= len(an) - 1 else ''




class Solution1:
    def reorganizeString(self, S):
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)/2: return ""
            A.extend(c * x)
        ans = [None] * N
        ans[::2], ans[1::2] = A[N/2:], A[:N/2]
        return "".join(ans)



class Solution2:
    def reorganizeString(self, S):
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            #This code turns out to be superfluous, but explains what is happening
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')

S = "aab"
a = Solution1()
print(a.reorganizeString(S))








