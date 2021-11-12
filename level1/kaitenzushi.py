from collections import deque, Counter
from typing import List


# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Write your code here
    q = deque()
    cnt = 0
    dish_counter = Counter()
    for i in D:
        if dish_counter[i] == 0:
            cnt += 1
            q.append(i)
            dish_counter[i] += 1
            if len(q) == K + 1:
                remove = q.popleft()
                dish_counter[remove] -= 1

    return cnt


N = 6
D = [1, 2, 3, 3, 2, 1]
K = 1

res = getMaximumEatenDishCount(N, D, K)
assert res == 5

N = 6
D = [1, 2, 3, 3, 2, 1]
K = 2

res = getMaximumEatenDishCount(N, D, K)
assert res == 4

N = 7
D = [1, 2, 1, 2, 1, 2, 1]
K = 2
res = getMaximumEatenDishCount(N, D, K)
assert res == 2
