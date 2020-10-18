"""

aaa
aaa

"""

import collections

"""

aaa
aaa

"""


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        if A == B:
            count = collections.Counter()
            for ch in A:
                count[ch] += 1

            for num in count.values():
                if num > 1:
                    return True

        first, second = -1, -1
        for i in range(len(A)):
            if A[i] != B[i]:
                if first == -1:
                    first = i
                elif second == -1:
                    second = i
                else:
                    return False

        return second != -1 and A[first] == B[second] and A[second] == B[first]





