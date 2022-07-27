
class Solution:
    def longestCommonSubpath(self, n: int, paths) -> int:
        # binary search the size of subpath --> check if it's common path

        minn = float('inf')
        for path in paths:
            minn = min(minn, len(path))

        left, right = 1, minn

        while left <= right:
            mid = left + (right - left) // 2
            if self.isCommonPath(paths, mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    def isCommonPath(self, paths, k):
        base = 10**5 + 1    # 初始值比数据大小 n + 1
        mod = 2 **63 - 1
        prevRow = set()

        for i, path in enumerate(paths):
            curRow = set()
            hashcode = 0

            for j in range(k):
                hashcode = (hashcode * base + path[j]) % mod
            curRow.add(hashcode)

            power = pow(base, k, mod)
            for j in range(k, len(path)):
                hashcode = (hashcode * base + path[j] - path[j - k ] *power) % mod
                curRow.add(hashcode)

            if i == 0:
                prevRow = curRow
            else:
                prevRow = curRow.intersection(prevRow)

            if i > 0 and not prevRow:
                return False

        return len(prevRow) > 0


