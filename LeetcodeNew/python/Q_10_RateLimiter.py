from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self, rate):
        self.counter = {}
        self.rate = rate  # 1000 per second

    def isallowed(self, userid):
        timestamp = datetime.now()
        if userid not in self.counter:
            self.counter[userid] = [timestamp, 1]
        else:
            new_tokens = int((timestamp - self.counter[userid][0]).total_seconds() * self.rate)
            self.counter[userid][0] += timedelta(seconds=new_tokens*1.0/self.rate)
            self.counter[userid][1] += new_tokens
            if self.counter[userid][1] == 0:
                return False

            self.counter[userid][1] = max(self.rate, self.counter[userid][1] - 1)
            return True


