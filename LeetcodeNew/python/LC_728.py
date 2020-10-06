

class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        res = []
        for num in range(left, right + 1):
            if self.check(num):
                res.append(num)
        return res

    def check(self, num):
        number = str(num)
        for char in list(number):
            if char == '0' or num % int(char) != 0:
                return False
        return True



class Solution2:
    def selfDividingNumbers(self, left: int, right: int):

        res = []
        for num in range(left, right + 1):
            if self.check(num):
                res.append(num)
        return res

    def check(self, num):
        x = num
        while x > 0:
            d = x % 10
            x //= 10
            if d == 0 or num % d != 0:
                return False
        return True
