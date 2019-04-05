
"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.

"""

"""
Idea:

- Build a word/freq mapping
- Since the # of freq must less or equal than len(words), then we could adopt counting sort.
- Using trie to iterate the anwsers
"""

import collections

class TreeNode(object):
    def __init__(self):
        self.word = None
        self.children = [None] * 26


class Solution:
    def __init__(self):
        self.results = []

    def build_tries(self, word_list):
        root = TreeNode()
        for word in word_list:
            ptr = root
            for ch in word[:]:
                idx = ord(ch) - ord('a')
                if not ptr.children[idx]:
                    ptr.children[idx] = TreeNode()
                ptr = ptr.children[idx]
            ptr.word = word
        return root

    def get_words(self, node):
        if node.word and self.k:
            self.results.append(node.word)
            self.k -= 1
        for nd in node.children:
            if nd:
                self.get_words(nd)

    def topKFrequent(self, words, k):

        words_counting = collections.Counter(words)
        freq_mapping = []
        self.k = k
        self.restuls = []
        for i in range(len(words)):
            freq_mapping.append([])
        for word, freq in words_counting.items():
            freq_mapping[freq].append(word)
        for word_list in freq_mapping[::-1]:
            trie = self.build_tries(word_list)
            for i in trie.children:
                if i and self.k:
                    self.get_words(i)
        return self.results






