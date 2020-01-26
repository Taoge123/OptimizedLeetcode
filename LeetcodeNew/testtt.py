
"""
Bowtie Round 2 Interview
Mini Project (60 min)

You will be building a simple chat bot for Bowtie Premium Laser Co. that can understand services related laser hair removal!

Please read these instructions carefully and treat this like real world scenario, which means the user input could be anything
# including irrelevant content and misspellings.
#
# I recommend you give yourself 15 min to understand the problem and think of a general strategy, then spend 45 min coding.
#
# ===============
#  Example input
# ===============
#
# User message:
#
#     "Hi, can I get laser hair removal on my arms?"
#
# Bot response format:
#
#     "Sure, which service would you like?
#
#     1. Upper Arms
#     2. Full Arms"
#
# ==========================
#     The bot's response
# ==========================
#
# You can refer to the global variable "services" for a list of all services the bot should understand.
# The global variable "tags" defines alternate phrasing for services that a user might ask for.
#
# For example, if the user says "Can I make a laser appointment?", the bot should match the term "laser" with the corresponding tag, and
# offer all the services in the list given by tags["laser"].
#
# If there are multiple tags present, you should intersect all of the services for those tags and list out the matching services separated by numbered newlines.
# For example if the user says "I want laser hair removal for my arms", the bot should respond: "Sure, which service would you like?\n\n1. Upper Arms\n2. Full Arms".
#
# If a single service is matched, the bot should ask the next question in the booking process and say "Sure! Who would you like to see for your <service>?"
#
# ================
#     The Task
# ================
#
# Please implement the function handle_user_message(user_message) and return the bot's response.
#
# You are provided with two helper functions: is_similar(text, text2) and strip_punctuation(text).
#
# There are 4 test cases defined by the global variable "test_inputs". Keep in mind your code should be general and we will test it on additional test cases.
# We've implemented the main function so if you run this script it will evaluate the 4 test cases.
#
# Here are 2 main things that you should account for:
# 1. Tags with multiple words, ie. "I want a hair removal" should match the "hair removal" tag
# 2. Misspellings in the user input, please use the helper function is_similar()
#
# ===================
#     Final Notes
# ===================
#
# - Feel free to create helper functions and use built-in Python modules, but do not use 3rd party libraries.
# - We will discuss your solution in a follow up.
# - Please don't hardcode responses to pass the tests.
#
# """
#
# # ====================== Service list and tags ======================
#
# # list of all possible services
# services = ["Laser Eye Surgery", "Organic Facial", "Chest", "Full Back", "Full Legs", "Upper Arms", "Full Arms"]
#
# # dictionary that maps a tag to a list of services it refers to. Note that hair removal is two words.
# tags = {
#     "laser": ["Laser Eye Surgery", "Chest", "Full Back", "Full Legs", "Upper Arms", "Full Arms"],
#     "hair removal": ["Chest", "Full Back", "Full Legs", "Upper Arms", "Full Arms"],
#     "arms": ["Upper Arms", "Full Arms"],
#     "legs": ["Full Legs"],
#     "facial": ["Organic Facial"]
# }
#
# test_inputs = [
#     # asking for a specific service should add that service to the appointment and move on to asking for staff
#     {
#         "user_message": "Can I laser my upper arms",
#         "response": "Sure! Who would you like to see for your Upper Arms?",
#     },
#
#     # notice the typo in "removal"
#     {
#         "user_message": "Can I get a laser hair remval",
#         "response": "Sure, which service would you like?",
#         "services": ["Chest", "Full Back", "Full Legs", "Upper Arms", "Full Arms"]
#     },
#
#     # now multiple tags are present in the sentence
#     {
#         "user_message": "Hi, can I get laser hair removal on my arms?",
#         "response": "Sure, which service would you like?",
#         "services": ["Upper Arms", "Full Arms"]
#     },
#     {
#         "user_message": "I want to laser my arms",
#         "response": "Sure, which service would you like?",
#         "services": ["Upper Arms", "Full Arms"]
#     },
# ]
#
# # ====================== Helper functions ======================
#
# import string
# from collections import Counter
#
# def is_similar(text, text2):
#     """
#     Naive similarity implementation
#     """
#     if not text or not text2:
#         return 0
#
#     # use the longer string as the base
#     if len(text2) > len(text):
#         text, text2 = text2, text
#
#     d = Counter(text)
#     d2 = Counter(text2)
#
#     sim = 0
#     for ch, count in d.items():
#         count2 = d2.get(ch, 0)
#         sim += min(count, count2)
#     sim /= float(len(text))
#
#     if text[0] != text2[0]:
#         sim -= 0.5
#
#     return sim > 0.8
#
#
# def strip_punctuation(text):
#     """
#     Strip punctuation from text
#     """
#     try:
#         text = text.decode('utf-8')
#     except:
#         pass
#     return text.translate({ord(c): None for c in string.punctuation})
#
#
# # ====================== Handler function  ======================
#
#
# def handle_user_message(user_message):
#     """
#     Your code here
#     """
#     response = ''
#     print('-----')
#     print()
#
#     return response
#
# for test in test_inputs:
#     handle_user_message(test['user_message'])
#
#
#
#
#
#
#
# def findlargestSubGrid(grid, maxSum):
#     if not grid or not maxSum:
#         return 0
#     m = len(grid)
#     n = len(grid[0])
#     if (m != n):
#         return 0
#     dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
#     ret = [0 for i in range(m)]
#     for i in range(m):
#         for j in range(n):
#             dp[i + 1][j + 1] = grid[i][j] +  dp[i + 1][j] + dp[i][j + 1] - dp[i][j]
#
#     length = len(dp)
#     for len in range(m+1):
#         max = float('-inf')
#         for i in range(len, length):
#             for j in range(len, length):
#                 max = max(max, dp[i][j] - dp[i - len][j] - dp[i][j - len] + dp[i - len][j - len])
#         ret[len-1] = max
#
#     for i in range(len(ret)-1, -1, -1):
#         if (ret[i] <= maxSum):
#             return i + 1
#
# grid = [[2,2,2], [3,3,3], [4,4,4]]
# maxSum = 28
#
# print(findlargestSubGrid(grid, maxSum))
#
#

