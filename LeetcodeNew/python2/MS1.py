import bisect

#max sum of pairs,
#for the pairs, digit sum should be equal
def solution(A):
    d = {}
    for i in range(len(A)):
        digit_sum = sum([int(k) for k in str(A[i])])
        if digit_sum not in d:
            d[digit_sum] = [A[i]]
        else:
            bisect.insort(d[digit_sum], A[i])
    ret = -float('inf')
    for i in d.values():
        if len(i)<2:
            continue
        else:
            ret = max(ret,i[-2]+i[-1])
    print(d)
    if ret == -float('inf'):
        return -1
    return ret



A = [51, 71,17,42, 33]
print(solution(A))



