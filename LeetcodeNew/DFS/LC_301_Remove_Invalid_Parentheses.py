"""
https://blog.csdn.net/xyqzki/article/details/50404214

For a better view see here

Key Points:

Generate unique answer once and only once, do not rely on Set.
Do not need preprocess.
Runtime 3 ms.
Explanation:
We all know how to check a string of parentheses is valid using a stack.
Or even simpler use a counter.
The counter will increase when it is ‘(‘ and decrease when it is ‘)’.
Whenever the counter is negative, we have more ‘)’ than ‘(‘ in the prefix.

To make the prefix valid, we need to remove a ‘)’.
The problem is: which one? The answer is any one in the prefix.
However, if we remove any one, we will generate duplicate results, f
or example: s = ()), we can remove s[1] or s[2] but the result is the same ().
Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

After the removal, the prefix is then valid. We then call the function recursively
to solve the rest of the string. However,
we need to keep another information: the last removal position.
If we do not have this position, we will generate duplicate by removing two ‘)’
in two steps only with a different order.
For this, we keep tracking the last removal position and only remove ‘)’ after that.

Now one may ask. What about ‘(‘? What if s = ‘(()(()’ in which we need remove ‘(‘?
The answer is: do the same from right to left.
However a cleverer idea is: reverse the string and reuse the code!
Here is the final implement in Java.
"""

"""
The idea is straightforward, with the input string s, 
we generate all possible states by removing one ( or ), 
check if they are valid, if found valid ones on the current level, 
put them to the final result list and we are done, otherwise, 
add them to a queue and carry on to the next level.

The good thing of using BFS is that we can guarantee the number of parentheses 
that need to be removed is minimal, also no recursion call is needed in BFS.

Thanks to @peisi, we don't need stack to check valid parentheses.

Time complexity:

In BFS we handle the states level by level, in the worst case, 
we need to handle all the levels, we can analyze the time complexity level by level and 
add them up to get the final complexity.

On the first level, there's only one string which is the input string s, 
let's say the length of it is n, to check whether it's valid, we need O(n) time. 
On the second level, 
we remove one ( or ) from the first level, so there are C(n, n-1) new strings, 
each of them has n-1 characters, and for each string, 
we need to check whether it's valid or not, 
thus the total time complexity on this level is (n-1) x C(n, n-1). 
Come to the third level, total time complexity is (n-2) x C(n, n-2), 
so on and so forth...

"""

"""
Here I share my DFS or backtracking solution. It's 10X faster than optimized BFS.

Limit max removal rmL and rmR for backtracking boundary. 
Otherwise it will exhaust all possible valid substrings, not shortest ones.
Scan from left to right, avoiding invalid strs (on the fly) by checking num of open parens.
If it's '(', either use it, or remove it.
If it's '(', either use it, or remove it.
Otherwise just append it.
Lastly set StringBuilder to the last decision point.
In each step, make sure:

i does not exceed s.length().
Max removal rmL rmR and num of open parens are non negative.
De-duplicate by adding to a HashSet.
Compared to 106 ms BFS (Queue & Set), it's faster and easier. Hope it helps! Thanks.
"""

"""
Breadth First Search

is_valid - Tests if the brackets are balanced or not. Keep a counter. 
Increment it when you have "(" and decrement it when you see ")". 
If counter is ever negative, then return False
Keep a queue and hash-set. Now add s to queue.
Now run a standard BFS.
Dequeue one by one at a level and test if it is valid.
If yes, add to result. Otherwise remove each element and add to queue.
Why do we use a hash-set? Assume we have "())" 
-> you can remove 1st or 2nd and it will yield (), ().
This can be duplication and cause issues later
Complexity will be n* (2^n)
https://discuss.leetcode.com/topic/28827/share-my-java-bfs-solution"""


