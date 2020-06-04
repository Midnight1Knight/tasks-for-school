n = int(input())
k = int(input())
sm = 0
for i in range(1, n + 1):
    sm += i
    if k <= sm:
        print((str(i) + " ") * (i - (sm - k)))
        break
    print((str(i) + " ") * i)
