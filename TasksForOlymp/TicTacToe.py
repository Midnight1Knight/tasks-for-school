def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4s}".format(matrix[i][j]), end="")
        print()


def placeOfTic(matrix):
    print("Введите место крестика (по вертикали и горизонтали, начиная с нуля)")
    vertical = int(input())
    horizontal = int(input())
    matrix[vertical][horizontal] = "X"


def placeOfTac(matrix):
    print()


def winning(matrix):
    if (
        (matrix[0][0] == matrix[0][1] == matrix[0][2] == "O") or
        (matrix[1][0] == matrix[1][1] == matrix[1][2] == "O") or
        (matrix[2][0] == matrix[2][1] == matrix[2][2] == "O") or
        (matrix[0][0] == matrix[1][0] == matrix[2][0] == "O") or
        (matrix[0][1] == matrix[1][1] == matrix[2][1] == "O") or
        (matrix[0][2] == matrix[1][2] == matrix[2][2] == "O") or
        (matrix[0][0] == matrix[1][1] == matrix[2][2] == "O") or
        (matrix[0][2] == matrix[1][1] == matrix[2][0] == "O")
    ):
        return 1
    elif(
        (matrix[0][0] == matrix[0][1] == matrix[0][2] == "X") or
        (matrix[1][0] == matrix[1][1] == matrix[1][2] == "X") or
        (matrix[2][0] == matrix[2][1] == matrix[2][2] == "X") or
        (matrix[0][0] == matrix[1][0] == matrix[2][0] == "X") or
        (matrix[0][1] == matrix[1][1] == matrix[2][1] == "X") or
        (matrix[0][2] == matrix[1][2] == matrix[2][2] == "X") or
        (matrix[0][0] == matrix[1][1] == matrix[2][2] == "X") or
        (matrix[0][2] == matrix[1][1] == matrix[2][0] == "X")
    ):
        return -1
    else:
        return 0


matrix = [["ы", "ы", "ы"],
          ["ы", "ы", "ы"],
          ["ы", "ы", "ы"]]
for i in range(1, 9):
    placeOfTic(matrix)
    placeOfTac(matrix)
    printMatrix(matrix)
    print()
    if winning(matrix) == 1:
        print("Победа ноликов!")
        break
    elif winning(matrix) == -1:
        print("Победа крестиков!")
        break
