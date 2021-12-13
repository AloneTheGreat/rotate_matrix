# python3


#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#
import math


def new_position(M, N, xi, yi, R, I):
    while R != 0:
        while xi > I and R != 0 and yi == N + I - 1:
            xi -= 1
            R -= 1
        while yi > I and R != 0 and xi != M + I - 1:
            yi -= 1
            R -= 1
        while xi < M + I - 1 and R != 0 and yi != N + I - 1:
            xi += 1
            R -= 1
        while yi < N + I - 1 and R != 0 and xi == M + I - 1:
            yi += 1
            R -= 1
    return xi, yi


def matrixRotation(matrix, r, m, n):
    # Write your code here
    result = [[None for _ in range(n)] for _ in range(m)]
    n_circles = min(m, n) // 2
    for i in range(n_circles):
        l = ((m - 1) * 2) + ((n - 1) * 2)
        new_r = r % l
        X, Y = i, i
        for x in range(i, m + i - 1, 1):
            xf, yf = new_position(m, n, x, Y, new_r, i)
            result[xf][yf] = matrix[x][Y]
            X = x + 1
        for y in range(i, n + i - 1, 1):
            xf, yf = new_position(m, n, X, y, new_r, i)
            result[xf][yf] = matrix[X][y]
            Y = y + 1
        for x in range(m + i - 1, i, -1):
            xf, yf = new_position(m, n, x, Y, new_r, i)
            result[xf][yf] = matrix[x][Y]
            X = x - 1
        for y in range(n + i - 1, i, -1):
            xf, yf = new_position(m, n, X, y, new_r, i)
            result[xf][yf] = matrix[X][y]
        m = m - 2
        n = n - 2
    for k in result:
        print(*k)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    row = int(first_multiple_input[0])

    col = int(first_multiple_input[1])

    rot = int(first_multiple_input[2])

    matrixx = []

    for _ in range(row):
        matrixx.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrixx, rot, row, col)
