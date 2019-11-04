
"""
https://leetcode.com/problems/can-i-win/discuss/95319/Python-solution-with-detailed-explanation
http://guoyc.com/post/can_i_win/


In the "100 game," two players take turns adding, to a running total, any integer from 1..10.
The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal,
determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""
"""
After solving several "Game Playing" questions in leetcode, I find them to be pretty similar. 
Most of them can be solved using the top-down DP approach, which "brute-forcely" simulates every possible state of the game.

The key part for the top-down dp strategy is that we need to avoid repeatedly solving sub-problems. 
Instead, we should use some strategy to "remember" the outcome of sub-problems. 
Then when we see them again, we instantly know their result. 
By doing this, we can always reduce time complexity from exponential to polynomial.
(EDIT: Thanks for @billbirdh for pointing out the mistake here. 
For this problem, by applying the memo, we at most compute for every subproblem once, 
and there are O(2^n) subproblems, so the complexity is O(2^n) after memorization. 
(Without memo, time complexity should be like O(n!))

For this question, the key part is: what is the state of the game? Intuitively, 
to uniquely determine the result of any state, we need to know:

The unchosen numbers
The remaining desiredTotal to reach
A second thought reveals that 1) and 2) are actually related because we can always get the 2) 
by deducting the sum of chosen numbers from original desiredTotal.

Then the problem becomes how to describe the state using 1).

In my solution, I use a boolean array to denote which numbers have been chosen, and then a question comes to mind, 
if we want to use a Hashmap to remember the outcome of sub-problems, can we just use Map<boolean[], 
Boolean> ? Obviously we cannot, because the if we use boolean[] as a key, 
the reference to boolean[] won't reveal the actual content in boolean[].

Since in the problem statement, it says maxChoosableInteger will not be larger than 20, 
which means the length of our boolean[] array will be less than 20. 
Then we can use an Integer to represent this boolean[] array. How?

Say the boolean[] is {false, false, true, true, false}, then we can transfer it to an Integer with binary representation as 00110. 
Since Integer is a perfect choice to be the key of HashMap, then we now can "memorize" the sub-problems using Map<Integer, Boolean>.

The rest part of the solution is just simulating the game process using the top-down dp.
"""

class Solution1:
    def canIWin(self, maxChoosableInteger, desiredTotal):

        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)

    def helper(self, nums, desiredTotal):

        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i]):
                self.memo[hash] = True
                return True
        self.memo[hash] = False
        return False


"""
Top Down DFS with Memoization: Time: O(N * 2^N). Space: O(2^N)

- We create an array allowed which has all the integers from 1 to maxChoosableInteger.
- We test if the input is valid or not i.e. sum(allowed) >= desiredTotal.
- How do we define the state of the game? This answer determines how we will do memoization as well. 
  Clearly list of current allowed numbers are needed to define the state. It might also look that so_far is also required to define the state. 
  However, given all allowed values and the current set of allowed values, 
  so_far is really the difference of the sum of the two. Therefore only allowed values uniquely determine the state.
- How many allowed values sets are possible? The length of the allowed value set can range 1 to maxChoosableInteger(N). 
  So the answer is (N,1) + (N,2) + ..(N,N) where (N,K) means choose K from N. This is equal to 2^N.
- Now at my turn, if the max(allowed) + so_far >= target, then I will win. Otherwise, 
  I choose from the allowed values one by one and recursively call for the other player. 
  If with any choice the opponent fails for sure, then also I can win for sure from this state.
- What is the time complexity? For a brute force solution, the game tree has 10 choices at first level, 
  each of these choices has 9 choices at second level, and so on. So the complexity is N!. 
  But with memoization, we only compute 2^N sub-problems, and in each problem we do O(N) work. 
  So total time complexity is O(N2^N).

