import random


# write your code in Python 3.6
def solution(N):
    while N % 10 != 0:
        N += 1

    mini = N // 10
    maxi = 100000000
    if mini == 100000000:
        return maxi * 10

    return random.randint(mini, maxi) * 10;


import random


# write your code in Python 3.6
def solution(N):
    while N % 10 != 0:
        N += 1

    mini = N // 10
    maxi = 100000000
    if mini == 100000000:
        return maxi * 10

    return random.randint(mini, maxi) * 10;




