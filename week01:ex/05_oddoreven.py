num = input("Input a number:\n")
if num.isnumeric():
    if int(num) %2 ==0:
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Not a valid Number")