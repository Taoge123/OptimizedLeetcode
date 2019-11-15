class UseMainCode(object):
    @classmethod
    def RangeSize(cls, input1):
        if not input1:
            return 0
        input1 = input1.split(':')
        if len(input1) != 2:

            return -1
        left, right = input1[0], input1[1]
        leftRow, leftCol = "", ""
        rightRow, rightCol = "", ""
        res = 0
        for i in left:
            if i.isalpha():
                leftRow += i
            else:
                leftCol += i

        for j in right:
            if j.isalpha():
                rightRow += j
            else:
                rightCol += j
        leftRow = cls.convert(leftRow)
        rightRow = cls.convert(rightRow)
        res = (rightRow - leftRow + 1)  * (int(rightCol) - int(leftCol) + 1)
        print(res)
        return res


    @classmethod
    def convert(cls, s):
        res = 0
        for i in s:
            res = res * 4 + ord(i) - ord('A') + 1
        return res


a = UseMainCode()
a.RangeSize('A1:AA2')
a.RangeSize('A1:C2')
a.RangeSize('A1')



class UseMainCode(object):
    @classmethod
    def CountBadPeriods(cls, input1):
        n = len(input1)
        dp = [0] * n
        dp[0] = input1[0]
        for i in range(1, n):
            dp[i] = dp[i-1] + input1[i]
        print(dp)

        res = 0
        index = 0
        while index < n:
            for j in range(index+1, n+1):
                if index +1 >= n:
                    return res
                check = cls.check(dp[index], dp[j])
                if check:

                    index = j
                    res += 1
                    break
            if not check:
                index += 1

        return res
    @classmethod
    def check(cls, num1, num2):
        loss = num2 - float(num1)
        # print(loss)
        return loss / float(num1) <= -0.05


input1 = [30, -1, -1, -2, 1, -3]
a = UseMainCode()
print(a.CountBadPeriods(input1))
print(a.check(30, 29))




