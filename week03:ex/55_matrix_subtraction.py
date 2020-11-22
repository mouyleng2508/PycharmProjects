# import numpy as np
# def matrix_addition(matrix1, matrix2):
#     result = [[0 for x in range(4)] for y in range(4)]
#
#     for x in range(len(matrix1)):
#         for y in range(len(matrix1[0])):
#             result[x][y] = matrix1[x][y] - matrix2[x][y]
#
#     print("The result matrix is: ")
#     for x in range(4):
#         for y in range(4):
#             print(format(result[x][y], "<3"), end="  ")
#         print("")
#
#     return ''
#
# arr1 = np.array([10, 5, 4, 2, 5, 10, 9, 55, 9, 19, 69, 8, 7, 8, 4, 75])
# matrix1 = arr1.reshape(4, 4)
# print(f"Matrix1:\n\n{matrix1}\n")
#
# arr2 = np.array([12, 65, 34, 2, 1, 5, 8, 45, 7, 21, 63, 8, 0, 78, 4, 65])
# matrix2 = arr2.reshape(4, 4)
# print(f"Matrix2:\n\n{matrix2}\n ")
#
# print(matrix_addition(matrix1, matrix2))


def matrix_addition(matrix1, matrix2):
    for x in range(len(matrix1)):
        for y in range(len(matrix1[0])):
            results[x][y] = matrix1[x][y] - matrix2[x][y]

    print("Matrix 1: \n")
    for x in matrix1:
        print(x)

    print("\nMatrix 2: \n")
    for x in matrix2:
        print(x)

    print("\nThe result matrix is: \n")
    for x in results:
        print(x)

    return ''

matrix1 = [[10, 5, 4, 2],
           [5, 10, 9, 55],
           [9, 19, 69, 8],
           [7, 8, 4, 75]]
matrix2 = [[12, 65, 34, 2],
           [1, 5, 8, 45],
           [7, 21, 63, 8],
           [0, 78, 4, 65]]
results = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

print(matrix_addition(matrix1, matrix2))
