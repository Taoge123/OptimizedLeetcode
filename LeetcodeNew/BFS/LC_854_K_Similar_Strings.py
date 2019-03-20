
"""
Strings A and B are K-similar (for some non-negative integer K)
if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

Input: A = "ab", B = "ba"
Output: 1
Example 2:

Input: A = "abc", B = "bca"
Output: 2
Example 3:

Input: A = "abac", B = "baca"
Output: 2
Example 4:

Input: A = "aabc", B = "abca"
Output: 2
Note:

1 <= A.length == B.length <= 20
A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}


"""


"""
The trick in this BFS is how to find all necessary neighbors efficiently.
"""
import collections

class Solution:
    def kSimilarity(self, A, B):

        # remove all equal characters in the same indexes before BFS
        A_chars, B_chars = [], []
        for a, b in zip(A, B):
            if a != b:
                A_chars.append(a)
                B_chars.append(b)
        A = "".join(A_chars)
        B = "".join(B_chars)

        def get_neighbors(s):
            res = []
            for i in range(len(s) - 1):
                # find the first mismatch index
                if s[i] == B[i]:
                    continue
                # find all possible chars to fix the first mismatch index
                for j in range(i + 1, len(s)):
                    if s[j] != B[j] and s[j] == B[i]:
                        res.append(s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
                break
            return res

        queue, res, seen = [A], 0, set([A])
        while queue:
            new_queue = []
            for s in queue:
                if s == B:
                    return res
                for nei in get_neighbors(s):
                    if nei not in seen:
                        seen.add(nei)
                        new_queue.append(nei)
            queue = new_queue
            res += 1


class Solution2:
    def kSimilarity(self, A, B):
        if A == B: return 0
        dq, seen, step, n = collections.deque([A]), {A}, 0, len(A)
        while dq:
            sz = len(dq)
            for _ in range(sz):
                cur, i = dq.popleft(), 0
                while i < n and cur[i] == B[i]: i += 1
                for j in range(i + 1, n):
                    if B[j] != cur[i] or cur[j] == B[j]: continue
                    nxt = cur[ : i] + cur[j] + cur[i + 1: j] + cur[i] + cur[j + 1: ]
                    if nxt not in seen:
                        seen.add(nxt)
                        if nxt == B: return step + 1
                        dq.append(nxt)
            step += 1

"""
The idea is, find the first character i where A[i] != B[i] , 
then swap it with all occurrence of B[i] in A, and see which produce the smallest answer.

"""

class Solution2:
    def kSimilarity(self, A, B):
        return self.helper(A, B, {})

    def helper(self, A, B, mem):
        if A == B:
            return 0

        if A in mem:
            return mem[A]

        ans = float('inf')
        i = 0
        # find first i where A[i] != B[i]
        while A[i] == B[i]:
            i += 1

        diffChar = B[i]
        for j, c in enumerate(A[i:], i):
            if c == diffChar:
                # find the smallest answer after each swap
                ans = min(ans, 1 + self.helper(A[i + 1:j] + A[i] + A[j + 1:], B[i + 1:], mem))
        mem[A] = ans
        return ans

"""
https://leetcode.com/problems/k-similar-strings/discuss/241213/Python-solution-with-lots-of-thinking

This is about transform the question to others

we don't care the order of A and B, only the revalent order matters
we don't care in a position i that A[i]==B[i]
So we can transform A and B to a 6*5 matrix
Ds = {c:{} for c in "abcdef"}
for a, b in zip(A, B):
	if a != b:
		if b not in Ds[a]:
			Ds[a][b] = 0
		Ds[a][b] += 1
		
		
		
The problem is transformed into a Graph, each edge (a,b) represent
that a character a at A that should be b in the end of the swaps
So let's consider a character a, which is in the position of b. 
It will go travel around and end up in position a. So the total swaps should be a sum of directed loops
for example, if we have A='abc' and B='bca', there is a loop in the Graph a->b, b->c, c->a, 
we can solve the problem by 2 swaps as the loop is of size 3
If we have E edges in the Graph, and the Graph can be split into P loops, 
we can solve the problem in E-P swaps

Then it is a problem of how many loops can you find in the Graph.
We can get any loop in the Graph by this:

"""

def getLoop(Ds):
	paths = [(
		(i, j), Ds[i][j]
	) for i in Ds for j in Ds[i]]
	while paths:
		path, l = paths.pop()
		i, j = path[0], path[-1]
		if i in Ds[j]:
			yield path, min(l, Ds[j][i])
		for k in Ds[j]:
			if k not in path:
				paths.append((path+(k,), min(l, Ds[j][k])))


"""
we can DFS/BFS to find the maximum number of loops

By the way, if there exists a path of length 2, we can greedily take it. As it only has 2 edges, it would at most break 2 loops and force them to be 1 loop. 1+1 = 2
Unfortunitely, for loop of length 3 or larger, we cannot greedily take it. It has 3 edges and may break 3 loops and force them to be 1 loop. 1+1<3

ans = 0
for aid in range(6):
	for bid in range(aid):
		a, b = "abcdef"[aid], "abcdef"[bid]
		if b in Ds[a] and a in Ds[b]:
			ans += min(Ds[a][b], Ds[b][a])
			if Ds[a][b] > Ds[b][a]:
				Ds[a][b] -= Ds[b][a]
				del Ds[b][a]
			elif Ds[a][b] < Ds[b][a]:
				Ds[b][a] -= Ds[a][b]
				del Ds[a][b]
			else:
				del Ds[b][a]
				del Ds[a][b]
"""
"""

def findMaxLoops(Ds):
	ans = 0
	for path, l in getLoop(Ds):
		DsN = {i:{j:Ds[i][j] for j in Ds[i]} for i in Ds}
		for i, j in zip(path, path[1:]+path[:1]):
			DsN[i][j] -= l
			if DsN[i][j] == 0:
				del DsN[i][j]
				if not Ds[i]:
					del Ds[i]
		ans = max(ans, findMaxLoops(DsN) + l)
	return 0 if ans == None else ans
NN = sum(Ds[i][j] for i in Ds for j in Ds[i])
return NN-findMaxLoops(Ds) + ans

"""

