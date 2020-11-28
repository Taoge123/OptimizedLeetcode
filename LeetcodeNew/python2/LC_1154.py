import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        first = datetime.datetime.strptime(date, "%Y-%m-%d")
        second = datetime.datetime.strptime(date.split("-")[0 ] +"-01-01", "%Y-%m-%d")
        return (first - second).days + 1



