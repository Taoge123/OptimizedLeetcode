import math

class Solution:
    def fractionAddition(self, expression):
        expression = expression.replace('+', ' +').replace('-', ' -')
        fracs = [x.split('/') for x in expression.split()]
        deno = 1
        for i in set([int(x[1]) for x in fracs]):
            deno *= i
        nume = 0
        for n, d in fracs:
            n, d = int(n), int(d)
            nume += n * (deno // d)
        gcd = math.gcd(abs(nume), deno)
        return '{}/{}'.format(nume // gcd, deno // gcd)

