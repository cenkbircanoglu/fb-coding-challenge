from typing import List


# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    cnt = 0
    previous = 1
    for i in C:
        cnt += min((previous - i) % N, (i - previous) % N)
        previous = i
    return cnt


N = 3
M = 3
C = [1, 2, 3]

res = getMinCodeEntryTime(N, M, C)
print(res)
assert res == 2

N = 10
M = 4
C = [9, 4, 4, 8]
res = getMinCodeEntryTime(N, M, C)
print(res)
assert res == 11
