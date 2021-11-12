# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    # Write your code here
    min_s, max_s = len(str(A)), len(str(B))

    min_val = int('1' * min_s)
    max_val = int('1' * max_s)
    if min_val == max_val:
        return B // max_val - (A - 1) // min_val
    return (max_s - min_s - 1) * 9 + 9 - ((A - 1) // min_val) + B // max_val


A = 75
B = 300
res = getUniformIntegerCountInInterval(A, B)
print(res)
assert res == 5
A = 1
B = 9
res = getUniformIntegerCountInInterval(A, B)
print(res)
assert res == 9

A = 999999999999
B = 999999999999

res = getUniformIntegerCountInInterval(A, B)
print(res)
assert res == 1
