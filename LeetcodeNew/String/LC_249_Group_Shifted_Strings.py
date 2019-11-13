import collections

class Solution:
    def groupStrings(self, strings):

        table = collections.defaultdict(list)
        for string in strings:
            key = ""
            for i in range(len(string) - 1):
                diff = str((ord(string[i + 1]) - ord(string[i])) % 26)
                key += str(diff)
            # key = ''.join(key)
            table[key].append(string)

        return table.values()



strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

a = Solution()
print(a.groupStrings(strings))







