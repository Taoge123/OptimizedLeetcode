class UseMainCode(object):
    @classmethod
    def RangeSize(cls, input1):
        print(input1)
        cls.convert(input1)
        
    @classmethod
    def convert(self, s):
        res = 0
        for i in s:
            res = res*4 + ord(i)-ord('A')+1
        print(res)
        return res

a = UseMainCode()
a.RangeSize('A1:AA2')




