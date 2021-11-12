# Write any import statements here
# Write any import statements here
import itertools


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    counter = 0
    for i, j, k in itertools.combinations(range(N), 3):
        if X <= abs(i - j) <= Y and X <= abs(j - k) <= Y:
            counter += (C[i] == 'P' and C[j] == 'A' and C[k] == 'B') or (
                    C[i] == 'B' and C[j] == 'A' and C[k] == 'P')
    return counter


res = getArtisticPhotographCount(5, 'APABA', 1, 2)
assert res == 1
res = getArtisticPhotographCount(5, 'APABA', 2, 3)
assert res == 0
res = getArtisticPhotographCount(8, '.PBAAP.B', 1, 3)
assert res == 3