"""


class Solution2:
    def helper(self, allowed, target, so_far, cache):
        if len(allowed) == 0:
            return False
        state = tuple(allowed)
        if state in cache:
            return cache[state]
        else:
            cache[state] = False
            if max(allowed) + so_far >= target:
                cache[state] = True
            else:
                for x in allowed:
                    new_allowed = [y for y in allowed if x != y]
                    if self.helper(new_allowed, target, so_far + x, cache) == False:
                        cache[state] = True
                        break
            return cache[state]

    def canIWin(self, maxChoosableInteger, desiredTotal):

        allowed = [x for x in range(1, maxChoosableInteger + 1)]
        if sum(allowed) < desiredTotal:
            return False
        return self.helper(allowed, desiredTotal, 0, {})


"""
Corner Case:
- sum(pick values) < desired sum: The first player never wins.
- sum(pick values) == desired sum: Whoever takes the last wins. (Irrelevant to who pick which number first)
- max choosable number > desired sum: The first player always wins by picking the max number.
Code Supplemental Explanation:
- Record: Used to rememeber win\loss for current state. (what numbers have been picked, True: Win, False: Lose)
- Bitmap: Record which number has been picked. Also used as an index to access the win loss record. (if in hash table)
- Win if there is a way of picking a number 'n' such that no matter how opponent picks next, the opponent lose.
- Lose if there is no way of picking a number 'n' that satisfies the above situation.
- Win\Loss is for the first player with the game status (bitmap passed in).
"""

class Solution33:
    def canIWin(self, maxChoosableInteger, desiredTotal):

        seen = {}

        def can_win(choices, remainder):
            # if the largest choice exceeds the remainder, then we can win!
            if choices[-1] >= remainder:
                return True

            # if we have seen this exact scenario play out, then we know the outcome
            seen_key = tuple(choices)
            if seen_key in seen:
                return seen[seen_key]

            # we haven't won yet.. it's the next player's turn.
            # importantly, if we win just one permutation then
            # we're still on our way to being able to 'force their hand'
            for index in range(len(choices)):
                if not can_win(choices[:index] + choices[index + 1:], remainder - choices[index]):
                    seen[seen_key] = True
                    return True

            # uh-oh if we got here then next player won all permutations, we can't force their hand
            # actually, they were able to force our hand :(
            seen[seen_key] = False
            return False


        # note: usefully, choices is already sorted
        choices = list(range(1, maxChoosableInteger + 1))

        # let's do some quick checks before we journey through the tree of permutations
        summed_choices = sum(choices)

        # if all the choices added up are less then the total, no-one can win
        if summed_choices < desiredTotal:
            return False

        # if the sum matches desiredTotal exactly, then as
        # long as there is an odd number of choices then first player wins
        if summed_choices == desiredTotal and len(choices) % 2:
            return True

        # slow: time to go through the tree of permutations
        return can_win(choices, desiredTotal)


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        max_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if max_sum < desiredTotal:
            return False
        elif max_sum == desiredTotal:
            return (maxChoosableInteger % 2 == 1)

        if maxChoosableInteger >= desiredTotal:
            return True

        bit_mask = 1 << maxChoosableInteger  # bit 0: unused, bit 1: used
        self.record = {}

        return self.checkWin(maxChoosableInteger, bit_mask, desiredTotal)

    def checkWin(self, max_num, bit_mask, remain_sum):

        if bit_mask in self.record:
            return self.record[bit_mask]

        for i in range(max_num):

            if (1 & (bit_mask >> i)) != 0:
                # skip already-picked number
                continue

            n = i + 1  # n: picked number
            if (n >= remain_sum) or (self.checkWin(max_num, bit_mask | (1 << i), remain_sum - n) is False):
                self.record[bit_mask] = True
                return True

        self.record[bit_mask] = False
        return False

"""
如果数字可以重复使用
现在先实现数字可以重复使用的情况：

令dp[i]表示玩家在当前和为i的情况下是否可以获胜。 choose表示玩家可以使用1~choose之间的数字。 target表示先到达target的玩家获胜。

初始情况：

dp[i]=True if (i+choose)>=target

递推公式：

