


class Solution:
    def __init__(self):
        self.days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ]

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month < 3:
            month += 12
            year -= 1

        c, year = year // 100, year % 100
        w = ( c//4 - 2 * c + year + year // 4 + 13 * (month +1) // 5 + day - 1) % 7
        return self.days[w]



class Solution2:
    def dayOfTheWeek(self, d, m, y):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        from datetime import datetime
        return days[datetime(y, m, d).weekday()]


