
class Solution:
    def average(self, salary) -> float:
        mini, maxi = min(salary), max(salary)

        summ = 0
        count = 0
        for num in salary:
            if num in [mini, maxi]:
                continue
            summ += num
            count += 1
        return summ / count


