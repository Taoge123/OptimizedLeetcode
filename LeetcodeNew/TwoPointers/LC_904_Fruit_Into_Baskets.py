
"""

https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/


In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.

"""

"""
Problem
"Start from any index, we can collect at most two types of fruits. What is the maximum amount"

Translation
Find out the longest length of subarrays with at most 2 different numbers?

Solution of sliding window will be easier to understand.
Here I share another solution wihtout hash map.
Hope it's not damn hard to understand.

Explanation:
Loop all fruit c in tree,
Note that a and b are the last two different types of fruit that we met,
c is the current fruit type,
so it's something like "....aaabbbc..."

Case 1 c == b:
fruit c already in the basket,
and it's same as the last type of fruit
cur += 1
count_b += 1

Case 2 c == a:
fruit c already in the basket,
but it's not same as the last type of fruit
cur += 1
count_b = 1
a = b, b = c

Case 3 c != b && c!= a:
fruit c not in the basket,
cur = count_b + 1
count_b = 1
a = b, b = c

Of course, in each turn we need to update res = max(res, cur)
"""
import collections

class SolutionLee1:
    def totalFruit(self, tree):
        res = cur = count_b = a = b = 0
        for c in tree:
            cur = cur + 1 if c in (a, b) else count_b + 1
            count_b = count_b + 1 if c == b else 1
            if b != c:
                a, b = b, c
            res = max(res, cur)
        return res


"""
Problem
"Start from any index, we can collect at most two types of fruits. What is the maximum amount"

Translation
Find out the longest length of subarrays with at most 2 different numbers?

Complexity:
O(N) time, O(1) space
"""

class SolutionLee2:
    def totalFruit(self, tree):
        count = {}
        i = res = 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
            res = max(res, j - i + 1)
        return res


"""
It basically asks for max 2 types of element picked in the current sliding window. 
And you will pick any element in specified index just once.
"""

class Solution3:
    def totalFruit(self, tree):
        l, nums, res = 0, collections.Counter(), 0
        for r in range(len(tree)):
            nums[tree[r]] += 1
            while len(nums) > 2:
                nums[tree[l]] -= 1
                if not nums[tree[l]]:
                    nums.pop(tree[l])
                l += 1
            res = max(res, r - l + 1)
        return res


class Solution5:
    def totalFruit(self, tree):
        prev, curr, res = [None, 0], [None, 0], 0
        for t in tree:
            if t == curr[0]:
                curr[1] += 1
            else:
                prev, curr = curr, prev
                if t == curr[0]:
                    prev[1] += curr[1]
                else:
                    res = max(res, prev[1] + curr[1])
                curr = [t, 1]
        return max(res, prev[1] + curr[1])


