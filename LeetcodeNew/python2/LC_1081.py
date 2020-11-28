"""
42 Trapping Rain Water
84 Largest Rectangle in Histogram
496 Next Greater Element I
503 Next Greater Element II
856 Score of Parentheses
901 Online Stock Span
907 Sum of Subarray Minimums
1130 Minimum Cost Tree From Leaf Values


"""
"""
思路： 找出所有单词， 但是需要是 字典序 最小的 subsequence
一次遍历， 维护一个stack， 存一个降序排列的堆，堆低为最小值，堆顶位最大值
- 如果是之前出现过的字符，跳过
- 如果之前没出现的字符，遇到之前字符 字典序 小于之前最大值， 并且之前最大值在之后还会出现，那么就pop掉，
  知道孩子前stack为空或者没有比当前小
"""
"""
Explanation:
Find the index of last occurrence for each character.
Use a stack to keep the characters for result.
Loop on each character in the input string S,
if the current character is smaller than the last character in the stack,
and the last character exists in the following stream,
we can pop the last character to get a smaller result.


Time Complexity:
Time O(N)
Space O(26)
"""


class Solution:
    def smallestSubsequence(self, text: str) -> str:

        last = {char: i for i, char in enumerate(text)}
        stack = []

        for i, char in enumerate(text):
            if char in stack:
                continue

            #maintain monotonous increasing stack, if new char < stack[-1], and we still have new index > i in last,
            # then we pop it out and expect it com back later
            while stack and char < stack[-1] and i < last[stack[-1]]:
                stack.pop()

            stack.append(char)

        return "".join(stack)



text = "cdadabcc"
a = Solution()
print(a.smallestSubsequence(text))






