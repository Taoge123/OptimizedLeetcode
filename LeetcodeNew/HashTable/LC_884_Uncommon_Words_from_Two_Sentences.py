
"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""

"""

Intuition:
No matter how many sentences,
uncommon word = words that appears only once

I recall another similar problem:
819. Most Common Word
So I open my solutions there and copy some codes.

Explanation:

Two steps:
Count words occurrence to a HashMap<string, int> count.
Loop on the hashmap, find words that appears only once.
"""
import collections

class Solution1:
    def uncommonFromSentences(self, A, B):
        c = collections.Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]


class Solution2:
    def uncommonFromSentences(self, A, B):
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        #Alternatively:
        #count = collections.Counter(A.split())
        #count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]


class Solution3:
    def uncommonFromSentences(self, A, B):
        both = A.split(' ') + B.split(' ')      # create a list of words
        return [x for x in both if both.count(x)==1]        # standard list comprehension



