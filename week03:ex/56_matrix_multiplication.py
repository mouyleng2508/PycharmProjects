def matrix_addition(matrix1, matrix2):
    for x in range(len(matrix1)):
        for y in range(len(matrix2[0])):
            for z in range(len(matrix2)):
                results[x][z] += matrix1[x][y] * matrix2[y][z]

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

matrix1 = [[3, 7, 5],
           [2, 6, 7],
           [4, 3, 2]]
matrix2 = [[6, 5, 4],
           [3, 2, 1],
           [1, 2, 3]]
results = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
print(matrix_addition(matrix1, matrix2))
