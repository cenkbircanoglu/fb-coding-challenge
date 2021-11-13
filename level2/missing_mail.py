import decimal
from typing import List

decimal.getcontext().prec = 6


# Write any import statements here


def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    if S == 0:
        return sum(V) - C
    if S == 1:
        return sum([max(0, j - C) for i, j in enumerate(V)])

    cache_list = [0] * (N + 1)
    dp = cache_list.copy()
    last_value = 0
    for i, v in enumerate(V):
        last_value *= (1 - S)
        last_value += v
        cache_list[i + 1] = last_value
    for i in range(N - 1, -1, -1):
        tmp = [0] * (N + 1)
        for last_clear in range(i + 1):
            previous = cache_list[i + 1] - cache_list[last_clear] * (1 - S) ** (i - last_clear + 1)
            tmp[last_clear] = max(previous - C + dp[i + 1], dp[last_clear])
        dp = tmp.copy()
    return round(dp[0], 6)


N = 5
V = [10, 2, 8, 6, 4]
C = 5
S = 0.0

res = getMaxExpectedProfit(N, V, C, S)
print(res)
assert res == 25.00000000

N = 5
V = [10, 2, 8, 6, 4]
C = 5
S = 1.0

res = getMaxExpectedProfit(N, V, C, S)
print(res)
assert res == 9.00000000

N = 5
V = [10, 2, 8, 6, 4]
C = 3
S = 0.5

res = getMaxExpectedProfit(N, V, C, S)
print(res)
assert res == 17.00000000

N = 5
V = [10, 2, 8, 6, 4]
C = 3
S = 0.15

res = getMaxExpectedProfit(N, V, C, S)
print(res)
assert res == 20.10825000
