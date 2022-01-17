
"""
aabb



"""

import functools

def findValidDiscountCoupons(discounts):
    res = []
    cache = {}
    for s in discounts:
        if s in cache:
            temp = cache[s]
        else:
            temp = check(s)
            cache[s] = temp
        if temp:
            res.append(1)
        else:
            res.append(0)
    return res


def check(s) :
    stack = []
    for ch in s:
        if stack and stack[-1] != ch:
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(ch)
    return not stack





discounts = ["abba", "bbaa", "bcb"]
print(findValidDiscountCoupons(discounts))
# s = "bcb"
# print(check(s))


