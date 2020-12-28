"""
https://leetcode.com/problems/minimum-time-to-build-blocks/discuss/387035/Python%3A-O(n-log-n)-using-Huffman's-Algorithm-(priority-queue)-with-explanation.
"""

import heapq

class Solution:
    def minBuildTime(self, blocks, split: int) -> int:

        heapq.heapify(blocks)
        while len(blocks) > 1:
            x = heapq.heappop(blocks)
            y = heapq.heappop(blocks)
            new_block = max(x, y) + split
            heapq.heappush(blocks, new_block)
        return blocks[0]


