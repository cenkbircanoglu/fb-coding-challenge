from typing import List


# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    # Write your code here
    cnt = max(S) // 2
    need_1 = False
    for i in S:
        if i % 2 == 1:
            need_1 = True
            break
    return cnt + need_1


N = 6
S = [1, 2, 3, 4, 5, 6]

res = getMinProblemCount(N, S)
assert res == 4

N = 4
S = [4, 3, 3, 4]

res = getMinProblemCount(N, S)
assert res == 3

N = 4
S = [2, 4, 6, 8]
res = getMinProblemCount(N, S)
assert res == 4
