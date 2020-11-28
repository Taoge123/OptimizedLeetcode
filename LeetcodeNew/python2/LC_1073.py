
"""
(-5)//(-3) => q=2, r=1
(-5)//(-3) => q=1, r=-2


1073.Adding-Two-Negabinary-Numbers
本题可以认为是1017.Convert-to-Base--2的follow up.

此题的目的是希望实现类似于K进制的大数加法。“大数加法”是说，两个加数特别大、装不进内存的时候，就以数组的形式储存，我们需要逐位相加来实现最终的结果。

本题的第一步可以先实现一个普通的K进制大数相加的算法。然后将其中的进制K，改成-2进制即可，即：

int sum = a+b+carry;
int r = sum%(-2);
carry = sum/(-2);
注意到C++中的除法运算是rounding towards zero，所以为了保证余数是正数，需要做修补：

if (r<0)
{
  r+=abs(2);
  carrry+=1;
}
此外，我们需要注意，对于普通的K进制相加（K为正数），M位数和M位数相加的结果最多可能是M+1位。但是对于K为负数的情况则不一定。
比如说1(-2)+1(-2)=110(-2)。当算完第一次的sum之后，我们得到的carry=-1，说明我们还需要将-1做进一步的转化（为-2进制），
而不能简单的把这个carry附加到结果的最高位。我们的解决方案是，将需要逐位相加的计算次数定义为：len=max(arr1.size(),arr2.size())+2，
其中+2就是为了应对上面的情况。显然，我们需要在arr1和arr2的最高位前都做补零处理。

当然，上面的操作同样会引入不必要的leading zeros，所以最终结果还需要排除掉这些先导零（除非结果本身就是0）。

"""


class Solution:
    def addNegabinary(self, arr1, arr2):
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        n = max(len(arr1), len(arr2))

        res = []
        carry = 0

        for i in range( n +2):
            a = arr1[i] if i < len(arr1) else 0
            b = arr2[i] if i < len(arr2) else 0

            summ = a + b + carry
            remainder = summ % (-2)
            carry = summ // (-2)

            if remainder < 0:
                carry += 1
                remainder += abs(2)

            res.append(remainder)

        # if carry:
        #     res.append(carry)
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        res = res[::-1]
        return res




