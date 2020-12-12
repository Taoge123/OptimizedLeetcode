import collections


class Solution:
    def alertNames(self, keyName, keyTime):

        def alert(nums):
            for i in range(len(nums ) -2):
                if nums[ i +2] - nums[i] <= 60:
                    return True
            return False

        table = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour, mins = map(int, time.split(':'))
            table[name].append(hour * 60 + mins)

        res = []
        for name in table:
            table[name].sort()
            if alert(table[name]):
                res.append(name)

        return sorted(res)



