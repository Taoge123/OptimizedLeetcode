class StringIteratorTLE:
    def __init__(self, s: str):
        self.res = []
        self.index = 0
        i = 0
        while i < len(s):
            ch = s[i]
            i += 1
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            for k in range(num):
                self.res.append(ch)

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        res = self.res[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        return self.index != len(self.res)



class StringIterator:
    def __init__(self, s: str):
        self.res = list(s)
        self.index = 0
        self.num = 0
        self.ch = ' '

    def next(self) -> str:
        if not self.hasNext():
            return ' '

        if self.num == 0:
            self.ch = self.res[self.index]
            self.index += 1
            while self.index < len(self.res) and self.res[self.index].isdigit():
                self.num = self.num * 10 + int(self.res[self.index])
                self.index += 1

        self.num -= 1
        return self.ch

    def hasNext(self) -> bool:
        return self.index != len(self.res) or self.num != 0


