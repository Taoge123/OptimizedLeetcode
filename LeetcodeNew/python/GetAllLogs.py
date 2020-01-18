import collections
import bisect


class ServiceManager():
    def __init__(self):
        self.d = {}
        self.pq = []

    def addService(self, service):
        if service not in self.d:
            self.d[service] = []

    def addServiceCall(self, service, time, payload):
        if service in self.d:
            bisect.insort_left(self.pq, (time, payload))

    def getAllServiceCallsBetweenTimes(self, time1, time2):
        idx1 = bisect.bisect_left(self.pq, (time1, ))
        idx2 = bisect.bisect_right(self.pq, (time2, ))
        return [i[1] for i in self.pq[idx1: idx2]]

m = ServiceManager()
m.addService("A")
m.addService("B")
m.addServiceCall("A", 1, "abc")
m.addServiceCall("A", 5, "abec")
m.addServiceCall("B", 3, "ac")
print(m.getAllServiceCallsBetweenTimes(1, 4)) # ["abc", "ac"]