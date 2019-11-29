import collections, heapq
"""
使用Counter统计每个字符出现的次数，然后使用大根堆，每次弹出出现次数最多的字符，添加到生成结果字符串的末尾。
如果剩余的不同字符个数不够k，那么说明不能满足题目的要求，返回空字符串。另外，每次弹出出现次数最多的字符之后，
不能直接放入堆中，因为直接放入堆中可能下次又被弹出来，所以应该放入一个临时的数组中，在单次操作结束之后再重新插入堆中。

时间复杂度是O(N)，空间复杂度是O(N)。
"""


class Solution:
    def rearrangeString(self, words, k):
        _len = len(words)

        wordCount = collections.Counter(words)
        queue = []
        heapq.heapify(queue)
        for word, count in wordCount.items():
            heapq.heappush(queue, (-count, word))
        res = ""
        while queue:
            loop = min(_len, max(1, k))
            used = []
            for i in range(loop):
                if not queue:
                    return ""
                count, word = heapq.heappop(queue)
                res += word
                if -count > 1:
                    used.append((count + 1, word))
                _len -= 1
            for use in used:
                heapq.heappush(queue, use)
        return res


words = "aa"
k = 0

a = Solution()
print(a.rearrangeString(words, k))