dp[i]=True if dp[i+j]=False for any i+1<=j<=i+choose
"""
class Solution11:
    def canIWin(self, choose, total):
        dp = [False]*(total+1)
        for i in range(total, -1, -1):
            if i+choose>=total:
                dp[i] = True
                continue
            for j in range(1, choose+1):
                if not dp[i+j]:
                    dp[i] = True
                    break
        return dp[0]

"""
数字不可以重复使用
如果数字不可以重复使用的话，很直观的想法就是dfs进行回溯，新建一个数组保存每个数字的使用情况。
"""
"""
function dp(cur, used):
	for i in [1, choose]:
		# 如果i已经被使用，continue
		if used[i]:
			continue
		# 如果选择i可以超过total，获胜
		if cur+i>=total:
			return true
		# 选i，如果下一步对手在cur+i处不能获胜，则我方获胜
		used[i] = true
		tmp = dp(cur+i, used)
		used[i] = false
		if tmp:
			return true
	return false
"""

"""
题目大意：
在“100游戏”中，两个玩家轮流从整数1-10中取数相加，得到一个累加值。第一个使累加值达到或者超过100的玩家获胜。

我们修改游戏规则，用过的数字不能重复使用，会怎样呢？

例如，两个玩家可以轮流从1..15中无放回的取数字，使得累加值>=100。

给定整数 maxChoosableInteger 和 desiredTotal，判断第一个玩家是否一定能赢，假设两名玩家都采用最优策略。

你可以总是假设 maxChoosableInteger 不大于20，desiredTotal 不大于300。

解题思路：
记忆化搜索 + 位运算

由于maxChoosableInteger不大于20，因此可以通过整数state表示当前已经选择了哪些数字

state的第i位为1时，表示选择了数字i + 1

利用字典dp记录已经搜索过的状态
"""

class Solution4:
    def canIWin(self, maxChoosableInteger, desiredTotal):

        dp = dict()
        def search(state, total):
            for x in range(maxChoosableInteger, 0, -1):
                if not state & (1 << (x - 1)):
                    if total + x >= desiredTotal:
                        dp[state] = True
                        return True
                    break
            for x in range(1, maxChoosableInteger + 1):
                if not state & (1 << (x - 1)):
                    nstate = state | (1 << (x - 1))
                    if nstate not in dp:
                        dp[nstate] = search(nstate, total + x)
                    if not dp[nstate]:
                        dp[state] = True
                        return True
            dp[state] = False
            return False
        if maxChoosableInteger >= desiredTotal: return True
        if (1 + maxChoosableInteger) * maxChoosableInteger < 2 * desiredTotal: return False
        return search(0, 0)


"""
思路：

