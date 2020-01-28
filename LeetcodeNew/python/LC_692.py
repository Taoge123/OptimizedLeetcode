"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

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
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

"""

import collections
import heapq


class Solution:
    def topKFrequent(self, words, k):
        count = collections.Counter(words)

        res = sorted(count, key=lambda x: (-count[x], x))

        return res[:k]


class Solution2:
    def topKFrequent(self, words, k: int):

        count = collections.Counter(words)

        temp = []
        for key, val in count.items():
            heapq.heappush(temp, (-val, key))

        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(temp)[1])
        # return res
        return temp.nsmallest(n=k)


class Solution3:
    def topKFrequent(self, words, k):
        count = collections.Counter(words)

        temp = []
        for key, val in count.items():
            heapq.heappush(temp, (-val, key))

        return [i[1] for i in heapq.nsmallest(k, temp)]


# words = ["i", "love", "leetcode", "i", "love", "coding"]
# k = 2

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4

a = Solution2()
print(a.topKFrequent(words, k))



