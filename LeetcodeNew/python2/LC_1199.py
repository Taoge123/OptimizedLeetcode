"""
1167. Minimum Cost to Connect Sticks


https://leetcode.com/problems/minimum-time-to-build-blocks/discuss/387035/Python%3A-O(n-log-n)-using-Huffman's-Algorithm-(priority-queue)-with-explanation.

I understood the solution by building an example. Hope it helps.
For a specified question mentioned by another poster, I mean [1, 2, 4, 7, 10] with split cost 3. We can find the optimal tree as follow. Initial we have one worker and the cost is 0. It can be split into two with cost of 3 for each. For the rest, 0 means no splitting.
....................0
.............3...........3
........3.........3.............0
....3.......3.........0.............0
.3....3......0..........0..............0
.1....2........4............7.............10
If we can see this, the solution will be easier to understand.
Pop least two elements 1, 2 and change the tree to(with the cost of 3)
....................0
.............3...........3
........3.........3.............0
....3.......3.........0.............0
....4....... 5.........7............ 10
Pop least two elements 4, 5 and change the tree to
....................0
.............3...........3
........3.........3.............0
.......7.. .........8............ 10
Pop least two elements 7, 9and change the tree to
....................0
.............3...........3
...........11 ......... 12

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


