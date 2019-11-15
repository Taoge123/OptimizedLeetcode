
class Solution:
    def compareVersion(self, version1, version2):
        l1 = [int(n) for n in version1.split('.')]
        l2 = [int(n) for n in version2.split('.')]
        for i in range(max(len(l1), len(l2))):
            a = l1[i] if i < len(l1) else 0
            b = l2[i] if i < len(l2) else 0

            if a < b:
                return -1
            elif a > b:
                return 1
        return 0




