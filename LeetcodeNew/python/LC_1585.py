
import collections




class Solution2:
    def isTransformable(self, s: str, t: str) -> bool:
        places = collections.defaultdict(list)
        for i in reversed(range(len(s))):
            key = int(s[i])
            places[key].append(i)

        for e in t:  # we loop over t and check every digit
            key = int(e)  # current digit
            if not places[key]:  # digit is not in s, return False
                return False
            i = places[key][-1]  # location of current digit
            for j in range(key):  # only loop over digits smaller than current digit
                if places[j] and places[j][-1] < i:  # there is a digit smaller than current digit, return false
                    return False
            places[key].pop()
        return True


"""

   0 1 2 3 4 5 6 7 8
s: X X _ X X 6 X X X
t: 5 6 X X X X X X X

"""


class Solution22:
    def isTransformable(self, s: str, t: str) -> bool:

        pos = collections.defaultdict(list)

        for i in range(len(s)):
            pos[ord(s[i]) - ord('0')].append(i)

        for i in range(len(t)):
            num = ord(t[i]) - ord('0')
            if not pos[num]:
                return False
            idx = pos[num][0]

            for digit in range(num):
                if pos.get(digit) and pos[digit][0] < idx:
                    return False
            pos[num].pop(0)
        return True





class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        index = [[] for _ in range(10)]
        pos = [0 for _ in range(10)]

        for i, ch in enumerate(s):
            index[ord(ch) - ord('0')].append(i)

        for ch in t:
            num = ord(ch) - ord('0')
            if pos[num] >= len(index[num]):
                return False
            for i in range(num):
                if pos[i] < len(index[i]) and index[i][pos[i]] < index[num][pos[num]]:
                    return False
            pos[num] += 1
        return True

