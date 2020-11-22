def matrix_addition(matrix1, matrix2):
    for x in range(len(matrix1)):
        for y in range(len(matrix1[0])):
            results[x][y] = matrix1[x][y] + matrix2[x][y]

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
           [5, 0, 9, 5],
           [9, 19, 60, 8],
           [7, 8, 4, 5]]
matrix2 = [[12, 65, 34, 42],
           [10, 5, 89, 45],
           [11, 21, 63, 78],
           [87, 78, 54, 65]]
results = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

print(matrix_addition(matrix1, matrix2))
