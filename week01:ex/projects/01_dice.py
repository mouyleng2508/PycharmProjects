import random
results = 0
print("Welcome to the dices game!")
while True:
    number = input("Enter the number of dices you want to roll: ")
    if number.isnumeric() and int(number) <= 8:
       if number == '1':
            randoms = random.randint(1, 6)
            results = randoms
            print(f"RESULT: {results}")
            break
       else:
            for j in range(1, int(number)+1):
                randoms = random.randint(1, 6)
                print(f"Dice {j}: {randoms}")
                results += int(randoms)
            print(f"==========\nRESULT: {results}\n==========")
            break
    else:
        print("USAGE: The number must be between 1 and 8")
