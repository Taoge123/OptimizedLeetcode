"""
0 1 2 3 4 5 6 7 8 9
   *     + ** +


getIdx(0) = (((((nums[0]*a)+b)*c)*d)+e) = nums[0] * mul + add
getIdx(1) = (((((nums[1]*a)+b)*c)*d)+e) = nums[1] * mul + add
getIdx(2) = ((((nums[1]+b)*c)*d)+e) = nums[1] * mul + add
          = (((((val*a)+b)*c)*d)+e) = nums[1] = val * mul + add

val = nums[2]/a

before appending(nums[i])
{mul, add}
append val, s.t. val*mul+add = nums[i]

{mul, add}
getIdx(i) -> val * mul + add

append: val = (nums[i] - add) / mul
val' = (nums[i] - add) * inv(mul)

val' % mod = val % mod

inverse element: 逆元
x / a = x * b (mod)

b = inv(a)
a = inv(b)

<=> a 互质 mod

"""


class Fancy:
    def __init__(self):
        self.mod = 10 ** 9 + 7
        self.nums = []
        self.mul = 1
        self.add = 0

    def quickPow(self, x, y):
        res = 1
        cur = x
        while y:
            if y & 1:
                res = res * cur % self.mod
            cur = cur * cur % self.mod
            y >>= 1
        return res

    def inv(self, x):
        return self.quickPow(x, self.mod - 2)

    def append(self, val: int) -> None:
        val = (val - self.add) % self.mod
        val = (val * self.inv(self.mul)) % self.mod
        self.nums.append(val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1
        return (self.nums[idx] * self.mul % self.mod + self.add) % self.mod


