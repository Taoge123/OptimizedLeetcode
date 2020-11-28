"""
https://leetcode.com/problems/put-boxes-into-the-warehouse-i/discuss/814143/Python-Greedy-approach-with-example-O(NlogN-%2B-M)-O(1)
Idea

We update the height of warehouse rooms, warehouse[i], to be min(warehouse[:i+1]). Then, we sort all boxes and greedily push boxes to the right.


Example

boxes = [4, 3, 4, 1] => [1, 3, 4, 4] (sorting)
warehouse = [5, 3, 3, 4, 1] => [5, 3, 3, 3, 1] (updating heights)

Match 1 (j = 4, i = 0)

[5, 3, 3, 3, 1]
[1, 3, 4, 4]
Match 2 (j = 3, i = 1)

[5, 3, 3, 3, 1]
[1, 3, 4, 4]
Match 3 (j = 0, i = 2)

[5, 3, 3, 3, 1]
[1, 3, 4, 4]
We return ans = 3.


Complexity

Time complexity: O(NlogN + M)
Space complexity: O(1)

"""


class Solution:
    def maxBoxesInWarehouse(self, boxes, warehouse) -> int:
        n = len(boxes)
        m = len(warehouse)
        res = 0
        boxes.sort()
        for i in range(n - 1, -1, -1):
            if boxes[i] <= warehouse[res]:
                res += 1
                if res == m:
                    return m
        return res




