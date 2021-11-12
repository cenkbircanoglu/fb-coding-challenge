# Write any import statements here
# Write any import statements here


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    counter = 0
    possible_pabs = 0
    possible_baps = 0

    return counter


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
