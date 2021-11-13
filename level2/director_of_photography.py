# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    return getArtisticPhotographCount_sub(N, C, X, Y) + getArtisticPhotographCount_sub(N, C[::-1], X, Y)


def getArtisticPhotographCount_sub(N, C, X, Y):
    b = 0
    p = C[X - 1:Y].count('P')
    cnt = 0
    for i in range(N):
        if i - X >= 0 and C[i - X] == 'B':
            b += 1
        if i - Y - 1 >= 0 and C[i - Y - 1] == 'B':
            b -= 1
        if i + X - 1 < N and C[i + X - 1] == 'P':
            p -= 1
        if i + Y < N and C[i + Y] == 'P':
            p += 1
        if C[i] == 'A':
            cnt += b * p
    return cnt


N = 5
C = 'APABA'
X = 1
Y = 2
res = getArtisticPhotographCount(N, C, X, Y)
assert res == 1

N = 5
C = 'APABA'
X = 2
Y = 3

res = getArtisticPhotographCount(N, C, X, Y)
assert res == 0

N = 8
C = '.PBAAP.B'
X = 1
Y = 3
res = getArtisticPhotographCount(N, C, X, Y)
assert res == 3
