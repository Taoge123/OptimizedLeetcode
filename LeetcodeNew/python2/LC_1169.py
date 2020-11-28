import collections

class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city


class Solution:
    def invalidTransactions(self, transactions):
        trans = [Transaction(*t.split(',')) for t in transactions]
        trans.sort(key=lambda t: t.time)  # O(nlogn) time
        table = collections.defaultdict(list)
        for i, t in enumerate(trans):  # O(n) time
            table[t.name].append(i)

        res = []
        for name, indexes in table.items():  # O(n) time
            left = right = 0
            for i, currIndex in enumerate(indexes):
                curr = trans[currIndex]
                if (curr.amount > 1000):
                    res.append("{},{},{},{}".format(curr.name, curr.time, curr.amount, curr.city))
                    continue
                while left <= len(indexes) - 2 and trans[indexes[left]].time < curr.time - 60:  # O(60) time
                    left += 1
                while right <= len(indexes) - 2 and trans[indexes[right + 1]].time <= curr.time + 60:  # O(60) time
                    right += 1
                for i in range(left, right + 1):  # O(120) time
                    if trans[indexes[i]].city != curr.city:
                        res.append("{},{},{},{}".format(curr.name, curr.time, curr.amount, curr.city))
                        break
        return res




class Solution2:
    def invalidTransactions(self, transactions):
        res = set()
        transactions = [Transaction(*t.split(',')) for t in transactions]  # O(n) time
        transactions.sort(key=lambda t: t.time)  # O(nlogn) time

        for i in range(len(transactions)):  # O(n^2) time
            t1 = transactions[i]
            if t1.amount > 1000:
                res.add("{},{},{},{}".format(t1.name, t1.time, t1.amount, t1.city))
            for j in range(i + 1, len(transactions)):
                t2 = transactions[j]
                if t2.name == t1.name and t2.time - t1.time <= 60 and t2.city != t1.city:
                    res.add("{},{},{},{}".format(t1.name, t1.time, t1.amount, t1.city))
                    res.add("{},{},{},{}".format(t2.name, t2.time, t2.amount, t2.city))
        res = list(res)
        return res


class Solution3:
    def invalidTransactions(self, transactions):
        table = []
        for node in transactions:
            temp = node.split(',')
            temp[1] = int(temp[1])
            temp[2] = int(temp[2])
            table.append(temp)

        res = []
        for node in table:
            if node[2] > 1000:
                node[1] = str(node[1])
                node[2] = str(node[2])
                res.append(','.join(node))
                continue
            for x in table:
                if node[0] == x[0] and abs(node[1] - int(x[1])) <= 60 and node[3] != x[3]:
                    node[1] = str(node[1])
                    node[2] = str(node[2])
                    res.append(','.join(node))
                    break
        return res




