
"""
https://github.com/AnthonyNeu/LintCode/blob/master/Python/Top%20K%20Frequent%20Words.py

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

"""
import collections
import heapq

class Solution:
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]


class Solution2:
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


# O(nlogk) time and O(n) extra space
class Solution3:

    def topKFrequentWords(self, words, k):
        # Write your code here
        import heapq
        from collections import defaultdict
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        heap = []
        for key, value in dic.items():
            heapq.heappush(heap, (-value, key))
        result = []
        while heap and k > 0:
            word = heapq.heappop(heap)
            result.append(word[1])
            k -= 1
        return result



