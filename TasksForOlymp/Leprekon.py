A = int(input())
B = int(input())
if A > B:
    mid = A
    A = B
    B = mid
if A % 2 != 0:
    A += 1
if B % 2 == 0:
    B -= 1
N = B // A
print(N)
