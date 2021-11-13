from typing import List


# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    P.sort()
    current_ind = 0
    hops = 0
    while current_ind != F - 1:
        hop = P[current_ind + 1] - P[current_ind] - 1
        hops += hop
        current_ind += 1
    hops += (N - P[-1]) + (F - 1)
    return hops


N = 3
F = 1
P = [1]
res = getSecondsRequired(N, F, P)
print(res)
assert res == 2

N = 6
F = 3
P = [5, 2, 4]
res = getSecondsRequired(N, F, P)
print(res)
assert res == 4

N = 6
F = 2
P = [2, 4]
res = getSecondsRequired(N, F, P)
print(res)
assert res == 4
3, 4
4, 5
5, 6
6
