
"""
https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/discuss/840231/Javascript-Python3-C%2B%2B-Greedy-%2B-Shrinking-Window-i-...-j

put biggest box at a time to either leftmost or rightmost place, and return how many places have we filled in the warehouse

"""


class SolutionTony:
    def maxBoxesInWarehouse(self, box, spot) -> int:
        box.sort(reverse=True)
        i = 0
        j = len(spot) - 1
        k = 0
        res = 0
        while i <= j and k < len(box):
            if box[k] <= max(spot[i], spot[j]):
                res += 1
                if spot[i] < spot[j]:
                    j -= 1
                else:
                    i += 1
            k += 1
        return res



class Solution:
    def maxBoxesInWarehouse(self, boxes, warehouse) -> int:
        boxes.sort(reverse=True)
        box_id = 0
        left = 0
        right = len(warehouse) - 1

        while left <= right and box_id < len(boxes):
            if boxes[box_id] <= warehouse[left]:
                left += 1
            elif boxes[box_id] <= warehouse[right]:
                right -= 1
            box_id += 1

        return left + (len(warehouse ) -1 - right)



