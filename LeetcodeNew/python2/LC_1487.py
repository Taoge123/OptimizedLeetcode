
class Solution:
    def getFolderNames(self, names):
        visited = {}
        res = []
        for name in names:
            if name in visited:
                while name + "(" + str(visited[name]) + ")" in visited:
                    visited[name] += 1
                visited[name + "(" + str(visited[name]) + ")" ] =1
                res.append(name + "(" + str(visited[name]) + ")")
                visited[name] += 1
            else:
                res.append(name)
                visited[name] = 1
        return res



