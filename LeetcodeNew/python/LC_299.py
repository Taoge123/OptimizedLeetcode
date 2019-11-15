"""
You are playing the following Bulls and Cows game with your friend:
You write down a number and ask your friend to guess what the number is.
Each time your friend makes a guess, you provide a hint that indicates how many digits
in said guess match your secret number exactly in both digit and position
(called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows").
Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

"""

import collections

# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:

#         s = collections.defaultdict(int)
#         g = collections.defaultdict(int)

#         A, B = 0, 0

#         for i in range(len(guess)):
#             if secret[i] == guess[i]:
#                 A += 1
#             else:
#                 s[secret[i]] += 1
#                 g[guess[i]] += 1

#         for item in g:
#             B += min(g[item], s[item])

#         return '%dA%dB'% (A, B)



# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         s = collections.Counter(secret)
#         g = collections.Counter(guess)
#         A = sum(i == j for i, j in zip(secret, guess))
#         B = sum((s & g).values()) - A
#         return '%dA%dB'% (A, B)


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        sDict = collections.defaultdict(int)

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                sDict[s] += 1

        for i, g in enumerate(guess):
            if secret[i] != guess[i] and sDict[g]:
                cows += 1
                sDict[g] -= 1

        return "%dA%dB" %(bulls, cows)















