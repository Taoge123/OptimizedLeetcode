"""

Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place,
we just need 1 step to spell this character.
For the second key character 'd', we need to rotate the ring "goddin
g" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.



Store every index of every character in ring in indexes hashtable
Initialize steps for every index in ring in DP
For first character of key, update every DP[i] as distance btw zero index plus 1 step for press
For every next character in key, update every DP[i] as min distance btw pre indexes plus 1 step for press
Return min DP for last character of key
"""

"""
Some explanation:
This is the only way to write the dp: 
dp[i] = min(dp[j]+ min(abs(i - j), n - abs(i - j)) for j in indexes[pre]) + 1
dp[i] = min(dp[i], ....) is wrong. Because at any given point dp[i] stores the minimum path 
(from key[0] to current char).
i is the index of the current character, j is the index of the previous character. 
min(abs(i - j), n - abs(i - j)) gives us the minimum distance between the two indexes 
and updates the current minimum path.

"""
"""
class Solution {
    public int findRotateSteps(String ring, String key) {
        int n = ring.length();
        int m = key.length();
        
        int[][] dp = new int[m+1][n];
        //Start by solving key[i:m-1] -> smallest instance is key[m-1:m-1]
        for (int i = m-1; i>= 0; i--){
            //Solve the problem for key[i:m-1] and when the ring arrow points at index j.
            for (int j = 0; j < n; j++){
                dp[i][j] = Integer.MAX_VALUE;
                //Try out every type of spin (by 0, 1, 2, 3, and choose the best choice)
                for (int k = 0; k < n; k++){
                    if (ring.charAt(k) == key.charAt(i)){
                        //Using greedy logic that we should just use the min spin 
                        int diff = Math.abs(j-k);
                        //Choose the min of moving clockwise or counterclockwise
                        int step = Math.min(diff, n-diff);
                        //dp[i+1][k] = Solve the subproblem from key[i+1: m-1] and while our pointer points to k now since
                        //we have rotated the dial there.
                        dp[i][j] = Math.min(dp[i][j], step + dp[i+1][k]);
                    }
                }
            }
        }
        
        return dp[0][0] + m; //We will press the dial button m times in total no matter what.
    }
}
"""
"""
First, the distance between two positions (i, j) can be defined as

dist(i, j) = min(|i - j|, n - |i - j|)
Second, we need a dictionary, h, which tells us the characters on the ring 
and its possible positions of the ring (a list of positions).

The ring starts with one possible status: pcl_pre = [[position, cost]] = [[0, 0]]. 
For each next character, ch, on the key, we can have several choices of positions, h[ch]. 
Since we don't know which route will give the minimum total cost later, we need to compute 
and store the minimum cost for each possible next positions, h[ch], from all possible current positions, 
pcl_pre. In the end, we return the minimum total cost for the last character on the key.
"""


import collections
class Solution:
    def findRotateSteps(self, ring, key):
        indexes, n, dp, pre = collections.defaultdict(list), len(ring), [0] * len(ring), key[0]
        # add index as value and each item in ring is the key
        for i, item in enumerate(ring):
            indexes[item].append(i)
        print(indexes)
        # Base case,
        for i in indexes[key[0]]:
            dp[i] = min(i, n - i) + 1
        # For rest of the items in key
        for item, in key[1:]:
            for i in indexes[item]:
                dp[i] = min(dp[j] + min(i - j, j + n - i) if i >= j else dp[j] + min(j - i, i + n - j) for j in indexes[pre]) + 1
            pre = item
        return min(dp[i] for i in indexes[key[-1]])

a = Solution()
print(a.findRotateSteps(ring = "godding", key = "gd"))

"""
Build Character to Index map
For a given wheel position (cur) and target character index (target) find minimal number of steps. 
We try to reach this character by CW or CCW movement and then repeat the function for smaller subproblem.
"""
import collections

