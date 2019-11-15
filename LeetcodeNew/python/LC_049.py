
class Solution:
    def groupAnagrams(self, strs):

        table = {}

        for word in strs:
            word_key = "".join(sorted(word))

            if word_key not in table:
                table[word_key] = [word]
            else:
                table[word_key].append(word)

        result = []
        for value in table.values():
            result += [value]

        return result



