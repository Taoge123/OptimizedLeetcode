"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution:
    def countAndSay(self, n: int) -> str:

        res = "1"
        for i in range( n -1):
            curr = res[0]
            temp = ''
            count = 0
            for letter in res:
                if curr == letter:
                    count += 1
                else:
                    temp += str(count) +curr
                    curr = letter
                    count = 1
            temp += str(count ) +curr
            res = temp

        return res


class SolutionTony:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(n - 1):
            count = 1
            temp = []
            for i in range(1, len(res)):
                if res[i] == res[i - 1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(res[i - 1])
                    count = 1
            temp.append(str(count))
            temp.append(res[-1])
            res = ''.join(temp)
        return res


"""
Input: 4
Output: "1211
"""

n = 4
a = SolutionTony()
print(a.countAndSay(n))



