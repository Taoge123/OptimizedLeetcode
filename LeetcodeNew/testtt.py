import functools

def findValidDiscountCoupons(discounts):
    res = []
    for s in discounts:
        if check(s):
            res.append(1)
        else:
            res.append(0)
    return res


memo = {}
def check(s):
    if not s:
        return True

    return dfs(s, 0, len(s) - 1)

def dfs(s, i, j):
    if (i, j) in memo:
        return memo[(i, j)]

    if not s:
        return True

    if i > j:
        return True

    if s[i] == s[j] and i != j:
        res = dfs(s, i + 1, j - 1)
        memo[(i, j)] = res
        return res

    for k in range(i + 1, j):
        # print(s[i:k+1], s[k: j])
        if dfs(s, i, k) and dfs(s, k + 1, j):
            memo[(i, j)] = True
            return True
    memo[(i, j)] = False
    return False


discounts = ["abba", "bbaa", "bcb"]
print(findValidDiscountCoupons(discounts))
# s = "bcb"
# print(check(s))