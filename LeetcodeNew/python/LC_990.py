import string

class Solution:
    def equationsPossible(self, equations):
        if not equations:
            return True
        parent = {i :i for i in string.ascii_lowercase}

        for item in equations:
            if "==" in item:
                i, j = item.split("==")
                self.union(i, j, parent)

        for item in equations:
            if "!=" in item:
                i, j = item.split("!=")
                if self.find(i, parent) == self.find(j, parent):
                    return False
        return True


    def find(self, i, parent):
        if i == parent[i]:
            return parent[i]
        else:
            return self.find(parent[i], parent)

    def union(self, i, j, parent):
        x = self.find(i, parent)
        y = self.find(j, parent)
        parent[x] = y



