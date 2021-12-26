
import math
import heapq

def bestCombo(popularity, k):

    num = math.ceil(math.log(k, 2))
    nums = [(abs(popularity[0]), popularity[0])]
    i = 0
    for node in popularity[1:]:
        # print(nums)
        if len(nums) < num:
            heapq.heappush(nums, (-abs(node), node))
        else:
            heapq.heappushpop(nums, (-abs(node), node))
        i += 1
    small = []
    while nums:
        node, val = heapq.heappop(nums)
        small.append(val)
    # print(nums)
    small_nums = subsets(small)
    small_nums.sort()
    summ = sum(popularity)
    res = []
    for i in range(k):
        res.append(summ - small_nums[i])
    return res


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


popularity = [1, 2, 3, 1000]
k = 4

print(bestCombo(popularity, k))



