sum = 0
while True:
    inputs = input("Input a number: ")

    if inputs.isnumeric():
        sum += int(inputs)
    elif inputs == 'stop':
        print(f"Sum = {sum}")
        break
    else:
        print("The input must be a valid number!")




