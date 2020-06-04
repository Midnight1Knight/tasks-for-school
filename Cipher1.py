string = list(str(input()))
move = int(input())
for i in range(0, len(string)):
    j = (i + move) % len(string)
    print(string[j], end="")
