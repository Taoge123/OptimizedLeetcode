import collections

class Solution:
    def findDuplicate(self, paths):
        table = collections.defaultdict(list)
        for path in paths:
            content = path.split(" ")
            for i in range(1, len(content)):
                word = content[i].split("(")
                word[1] = word[1].replace(")", "")
                res = table[word[1]]
                res.append(content[0] + "/" + word[0])
                table[word[1]] = res

        res = []
        for key in table.keys():
            if len(table[key]) > 1:
                res.append(table[key])

        return res


paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

a = Solution()
print(a.findDuplicate(paths))


