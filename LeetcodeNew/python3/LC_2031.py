class BinaryIndexTree:
    def __init__(self, n):
        self.BIT = [0] * (n + 1)

    def _lowbit(self, i):
        return i & -i

    def query(self, i):
        count = 0
        while i > 0:
            count += self.BIT[i]
            i -= i & -i
        return count

    def update(self, i, val):
        while i < len(self.BIT):
            self.BIT[i] += val
            i += i & -i


class SolutionRika1:  # compress nums + BIT
    def subarraysWithMoreZerosThanOnes(self, nums) -> int:
        # similar to 315. Count of smaller numbers after self -----> sum1 - sum2 > 0 ==> sum1 > sum2
        # get prefSum
        prefsum = [0]
        for num in nums:
            if num == 0:
                prefsum.append(prefsum[-1] + (-1))
            else:
                prefsum.append(prefsum[-1] + num)

        # sort prefsum
        sortedSum = sorted(list(set(prefsum)))
        # compress sorted prefsum and save index
        index = {}
        for i, num in enumerate(sortedSum):
            index[num] = i + 1

        # operation --> find sum1 > sum2
        mod = 10 ** 9 + 7
        res = 0
        tree = BinaryIndexTree(len(prefsum))
        for i in range(len(prefsum)):
            res += tree.query(index[prefsum[i]] - 1)
            tree.update(index[prefsum[i]], 1)
        return res % mod



class SolutionRika2:
    def subarraysWithMoreZerosThanOnes(self, nums) -> int:
        presum = [0]
        for num in nums:
            if num == 0:
                presum.append(presum[-1] + (-1))
            else:
                presum.append(presum[-1] + num)

        mini, maxi = min(presum), max(presum)
        tree = BinaryIndexTree(maxi - mini + 1)

        res = 0
        mod = 10 ** 9 + 7
        for sum1 in presum:  # sum1 - sum2 > 0 ----> sum2 < sum1
            res += tree.query(sum1 - mini)
            tree.update(sum1 - mini + 1, 1)
        return res % mod