class Solution3:
    def findRotateSteps(self, ring, key):
        char_pos, n = collections.defaultdict(list), len(ring)
        for i, ch in enumerate(ring):
            char_pos[ch].append(i)

        @lru_cache(maxsize=None)
        def dfs(cur, target):
            if target == len(key):
                return 0
            return min(1 + min(abs(cur - option), n - abs(cur - option)) + dfs(option, target + 1) for option in
                       char_pos[key[target]])

        return dfs(0, 0)


"""
After some observation, we can see that this question falls under Category 1, Sequential Recurrence Relation from @fun4LeetCode's post.
https://discuss.leetcode.com/topic/79227/general-principles-behind-problems-similar-to-reverse-pairs

The formula is T(i) = T(i-1) + C, which means to calculate the minimum steps for i-th char, we need to calculate the state for (i-1)-th char

And C is: the minimum steps required to move from last_char to char_i. And it is determined by the index of key[i-1] and index of key[i]

Hence, we need to not only record what is the current char i, but also another dimension j to record the end position.

Hence, we have DP[i][j] that,

1. i denotes the i-th char in key,
2. denotes the the ending position of char[i],
3. DP[i][j] saves the minimum steps to reach this state
4. DP[i][j] = min(DP[i][j], DP[i-1][start] + min(STEPS_LEFT, STEPS_RIGHT) + 1), 
   where STEPS_LEFT and STEPS_RIGHT are the minimum steps clockwise/counter-clockwise 
   from index start to index j
"""
from collections import defaultdict


class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        m, n = len(key), len(ring)
        dp = [[float('inf') for j in range(n)] for i in range(m)]

        dic = defaultdict(list)
        for i, char in enumerate(ring):
            dic[char].append(i)

        for i in range(m):
            char = key[i]
            for j in dic[char]:
                if i == 0:
                    dp[i][j] = min(j - 0, n - j) + 1  # First row
                else:
                    last_char = key[i - 1]
                    for start in dic[last_char]:
                        left = j - start if j >= start else j - start + n  # Steps if counter-clockwise
                        right = start - j if start >= j else start - j + n  # Steps if clocewise
                        dp[i][j] = min(dp[i][j], dp[i - 1][start] + min(left, right) + 1)
        return min(dp[m - 1])


"""
First of all, I assume you understand the O(RK^2) dp solution. Which, at each step of the dp, requires going through the ring O(R) times. i.e.
dp[i][j]=min( [ dp[i][k] + minStepFrom_i_to_k for k in range(len(ring)) if ring[k]==key[i-1] ] ) if ring[j]==key[i]
(here I'm using python list comprehension notation)

which means we are going through all the characters to determine the minimum steps.
However, we just need to check the closest ones on the left and right! To see this, 
lets assume we are onto the ith character of the key and we wish to 
calculate the minimum steps required to get to all the characters on the ring same as key[i], 
and we are doing it on the jth character on the ring (such that ring[j]==key[i]). 
Then if we need to check the characters of previous key other than the closest ones, 
there exists a character at position u such that dp[i-1][u] leads to dp[i][j]. 
Suppose u is left to the left closest key[i-1], 
then from u to leftClosest takes at most leftClosest-u steps. However, 
dp[i-1][u]+(j-u)<dp[i-1][leftClosest]+(j-leftClosest), 
which means dp[i-1][leftClosest] - dp[i-1][u] > leftClosest - u. 
This is impossible since we can just take at most leftClosest - u steps to get from u to leftClosest, 
it should be the case that dp[i-1][leftClosest] - dp[i-1][u] <= leftClosest - u, 
therefore dp[i-1][leftClosest] is not optimal! 
(same argument applies to characters right to the rightClosest)

Therefore we just need to find the position of occurences of key[i-1] just left 
and right to the occurrences of key[i] in the ring! 
This is exactly what the subroutine findRange does. 
It takes in the indices of key[i-1] in the ring and the indices of key[i] in the ring, 
and it returns the indices of the left closest and right closest indices. Also to speed up the process, 
I used a dictionary to store the mapping from character to indices of that character 
on the ring to speed up the look-ups. 
The subroutine runs in O(R) time and each time after the left 
and right indices has been found the looping also takes O(R) time. 
The result is an O(R) inner loop and an O(RK) algorithm.

"""

