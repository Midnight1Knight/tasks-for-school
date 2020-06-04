def recursion(N):
    N *= 10
    if N != 0:
        print(N % 10)
        return recursion(N // 100)
    else:
        return 0


n = int(input())
print(recursion(n))
