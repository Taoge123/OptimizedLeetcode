# profits = [0.02, -0.08, 0.02, 0.01, -0.03, -0.05, 0.02, 0.03, -0.03, 0.01, 0.03]
# # profits = [0.01, -0.08, -0.01, 0.02, 0.03, 0.10, 0.04, 0.01]
#
# dp = [1] + [0] * len(profits)
#
# for i in range(1, len(profits)):
#     dp[i] = dp[i-1] * (1+profits[i-1])
#
# print(dp)
# print(dp[5]-dp[1])
#
# class Solution:
#     def wordsTyping(self, sentence, rows, cols):
#
#         s = ' '.join(sentence) + ' '
#         start = 0
#         for i in range(rows):
#             start += cols - 1
#             if s[start % len(s)] == ' ':
#                 start += 1
#             elif s[(start + 1) % len(s)] == ' ':
#                 start += 2
#             else:
#                 while start > 0 and s[(start - 1) % len(s)] != ' ':
#                     start -= 1
#         return start // len(s)
#
# rows = 3
# cols = 6
# sentence = ["a", "bcd", "e"]
#
# a = Solution()
# print(a.wordsTyping(sentence, rows, cols))
#







