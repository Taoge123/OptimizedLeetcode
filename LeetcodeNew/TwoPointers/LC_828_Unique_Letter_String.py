
"""
A character is unique in string S if it occurs exactly once in it.

For example, in string S = "LETTER", the only unique characters are "L" and "R".

Let's define UNIQ(S) as the number of unique characters in string S.

For example, UNIQ("LETTER") =  2.

Given a string S with only uppercases, calculate the sum of UNIQ(substring) over all non-empty substrings of S.

If there are two or more equal substrings at different positions in S, we consider them different.

Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.



Example 1:

Input: "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
Example 2:

Input: "ABA"
Output: 8
Explanation: The same as example 1, except uni("ABA") = 1.

"""

"""
分别统计每个字母出现的下标

假设字母letter的下标数组为idx，将-1和len(S)插入idx的头部和尾部

则sum((idx[i] - idx[i - 1]) * (idx[i + 1] - idx[i]))为letter出现的总次数

"""

"""
Approach #2: Split by Character [Accepted]
Intuition

As in Approach #1, we have U(x) = \sum_{c \in \mathcal{A}} U_c(x)U(x)=∑ 
c∈A
​	
 U 
c
​	
 (x), where \mathcal{A} = \{ \text{"A"}, \text{"B"}, \dots \}A={"A","B",…} is the alphabet, 
 and we only need to answer the following question (26 times, one for each character): 
 how many substrings have exactly one \text{"A"}"A"?

Algorithm

Consider how many substrings have a specific \text{"A"}"A". For example, 
let's say S only has three "A"'s, at 'S[10] = S[14] = S[20] = "A"; 
and we want to know the number of substrings that contain S[14]. 
The answer is that there are 4 choices for the left boundary of the substring (11, 12, 13, 14), 
and 6 choices for the right boundary (14, 15, 16, 17, 18, 19). So in total, 
there are 24 substrings that have S[14] as their unique "A".

Continuing our example, if we wanted to count the number of substrings that have S[10], 
this would be 10 * 4 - note that when there is no more "A" characters to the left of S[10], 
we have to count up to the left edge of the string.

We can add up all these possibilities to get our final answer.
"""

"""
Intuition:

Let's think about how a character can be found as a unique character.

Think about string "XAXAXXAX" and focus on making the second "A" a unique character.
We can take "XA(XAXX)AX" and between "()" is our substring.
We can see here, to make the second "A" counted as a uniq character, we need to:

insert "(" somewhere between the first and second A
insert ")" somewhere between the second and third A
For step 1 we have "A(XA" and "AX(A", 2 possibility.
For step 2 we have "A)XXA", "AX)XA" and "AXX)A", 3 possibilities.

So there are in total 2 * 3 = 6 ways to make the second A a unique character in a substring.
In other words, there are only 6 substring, in which this A contribute 1 point as unique string.

Instead of counting all unique characters and struggling with all possible substrings,
we can count for every char in S, how many ways to be found as a unique char.
We count and sum, and it will be out answer.

Explanation:

index[26][2] record last two occurrence index for every upper characters.
Initialise all values in index to -1.
Loop on string S, for every character c, update its last two occurrence index to index[c].
Count when loop. For example, if "A" appears twice at index 3, 6, 9 seperately, we need to count:
For the first "A": (6-3) * (3-(-1))"
For the second "A": (9-6) * (6-3)"
For the third "A": (N-9) * (9-6)"
Complexity:
One pass, time complexity O(N).
Space complexity O(1).
"""
import string
import collections

class Solution1:
    def uniqueLetterString(self, S):
        index = collections.defaultdict(list)
        for i, c in enumerate(S):
            index[c].append(i)

        ans = 0
        for A in index.values():
            A = [-1] + A + [len(S)]
            for i in range(1, len(A) - 1):
                ans += (A[i] - A[i-1]) * (A[i+1] - A[i])
        return ans % (10**9 + 7)

class SolutionLee:
    def uniqueLetterString(self, S):
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(S):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        return res % (10**9 + 7)


class Solution2:
    def uniqueLetterString(self, S):
        s = 0
        g = collections.defaultdict(lambda : [-1])
        for i,j in enumerate(S):
            g[j].append(i)
        for j in g.values():
            j.append(len(S))
            for k in range(1, len(j)-1):
                s += (j[k] - j[k-1]) * (j[k+1]-j[k])
        return s % (10 ** 9 + 7)



"""
肯定不能一个个substring来做，换个角度，求每个字符的有效substring个数
"""

"""
解题思路：在任何子串中，只有出现一次的字符才对最终的结果起作用。假设输入的S为 XXXAXXXXAXXAXXXXX，X表示其他任意字符，
现在我们来计算蓝A对最后的输出贡献了多少，很显然在两个红A之间的子串中，只要是包括蓝A的子串都有蓝A的贡献，
如果第一个红A到蓝A之间的字符数量是L，蓝A到第二个红A之间的字符数量是R，那么蓝A的贡献就是 L + R + L*R + 1 ，
其中L表示蓝A与左边字符组成的子串数量，R为与右边的，L*R为同时与左右结合，1表示不与任何字符结合。
所有只有找出所有字符左右两边相同字符出现的位置，即可计算出最终的答案。
"""

class Solution3:
    def uniqueLetterString(self, s):

        d = {}
        res = 0
        for i, c in enumerate(s):
            if c not in d:
                d[c] = [-1]
            else:
                k, j = d[c][-2:]
                res += (j - k) * (i - j)
            d[c].append(i)

        for c in d:
            k, j = d[c][-2:]
            res += (j - k) * (len(s) - j)

        return res



class Solution4:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        ret = 0
        for i in range(len(S)):
            left = i - 1
            right = i + 1
            while left >= 0 and S[left] != S[i]:
                left -= 1
            while right < len(S) and S[right] != S[i]:
                right += 1
            ret += (right - i) * (i - left)
        return ret % (1000000007)




