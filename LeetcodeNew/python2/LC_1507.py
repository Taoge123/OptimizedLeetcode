
class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month = str(months.index(month) + 1).zfill(2)
        return f'{year}-{month}-{day[:-2].zfill(2)}'

