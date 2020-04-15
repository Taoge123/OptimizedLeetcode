# class UseMainCode(object):
#     @classmethod
#     def RangeSize(cls, input1):
#         print(input1)
#         cls.convert(input1)
#
#     @classmethod
#     def convert(self, s):
#         res = 0
#         for i in s:
#             res = res*4 + ord(i)-ord('A')+1
#         print(res)
#         return res
#
# a = UseMainCode()
# a.RangeSize('A1:AA2')
#
#
#
#
class Solution:
    def entityParser(self, text: str) -> str:
        stack = []
        for i, char in enumerate(text):
            stack.append(char)
            print(stack[-5:])
            if stack[-6:] == ['&', 'q', 'u', 'o', 't', ';']:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('\"')

            if stack[-5:] == ['&', 'a', 'p', 'o', 's', ';']:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('\'')

            if stack[-7:] == ['&', 'f', 'r', 'a', 's', 'l', ';']:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('/')

            if stack[-4:] == ['a', 'm', 'p', ';']:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()

            if stack[-4:] == ['&', 'g', 't', ';']:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('>')

            if stack[-4:] == ['&', 'l', 't', ';']:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('<')

        return "".join(stack)


text = "and I quote: &quot;...&quot;"
a = Solution()
print(a.entityParser(text))



