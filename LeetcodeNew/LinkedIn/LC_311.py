



def multiply(self, A, B):
    a, b = len(A), len(A[0])
    c, d = len(B), len(B[0])
    ret = [[0 for i in range(d)] for j in range(a)]
    X, Y = [dict() for i in range(a)], [dict() for j in range(d)]
    for i in range(a):
        for j in range(b):
            if A[i][j] != 0:
                X[i][j] = A[i][j]
    for i in range(c):
        for j in range(d):
            if B[i][j] != 0:
                Y[j][i] = B[i][j]
    for i in range(a):
        for j in range(d):
            for r in X[i]:
                if r in Y[j]:
                    ret[i][j] += X[i][r] * Y[j][r]
    return ret


