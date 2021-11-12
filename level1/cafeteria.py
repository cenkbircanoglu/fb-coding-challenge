from typing import List


# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    if N // (K + 1) == M:
        return 0
    S.sort()
    addition = 0
    for s, t in zip([-K] + S, S + [N + K + 1]):
        addition += (t - s) // (K + 1) - 1
    return addition


res = getMaxAdditionalDinersCount(10, 1, 2, [2, 6])
assert res == 3
res = getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14])
assert res == 1
