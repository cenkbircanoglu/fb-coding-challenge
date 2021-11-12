from typing import List


# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    # Write your code here
    cnt = 0
    for i in range(N - 1, 0, -1):
        current_value = R[i - 1]
        next_value = R[i]
        if current_value >= next_value:
            current_value = next_value - 1
            if current_value <= 0:
                return -1
            R[i - 1] = current_value
            cnt += 1
    return cnt


N = 5
R = [2, 5, 3, 6, 5]

res = getMinimumDeflatedDiscCount(N, R)
assert res == 3

N = 3
R = [100, 100, 100]

res = getMinimumDeflatedDiscCount(N, R)
assert res == 2

N = 4
R = [6, 5, 4, 3]

res = getMinimumDeflatedDiscCount(N, R)
assert res == -1
