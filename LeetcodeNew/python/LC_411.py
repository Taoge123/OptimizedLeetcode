"""
A string such as "word" contains the following abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.

Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.

Note:
In the case of multiple answers as shown in the second example below, you may return any one of them.
Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.
Examples:
"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

"apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
"""

"""
If the target is apple and the dictionary contains apply, then the abbreviation must include the e as the letter e,
not in a number. It's the only letter distinguishing these two words.
Similarly, if the dictionary contains tuple, then the abbreviation must include the a or the first p as a letter.

For each dictionary word (of correct size), I create a diff-number whose bits tell me which of the word's letters differ from the target.
Then I go through the 2m possible abbreviations, represented as number from 0 to 2m-1,
the bits representing which letters of target are in the abbreviation.
An abbreviation is ok if it doesn't match any dictionary word. To check whether an abbreviation doesn't match a dictionary word,
I simply check whether the abbreviation number and the dictionary word's diff-number have a common 1-bit.
Which means that the abbreviation contains a letter where the dictionary word differs from the target.

Then from the ok abbreviations I find one that maximizes how much length it saves me.
Two consecutive 0-bits in the abbreviation number mean that the two corresponding letters will be encoded as the number 2.
It saves length 1. Three consecutive 0-bits save length 2, and so on. To compute the saved length,
I just count how many pairs of adjacent bits are zero.

Now that I have the number representing an optimal abbreviation, I just need to turn it into the actual abbreviation.
First I turn it into a string where each 1-bit is turned into the corresponding letter of the target and each 0-bit is turned into #.
Then I replace streaks of # into numbers.

"""


class Solution:
    def minAbbreviation(self, target: str, dictionary) -> str:

        def abbr(target, num):
            word, count = '', 0
            for w in target:
                if num & 1 == 1:
                    if count:
                        word += str(count)
                        count = 0
                    word += w
                else:
                    count += 1

                num >>= 1
            if count:
                word += str(count)
            return word

        m = len(target)

        # Figure out the different bits for a same length word in the dictionary
        diffs = []
        for word in dictionary:
            if len(word) != m:
                continue

            # The encoding is opposite
            bits = 0
            for i, char in enumerate(word):
                if char != target[i]:
                    bits += 2 ** i
            diffs += bits,

        # No word in dictionary has same length, return the shortest
        if not diffs:
            return str(m)

        abbrs = []
        for i in range(2 ** m):
            # This abbreviation at least has one word different to every words in the dictionary
            if all(d & i for d in diffs):
                abbrs += abbr(target, i),

        return min(abbrs, key=lambda x: len(x))