class Solution11:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s: return ['']
        q, ans, vis = [s], [], set([s])
        found = False
        while q:
            cur = q.pop(0)
            if self.isValidParentheses(cur):
                found = True
                ans.append(cur)
            elif not found:
                for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        t = cur[:i] + cur[i + 1:]
                        if t not in vis:
                            q.append(t)
                            vis.add(t)
        return ans

    def isValidParentheses(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0: return False
                cnt -= 1
        return cnt == 0

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # this checks if a string is invalid
        def isvalid(s):
            s = ''.join(list(filter('()'.count, s)))  # eliminate all non-brackets
            while '()' in s:
                s = s.replace('()', '')
            return not s

        store = {s}
        while True:
            valid = filter(isvalid, store)
            if valid:
                return valid
            store = {s[:i] + s[i + 1:] for s in store for i in range(len(s))}  # add all possible brackets into store



class Solution22:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s: return ['']
        left_remove = right_remove = 0
        for c in s:
            if c == '(':
                left_remove += 1
            elif c == ')':
                if left_remove:
                    left_remove -= 1
                else:
                    right_remove += 1

        ans = set()
        self.dfs(0, left_remove, right_remove, 0, '', s, ans)
        return list(ans)

    def dfs(self, index, left_remove, right_remove, left_pare, cur, s, ans):
        if left_remove < 0 or right_remove < 0 or left_pare < 0: return
        if index == len(s):
            if left_remove == right_remove == left_pare == 0:
                ans.add(cur)
            return

        if s[index] == '(':
            self.dfs(index + 1, left_remove - 1, right_remove, left_pare, cur, s, ans)
            self.dfs(index + 1, left_remove, right_remove, left_pare + 1, cur + s[index], s, ans)
        elif s[index] == ')':
            self.dfs(index + 1, left_remove, right_remove - 1, left_pare, cur, s, ans)
            self.dfs(index + 1, left_remove, right_remove, left_pare - 1, cur + s[index], s, ans)
        else:
            self.dfs(index + 1, left_remove, right_remove, left_pare, cur + s[index], s, ans)

"""
As we need to generate all possible output 
we will backtrack among all states by removing one opening 
or closing bracket and check if they are valid if invalid 
then add the removed bracket back and go for next state. 
We will use BFS for moving through states,
use of BFS will assure removal of minimal number of brackets 
because we traverse into states level by level 
and each level corresponds to one extra bracket removal. 
Other than this BFS involve no recursion so overhead of passing parameters is also saved.
Below code has a method isValidString to check validity of string, 
it counts open and closed parenthesis at each index ignoring non-parenthesis character. 
If at any instant count of close parenthesis 
becomes more than open then we return false else we keep update the count variable.
"""

"""
Analysis:
In this post, I will firstly present the very basic yet workable solutions using BFS, 
which is implemented in C++.

Then I will explain the DFS solution which is much faster but needs a little more thinking.
 It is implemented in python.

BFS
First of all, notice that the problem requires all possible results, 
thus a search algorithm (BFS, or DFS) often would be a good option.

Considering the BFS solution, 
in this problem we will expand a "tree" with all its child nodes from one level to the other, 
until we find the leaf nodes we want. So given a string s, the mimimum number of deletion is 0, 
which is the string itself, also it is the root node of our tree. If it is a valid string, we're done.

Then we expand the tree by delete only 1 parentheses, 
each child node is one string where 1 parentheses is deleted from the root. 
Therefore, nodes in this level of tree, represents all possible strings where only 1 parentheses is removed.

We could check each new string and see if it is a valid one. 
If in current level there is at lease one valid string, 
the search is terminated after this level is done. 
Since the minimum of deletion is current level depth, 
while the possible valid string are all in this level.

For the implementation, we should have:

A function to check if the string is valid or not.
A queue for the BFS, which stores the nodes in the same level.
Here I use a "map" which we will eliminate the duplicate strings, 
so that the number of "check" could be reduced.
Please check the C++ code below for more details.
DFS
Some will notice that in the BFS solution above, the bottleneck is the number of calls for "check". 
Each time we have to check all the nodes in current level and then go to next level. 
Alternatively, we could try using DFS.

To reduce the number of "check" being called, 
we could store the state (true or false) of nodes in each search path. 
So in next search if we go to the same node, we already have the states, 
which we don't have to check again.

Also, we could firstly compute the number of '(' and ')' to be removed by counting the parentheses in original string. 
Notice that after the removal, we still have to check the result string again."""


class Solution:
    def check(self, s):
        c = 0
        for ch in s:
            if ch == '(':
                c += 1
            if ch == ')':
                c -= 1
                if c < 0:
                    return False
        return c == 0

    def dfs(self, s, d_l, d_r, res, hist):
        if d_l == 0 and d_r == 0:
            if not s in res and self.check(s):
                res[s] = True
        elif s == "":
            return
        else:
            for i in range(len(s)):
                if not s[0:i] + s[i + 1:] in hist:
                    hist[s[0:i] + s[i + 1:]] = True

                    if s[i] == '(' and d_l > 0:
                        self.dfs(s[0:i] + s[i + 1:], d_l - 1, d_r, res, hist)

                    if s[i] == ')' and d_r > 0:
                        self.dfs(s[0:i] + s[i + 1:], d_l, d_r - 1, res, hist)

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        res = {}
        hist = {}
        d_r = 0  # number of '(' to be deleted
        d_l = 0  # number of ')' to be deleted
        for ch in s:
            if ch == '(':
                d_l += 1
            if ch == ')':
                if d_l > 0:
                    d_l -= 1
                else:
                    d_r += 1

        self.dfs(s, d_l, d_r, res, hist)

        return res.keys()
















