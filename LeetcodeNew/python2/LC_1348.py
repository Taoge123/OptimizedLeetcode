import collections


class TweetCounts:
    def __init__(self):
        self.table = collections.defaultdict(list)

    def recordTweet(self, tweetName, time):
        self.table[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        times = self.table[tweetName]
        times.sort()
        if freq == 'minute':
            interval = 60
        if freq == 'hour':
            interval = 3600
        if freq == 'day':
            interval = 86400
        res = []
        x = startTime
        while x <= endTime:
            i = bisect.bisect_left(times, x)
            j = bisect.bisect_left(times, min(x + interval, endTime + 1))
            res.append( j -i)
            x += interval
        return res