这道题目既可以用动态规划，也可以用DFS + memorization。感觉DFS + memorization更容易理解一些。
由于题目限定了maxChhoseableInteger <= 20，所以我们可以巧妙地用20个bits来表示截止当前已经用过的数（第i位为1表示i已经被使用过了，
否则表示i尚未被使用过）。我们用两个哈希表来表示哪些数字确定可以赢，哪些数字确定会输。在DFS的过程中，
我们首先在哈希表中查找当前组合是否已经被记录下来了，如果是，则直接返回结果；否则我们就逐个尝试（从1到maxChooseableInteger），
如果发现该数字已经被使用，则直接跳过；否则就从对手是否可能赢来判断我是不是可以保证赢：“我能保证赢的充分必要条件是：
我选取了当前这个数字之后，对方无论如何都不可能赢”。如果我选择任何数字都不可能赢，那么对方就一定可以保证赢了。
具体看下面的代码片段以及详细解释。
"""
"""
这道题给了我们一堆数字，然后两个人，每人每次选一个数字，看数字总数谁先到给定值，有点像之前那道Nim Game，
但是比那题难度大。我刚开始想肯定说用递归啊，结果写完发现TLE了，
后来发现我们必须要优化效率，使用HashMap来记录已经计算过的结果。
我们首先来看如果给定的数字范围大于等于目标值的话，直接返回true。
如果给定的数字总和小于目标值的话，说明谁也没法赢，返回false。
然后我们进入递归函数，首先我们查找当前情况是否在哈希表中存在，有的话直接返回即可。
我们使用一个整型数按位来记录数组中的某个数字是否使用过，我们遍历所有数字，将该数字对应的mask算出来，
如果其和used相与为0的话，说明该数字没有使用过，我们看如果此时的目标值小于等于当前数字，说明已经赢了，
或者我们调用递归函数，如果返回false，说明也是第一个人赢了。为啥呢，因为当前我们已经选过数字了，
此时就该对第二个人调用递归函数，只有他的结果是false，我们才能赢，所以此时我们标记true，返回true。
如果遍历完所有数字，我们标记false，返回false，
"""


class Solution5:
    def canWin(self, maxChoosableInteger, desiredTotal, cur, d):
        if cur in d: return d[cur]
        if desiredTotal <= 0:
            d[cur] = False
            return d[cur]
        for i in range(maxChoosableInteger):
            if (cur >> i) & 1 == 0:
                if not self.canWin(maxChoosableInteger, desiredTotal - (i + 1), cur + (1 << i), d):
                    d[cur] = True
                    return d[cur]
        d[cur] = False
        return d[cur]

    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= 0: return True
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal: return False
        return self.canWin(maxChoosableInteger, desiredTotal, 0, {})


"""
the variable "cur" represents which numbers have been chosen and which are not. For example, 
if maxChoosableInteger = 8, we have all the numbers we can choose from: 1, 2, 3, 4, 5, 6, 7, 8.

The "cur" variable lets us know the state of our number stock. 
Originally, cur = 0, or cur = 0000 0000 (in 8-bit system). This means, all number from 1 to 8 have not been chosen.
At some point, let's say cur = 0000 0001, that means number 1 have been picked by some player. 
Or when cur = 0000 0101, this means number 1 and 3 have been picked.

And so if (cur >> i) & 1 == 0 is checking if number (i+1) has been picked yet or not, 
so we don't pick what has been picked (since the problem said that we pick without replacement, 
which means you cannot reuse a number). You shouldn't do what I did, just use hash set. Looking back at this,
I don't understand why I did this and not use a hash set
"""


class Solution6:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        choosable = tuple(range(1, maxChoosableInteger + 1))
        if sum(choosable) < desiredTotal: return False
        self.cache = {}
        return self.dfs(choosable, desiredTotal)

    def dfs(self, choosable, total):
        if choosable[-1] >= total: return True
        key = choosable
        if key in self.cache: return self.cache[key]
        for i in range(len(choosable)):
            if not self.dfs(choosable[:i] + choosable[i + 1:], total - choosable[i]):
                self.cache[key] = True
                return True
        self.cache[key] = False
        return False



class SolutionHuahua:
  def canIWin(self, M, T):
    def win(M, T, m, state):
      if T <= 0: return False
      if m[state] != 0: return m[state] == 1
      for i in range(M):
        #number i used
        if (state & (1 << i)) > 0: continue
        #The next player can not win, current player wins
        if not win(M, T - i - 1, m, state | (1 << i)):
          m[state] = 1
          return True
      m[state] = -1
      return False

    s = M * (M + 1) / 2
    if s < T: return False
    if T <= 0: return True
    if s == T: return (M % 2) == 1

    m = [0] * (1 << M)
    return win(M, T, m, 0)


class SolutionTony:
    def canIWin(self, num: int, target: int) -> bool:
        if num * (num + 1) // 2 < target:
            return False
        cache = {}

        return self.helper(tuple(range(1, num + 1)), target, cache)

    def helper(self, nums, target, cache):
        if not nums:
            return False
        if nums in cache:
            return cache[nums]
        if nums[-1] >= target:
            return True

        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i + 1:], target - nums[i], cache):
                cache[nums] = True
                return True
        cache[nums] = False

        return False


a = SolutionTony()
print(a.canIWin(10, 11))


