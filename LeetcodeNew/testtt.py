

def calculate_prime_factors(input):
    i = 2
    res = []
    while i * i <= input:
        if input % i:
            i += 1
        else:
            input //= i
            res.append(i)
    if input > 1:
        res.append(input)
    return res


def test():
    assert calculate_prime_factors(6) == [2, 3]


