num = input("Input a number: ")
evenSum = 0
oddSum = 0
if num.isnumeric():
    for i in range(1,int(num)+1):
        if i%2 == 0:
            evenSum += i
        else:
            oddSum += i
    averageEven = 2*evenSum / i
    averageOdd = 2*oddSum / i
    print(f"Average of odd numbers = {averageOdd}")
    print(f"Average of even numbers = {averageOdd}")
else:
    print("Invalid Input")
