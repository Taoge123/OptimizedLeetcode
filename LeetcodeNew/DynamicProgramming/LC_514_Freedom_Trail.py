
"""
https://leetcode.com/problems/reverse-pairs/discuss/97268/general-principles-behind-problems-similar-to-reverse-pairs
http://www.cnblogs.com/grandyang/p/6675879.html

https://leetcode.com/problems/freedom-trail/discuss/209125/Memoized-recursive-solution-in-Python-(long-explanation)

Can be simplified to dp[i] = min(dp[j]+ min(abs(i - j), n - abs(i - j)) for j in indexes[pre]) + 1


In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring",
and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled.
You need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction.
You need to spell all the characters in the string key one by one by rotating the ring clockwise
or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step.
The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction,
where this character must equal to the character key[i].
If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step.
After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.
Example:

Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.
Note:

Length of both ring and key will be in range 1 to 100.
There are only lowercase letters in both strings and might be some duplcate characters in both strings.
It's guaranteed that string key could always be spelled by rotating the string ring.
"""
"""
This is the only way to write the dp: dp[i] = min(dp[j]+ min(abs(i - j), n - abs(i - j)) for j in indexes[pre]) + 1
dp[i] = min(dp[i], ....) is wrong. Because at any given point dp[i] stores the minimum path (from key[0] to current char).
i is the index of the current character, j is the index of the previous character. 
min(abs(i - j), n - abs(i - j)) gives us the minimum distance between the two indexes and updates the current minimum path.
"""
"""
- Store every index of every character in ring in indexes hashtable
- Initialize steps for every index in ring in DP
- For first character of key, update every DP[i] as distance btw zero index plus 1 step for press
- For every next character in key, update every DP[i] as min distance btw pre indexes plus 1 step for press
- Return min DP for last character of key
"""
"""
After some observation, we can see that this question falls under Category 1, Sequential Recurrence Relation from @fun4LeetCode's post.
https://discuss.leetcode.com/topic/79227/general-principles-behind-problems-similar-to-reverse-pairs

The formula is T(i) = T(i-1) + C, which means to calculate the minimum steps for i-th char, we need to calculate the state for (i-1)-th char

And C is: the minimum steps required to move from last_char to char_i. And it is determined by the index of key[i-1] and index of key[i]

Hence, we need to not only record what is the current char i, but also another dimension j to record the end position.

Hence, we have DP[i][j] that,

i denotes the i-th char in key,
denotes the the ending position of char[i],
DP[i][j] saves the minimum steps to reach this state
DP[i][j] = min(DP[i][j], DP[i-1][start] + min(STEPS_LEFT, STEPS_RIGHT) + 1), 
where STEPS_LEFT and STEPS_RIGHT are the minimum steps clockwise/counter-clockwise from index start to index j
"""
"""
这个DP的做法是从0开始遍历直至key结束，我还看到一种更加简单的做法，

做法2：dp[i][j]表示转动从i位置开始的key串所需要的最少步数(这里不包括spell的步数，因为spell可以在最后统一加上)，
此时表盘的12点位置是ring中的第j个字符。不得不佩服这样的设计的确很巧妙，我们可以从key的末尾往前推，
这样dp[0][0]就是我们所需要的结果，因为此时是从key的开头开始转动，而且表盘此时的12点位置也是ring的第一个字符。
现在我们来看如何找出递推公式，对于dp[i][j]，我们知道此时要将key[i]转动到12点的位置，而此时表盘的12点位置是ring[j]，
我们有两种旋转的方式，顺时针和逆时针，我们的目标肯定是要求最小的转动步数，而顺时针和逆时针的转动次数之和刚好为ring的长度n，
这样我们求出来一个方向的次数，就可以迅速得到反方向的转动次数。为了将此时表盘上12点位置上的ring[j]转动到key[i]，
我们要将表盘转动一整圈，当转到key[i]的位置时，我们计算出转动步数diff，然后计算出反向转动步数，并取二者较小值为整个转动步数step，
此时我们更新dp[i][j]，更新对比值为step + dp[i+1][k]，这个也不难理解，因为key的前一个字符key[i+1]的转动情况suppose已经计算好了，
那么dp[i+1][k]就是当时表盘12点位置上ring[k]的情况的最短步数，step就是从ring[k]转到ring[j]的步数，
也就是key[i]转到ring[j]的步数，用语言来描述就是，
从key的i位置开始转动并且此时表盘12点位置为ring[j]的最小步数(dp[i][j])
就等价于将ring[k]转动到12点位置的步数(step)加上从key的i+1位置开始转动并且ring[k]已经在表盘12点位置上的最小步数(dp[i+1][k])之和。
"""

import collections

