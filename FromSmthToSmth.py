def to_(n, base, b):
    while n > 0:
        b += str(n % base)
        n //= base
    print(b)


n = int(input())
base = int(input())
b = ''
summa = 0
