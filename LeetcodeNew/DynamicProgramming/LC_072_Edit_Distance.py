
"""
https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
"""
It turns out that one could compute D[i][j], knowing D[i - 1][j], D[i][j - 1] and D[i - 1][j - 1].

There is just one more character to add into one or both strings and the formula is quite obvious.

If the last character is the same, i.e. word1[i] = word2[j] then

D[i][j] = 1 + \min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1] - 1) D[i][j]=1+min(D[i−1][j],D[i][j−1],D[i−1][j−1]−1)

and if not, i.e. word1[i] != word2[j] we have to take into account the replacement of the last character during the conversion.

D[i][j] = 1 + \min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1]) D[i][j]=1+min(D[i−1][j],D[i][j−1],D[i−1][j−1])

So each step of the computation would be done based on the previous computation, as follows:
"""


class Solution1:
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # if one of the strings is empty
        if n * m == 0:
            return n + m

        # array to store the convertion history
        d = [[0] * (m + 1) for _ in range(n + 1)]

        # init boundaries
        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j

        # DP compute
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = d[i - 1][j] + 1
                down = d[i][j - 1] + 1
                left_down = d[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                d[i][j] = min(left, down, left_down)

        return d[n][m]


"""
For those having difficulty cracking dynamic programming solutions, 
I find it easiest to solve by first starting with a naive, but working recursive implementation. 
It's essential to do so, because dynamic programming is basically recursion with caching. 
With this workflow, deciphering dynamic programming problems becomes just a little more manageable for us normal people. :)

Thought process:
Given two strings, we're tasked with finding the minimum number of transformations we need to make to arrive with equivalent strings. 
From the get-go, there doesn't seem to be any way around trying all possibilities, 
and in this, possibilities refers to inserting, deleting, or replacing a character. 
Recursion is usually a good choice for trying all possilbilities.

Whenever we write recursive functions, we'll need some way to terminate, 
or else we'll end up overflowing the stack via infinite recursion. 
With strings, the natural state to keep track of is the index.
We'll need two indexes, one for word1 and one for word2. 
Now we just need to handle our base cases, and recursive cases.
What happens when we're done with either word? 
Some thought will tell you that the minimum number of transformations is simply to insert the rest of the other word. 
This is our base case. What about when we're not done with either string? 
We'll either match the currently indexed characters in both strings, or mismatch. 
In the first case, we don't incur any penalty, 
and we can continue to compare the rest of the strings by recursing on the rest of both strings. 
In the case of a mismatch, we either insert, delete, or replace. To recap:

1. base case: word1 = "" or word2 = "" => return length of other string
2. recursive case: word1[0] == word2[0] => recurse on word1[1:] and word2[1:]
3. recursive case: word1[0] != word2[0] => recurse by inserting, deleting, or replacing"""

class Solution2:
    def minDistance(self, word1, word2):
        """Naive recursive solution"""
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)


"""
With a solution in hand, we're ecstatic and we go to submit our code. 
All is well until we see the dreaded red text... TIME LIMIT EXCEEDED. What did we do wrong? 
Let's look at a simple example, and for sake of brevity I'll annotate the minDistance function as md.

word1 = "horse"
word2 = "hello"

The tree of recursive calls, 3 levels deep, looks like the following. 
I've highlighted recursive calls with multiple invocations. So now we see that we're repeating work. 
I'm not going to try and analyze the runtime of this solution, but it's exponential.

md("horse", "hello")
	md("orse", "ello")
		md("orse", "llo")
			md("orse", "lo")
			md("rse", "llo") <- 
			md("rse", "lo")
		md("rse", "ello")
			md("rse", "llo") <-
			md("se", "ello")
			md("se", "llo") <<-
		md("rse", "llo")
			md("rse", "llo") <-
			md("se", "llo") <<-
			md("se", "lo")
			

The way we fix this is by caching. We save intermediate computations in a dictionary and if we recur on the same subproblem, 
instead of doing the same work again, we return the saved value. Here is the memoized solution, 
where we build from bigger subproblems to smaller subproblems (top-down).

"""
class Solution3:
    def minDistance(self, word1, word2, i, j, memo):
        """Memoized solution"""
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.minDistance2(word1, word2, i + 1, j + 1, memo)
            else:
                insert = 1 + self.minDistance2(word1, word2, i, j + 1, memo)
                delete = 1 + self.minDistance2(word1, word2, i + 1, j, memo)
                replace = 1 + self.minDistance2(word1, word2, i + 1, j + 1, memo)
                ans = min(insert, delete, replace)
            memo[(i, j)] = ans
        return memo[(i, j)]


"""
Of course, an interative implementation is usually better than its recursive counterpart 
because we don't risk blowing up our stack in case the number of recursive calls is very deep. 
We can also use a 2D array to do essentially the same thing as the dictionary of cached values. 
When we do this, we build up solutions from smaller subproblems to bigger subproblems (bottom-up). 
In this case, since we are no longer "recurring" in the traditional sense, 
we initialize our 2D table with base constraints. 
The first row and column of the table has known values since if one string is empty, 
we simply add the length of the non-empty string since that is the minimum number of edits necessary to arrive at equivalent strings. 
For both the memoized and dynamic programming solutions, 
the runtime is O(mn) and the space complexity is O(mn) where m and n are the lengths of word1 and word2, respectively.
"""
class Solution4:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]


class SolutionCaikehe:
    # O(m*n) space
    def minDistance1(self, word1, word2):
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):
            dp[i][0] = i
        for j in range(l2):
            dp[0][j] = j
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]))
        return dp[-1][-1]

    # O(n) space with rolling array
    def minDistance(self, word1, word2):
        l1, l2 = len(word1) + 1, len(word2) + 1
        pre = [0 for _ in range(l2)]
        for j in range(l2):
            pre[j] = j
        for i in range(1, l1):
            cur = [i] * l2
            for j in range(1, l2):
                cur[j] = min(cur[j - 1] + 1, pre[j] + 1, pre[j - 1] + (word1[i - 1] != word2[j - 1]))
            pre = cur[:]
        return pre[-1]

    
class Solution5:
    def minDistance(self, word1, word2):

        m = len(word1)
        n = len(word2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        return dp[m][n]   