class Solution1:
    def findRotateSteps(self, ring, key):
        indexes, n, dp, pre = collections.defaultdict(list), len(ring), [0] * len(ring), key[0]
        for i, c in enumerate(ring):
            indexes[c].append(i)
        for i in indexes[key[0]]:
            dp[i] = min(i, n - i) + 1
        for c in key[1:]:
            for i in indexes[c]:
                dp[i] = min(dp[j] + min(i - j, j + n - i) if i >= j else dp[j] + min(j - i, i + n - j) for j in indexes[pre]) + 1
            pre = c
        return min(dp[i] for i in indexes[key[-1]])


class Solution2:
    def findRotateSteps(self, ring, key):
        ind, n, dp, pre = collections.defaultdict(list), len(ring), [0] * len(ring), key[0]
        for i, c in enumerate(ring): ind[c].append(i)
        for i in ind[key[0]]: dp[i] = min(i, n - i) + 1
        for c in key[1:]:
            for i in ind[c]: dp[i] = min(dp[j] + min(i - j, j + n - i) if i >= j else dp[j] + min(j - i, i + n - j) for j in ind[pre]) + 1
            pre = c
        return min(dp[i] for i in ind[key[-1]])



class SolutionLee:
    def findRotateSteps(self, ring, key):
        # the distance between two points (i, j) on the ring
        def dist(i, j):
            return min(abs(i - j), len(ring) - abs(i - j))

        # build the position list for each character in ring
        pos = {}
        for i, c in enumerate(ring):
            if c in pos:
                pos[c].append(i)
            else:
                pos[c] = [i]
        # the current possible state: {position of the ring: the cost}
        state = {0: 0}
        for c in key:
            next_state = {}
            for j in pos[c]:  # every possible target position
                next_state[j] = float('inf')
                for i in state:  # every possible start position
                    next_state[j] = min(next_state[j], dist(i, j) + state[i])
            state = next_state
        return min(state.values()) + len(key)


"""
题目大意：
给定一个拨盘，拨盘上的字符为ring（顺时针方向排列），以及一个关键词key。

拨盘的顶点初始对准ring的第一个字符，拨盘可以顺时针拨动，也可以逆时针拨动。

每拨动一个字符记1步，按一下按钮也记1步。

求利用拨盘得到关键词所需的最小步数。

注意：

ring和key的长度不超过100。
字符串中只包含小写字母。
输入确保可以利用ring得到key。

解题思路：
动态规划（Dynamic Programming）

利用字典dp记录当拨盘位于某位置时，所需的最少步数。

状态转移方程：

dp[k][i] = min(dp[k][i], dp[k - 1][j] + min(abs(i - j), len(ring) - abs(i - j)))

其中k表示当前字符在key中的下标，i表示当前字符在ring中的下标，j表示上一个字符在ring中的下标。

上式可以利用滚动数组化简为一维，节省空间开销。
"""
class Solution3:
    def findRotateSteps(self, ring, key):

        rlist = collections.defaultdict(list)
        for i, r in enumerate(ring):
            rlist[r].append(i)
        rsize = len(ring)
        dp0 = {0 : 0}
        for c in key:
            dp = {}
            for i in rlist[c]:
                dp[i] = 0x7FFFFFFF
                for j in dp0:
                    dp[i] = min(dp[i], dp0[j] + min(abs(i - j), rsize - abs(i - j)))
            dp0 = dp
        return min(dp.values()) + len(key)


"""
大神用的是DP做的。
DP[i][j]：j 表示 ring中位于12点位置的索引 。DP[i][j] 表示拼写 key中从 i-th 字符开始的子字符串，
当 ring中的 j-th 位于12点位置时，需要的最小步骤(只旋转，不含按按钮)。其中 diff 和 n - diff 表示顺时针or逆时针。
DP[i][j] = Math.min(DP[i][j], step + DP[i + 1][k])    
：dp[i][j] =把第 k-th 字符转到12点位置的最小步骤 + 当 k-th 位于12点位置时 拼写出从 i-th + 1 开始的子字符串的最小步骤 (dp[i+1][k]).

state:
12:00 points to jth letter in ring, how many rotation steps required to spell letters starting from ith character
initialization:
dp[m+1][0~n] = 0 since zero steps required to spell empty string regardless of starting position
function:
Previous result + Min(going clockwise, going anticlockwise);
clockwise : this rotation start at j, end at p
anticlockwise : this rotation start at j, end at q
dp[i][j] = Math.min(dp[i + 1][p] + (j + n - p) % n, dp[i + 1][q] + (q + n - j) % n);
result:
dp[0][0] which is the original pattern, plus m steps to spell the word

public class Solution {
    public int findRotateSteps(String ring, String key) {
        int n = ring.length();
        int m = key.length();
        int[][] dp = new int[m + 1][n];
        
        for (int i = m - 1; i >= 0; i--) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = 0; k < n; k++) {
                    if (ring.charAt(k) == key.charAt(i)) {
                        int diff = Math.abs(j - k);
                        int step = Math.min(diff, n - diff);
                        dp[i][j] = Math.min(dp[i][j], step + dp[i + 1][k]);
                    }
                }
            }
        }
        
        return dp[0][0] + m;
    }
}

"""




