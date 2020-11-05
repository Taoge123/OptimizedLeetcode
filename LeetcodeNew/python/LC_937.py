
"""
https://leetcode.com/problems/reorder-data-in-log-files/discuss/779319/Python-Custom-Sort-Solution-With-Explanation
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []

        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        letter.sort(key=lambda x: x.split()[0])
        letter.sort(key=lambda x: x.split()[1:])

        letter.extend(digit)

        return letter


