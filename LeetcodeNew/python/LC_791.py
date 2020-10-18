"""
Idea: Use a dictionary dicS to map each character in S to its index in S,
and use another dictionary dicT to count the number of occurrences of characters in T. We initialize a list res of
empty strings of length len(S). We enumerate over the key, val pairs in dicS, if key is in dicT,
we let res[val] = key*dicT[key]. This puts all characters in T that also appear in S in the correct order
(i.e., according to the order in S). Next, we enumerate over the key, val pairs in dicT,
if key does not appear in S, we append key*val to res. Finally, we return "".join(res).

Time complexity: O(len(S)+len(T)), space complexity: O(len(S)+len(T)).
"""


import collections

class Solution:
    def customSortString(self, S: str, T: str) -> str:

        tableS = {char :i for i, char in enumerate(S)}
        tableT = collections.Counter(T)
        res = [""] * len(S)

        for k, val in tableS.items():
            if k in tableT:
                res[val] = k * tableT[k]

        for k, val in tableT.items():
            if k not in tableS:
                res.append(k * val)

        return "".join(res)



class Solution2:
    def customSortString(self, S: str, T: str) -> str:
        count = collections.defaultdict(int)
        res = []

        for ch in T:
            count[ch] += 1

        for ch in S:
            while count[ch] > 0:
                res.append(ch)
                count[ch] -= 1

        for ch in T:
            while count[ch] > 0:
                res.append(ch)
                count[ch] -= 1

        return "".join(res)


