# Sorry sir I use the library function because I don't know any logic
# Same as exercise 52, 53
def binary_addition(num1, num2):
    decimal_sum = num1 + num2
    binary1 = []
    binary2 = []

    while num1 > 0 and num2 > 0:
        value1 = int(num1 % 2)
        value2 = int(num2 % 2)
        num1 = int(num1 / 2)
        num2 = int(num2 / 2)
        binary1.append(value1)
        binary2.append(value2)

    binary1.reverse()
    binary2.reverse()

    print("Num1         ", end=': ')
    for x in binary1:
        print(x, end='')

    print("\nNum2         ", end=': ')
    for y in binary2:
        print(y, end='')

    binary_sum = bin(decimal_sum)[2:]
    print(f"\nSum(Binary)  : {binary_sum}")
    print(f"Sum(Decimal) : {decimal_sum}")

    return ''
binary_addition(60, 50)
