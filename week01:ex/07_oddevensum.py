num = input("Input a number: ")
evenSum = 0
oddSum = 0

if num.isnumeric():
    for i in range(1, int(num)+1):
        if i % 2 == 0:
            evenSum += i
        else:
            oddSum += i
else:
    print("Invalid Input")
print(f"Sum of odd numbers = {oddSum}")
print(f"Sum of even numbers = {evenSum}")