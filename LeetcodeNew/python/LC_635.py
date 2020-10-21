import collections

class LogSystem:
    def __init__(self):
        self.timeStamp = []
        self.index = collections.defaultdict(int)
        self.index["Year"] = 4
        self.index["Month"] = 7
        self.index["Day"] = 10
        self.index["Hour"] = 13
        self.index["Minute"] = 16
        self.index["Second"] = 19

    def put(self, id: int, timestamp: str) -> None:
        self.timeStamp.append([int(id), timestamp])

    def retrieve(self, start: str, end: str, granularity: str):
        res = []
        idx = self.index[granularity]
        for ts in self.timeStamp:
            if ts[1][:idx] >= start[:idx] and ts[1][:idx] <= end[:idx]:
                res.append(ts[0])
        return res


