


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        table = collections.defaultdict(int)
        table[0] = -1
        count = [0] * 5
        res = 0
        for i in range(len(s)):
            if s[i] == 'a':
                count[0] += 1
            elif s[i] == 'e':
                count[1] += 1
            elif s[i] == 'i':
                count[2] += 1
            elif s[i] == 'o':
                count[3] += 1
            elif s[i] == 'u':
                count[4] += 1
            key = self.convert(count)
            if key in table:
                res = max(res, i - table[key])
            else:
                # if key never there before, we add this key, because we want the largest bandwith
                table[key] = i
        return res

    def convert(self, count):
        key = 0
        for i in range(5):
            if count[i] % 2 == 1:
                key += (1 << i)
        return key


