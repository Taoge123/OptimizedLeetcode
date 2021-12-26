

def bestCombo(popularity, k):
    res = subsets(popularity)
    # print(res)
    res.sort(reverse=True)
    return res[:k]

def subsets(nums):
    res = []
    dfs(nums, 0, 0, res)
    return res

def dfs(nums, pos, summ, res):
    if pos == len(nums):
        res.append(summ)
        return res

    dfs(nums, pos + 1, summ + nums[pos], res)
    dfs(nums, pos + 1, summ, res)


popularity = [3, 5, -2]
k = 3

print(bestCombo(popularity, k))

