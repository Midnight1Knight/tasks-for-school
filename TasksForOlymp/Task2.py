def recursion(N):
    if N != 0:
        return N % 10, N // 10
    else:
        return 0


n = int(input())
print(recursion(n))