"""
Input: s = "baabb"
Output: 2
Explanation: "baabb" -> "b" -> "". 

s = "baabb"


"baa bb"
 bbaab

ababab
aaabbb
ababbabbbabbab

"""

#
# class Solution:
#     def filterRestaurants(self, restaurants, veganFriendly: int, maxPrice: int, maxDistance: int):
#         if veganFriendly == 1:
#             res = [item for i, item in enumerate(restaurants) if item[2] is veganFriendly and item[3] <= maxPrice and item[4] <= maxDistance]
#         else:
#             res = [item for i, item in enumerate(restaurants) if item[3] <= maxPrice and item[4] <= maxDistance]
#         res = sorted(res, key=lambda x: (x[1], x[2]), reverse=True)
#         return [i[0] for i in res]
#


# restaurants = [[1,4, 1,40,10],
#                [2,8, 0,50,5],
#                [3,8, 1,30,4],
#                [4,10,0,10,3],
#                [5,1, 1,15,1]]
#
# veganFriendly = 1
# maxPrice = 50
# maxDistance = 10
#
# restaurants = [[1,4, 1,40,10],
#                [2,8, 0,50,5],
#                [3,8, 1,30,4],
#                [4,10,0,10,3],
#                [5,1, 1,15,1]]
# veganFriendly = 0
# maxPrice = 50
# maxDistance = 10
#
# a = Solution()
# print(a.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))
#

import collections

class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            if w <= distanceThreshold:
                graph[u].append(v)
                graph[v].append(u)

        mini = [sum(v) for k, v in graph.items() if sum(v) < distanceThreshold]
        res = [k for k, v in graph.items() if len(v) in mini]

        return max(res)





# n = 4
# edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
# distanceThreshold = 4

n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4


a = Solution()
print(a.findTheCity(n, edges, distanceThreshold))






