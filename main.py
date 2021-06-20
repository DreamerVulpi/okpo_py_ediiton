import numpy as np
import random

if __name__ == '__main__':
    # Запись размерности трехмерного массива
    N = int(input("Write N: "))
    M = int(input("Write M: "))
    L = int(input("Write L: "))
    print("{0} {1} {2}".format(N, M, L))
    A = np.zeros((N, M, L))

    # Генерация случайных чисел в диапазоне -20 до 20
    x = 0
    y = 0
    z = 0
    for x in range(0, N):
        for y in range(0, M):
            for z in range(0, L):
                A[x][y][z] = random.randint(-20, 20)

    # Печать сгенерированного массива
    for x in range(0, N):
        for y in range(0, M):
            for z in range(0, L):
                print("A[{0}][{1}][{2}] == {3}".format(x, y, z, A[x][y][z]))

    maxX = -21
    maxY = -21
    maxZ = -21

    # Прохождение по оси X
    for x in range(0, N):
        sum = 0
        print("SumPlaneX = {0}".format(sum), end='')
        for y in range(0, M):
            for z in range(0, L):
                sum += A[x][y][z]
                print(" + {0}".format(A[x][y][z]), end='')
        if sum > maxX:
            print(" = {0}".format(sum))
            print("SumPlaneX > maxX")
            print("{0} > {1}".format(sum, maxX))
            maxX = sum
            print("CoordinateDotOnPlaneX [{0}][{1}][{2}]\n".format(x, 0, 0))
        print("\n")
    print("maxX = {0}\n".format(maxX))

    # Прохождение по оси Y
    for y in range(0, M):
        sum = 0
        print("SumPlaneY = {0}".format(sum), end='')
        for x in range(0, N):
            for z in range(0, L):
                sum += A[x][y][z]
                print(" + {0}".format(A[x][y][z]), end='')
        if sum > maxY:
            print(" = {0}".format(sum))
            print("SumPlaneY > maxY")
            print("{0} > {1}".format(sum, maxY))
            maxY = sum
            print("CoordinateDotOnPlaneX [{0}][{1}][{2}]\n".format(0, y, 0))
        print("\n")
    print("maxY = {0}\n".format(maxY))

    # Прохождение по оси Z
    for z in range(0, L):
        sum = 0
        print("SumPlaneZ = {0}".format(sum), end='')
        for x in range(0, N):
            for y in range(0, M):
                sum += A[x][y][z]
                print(" + {0}".format(A[x][y][z]), end='')
        if sum > maxZ:
            print(" = {0}".format(sum))
            print("SumPlaneX > maxZ")
            print("{0} > {1}".format(sum, maxZ))
            maxZ = sum
            print("CoordinateDotOnPlaneX [{0}][{1}][{2}]\n".format(0, 0, z))
        print("\n")
    print("maxZ = {0}\n".format(maxZ))

    Max = max(maxX, max(maxY, maxZ))
    print("Maximum value [{0}, {1}, {2}] => {3}".format(maxX, maxY, maxZ, Max))
