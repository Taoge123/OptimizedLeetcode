import collections
import datetime
import collections

friends = []

tiffany = [datetime.datetime(1992, 2, 16), "老2"]
friends.append(tiffany)

disk = [datetime.datetime(1997, 8, 31), "老5"]
friends.append(disk)

kaiming = [datetime.datetime(1994, 1, 8), "老9"]
friends.append(kaiming)

cilun = [datetime.datetime(1992, 5, 21), "cl大表哥"]
friends.append(cilun)


def find_people(friends):
    res = []
    for node, name in friends:
        if node:
            if node.date().month == datetime.date.today().month and node.date().day == datetime.date.today().day:
                res.append(name)
    return res


print(find_people(friends))





