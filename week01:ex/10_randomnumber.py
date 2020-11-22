import random
n = int(input("Input Number:"))
sum = 0
for i in range(0, n):
    randoms = random.randint(2000, 3000)
    if randoms % 2 == 0:
        sum += randoms
print(f"Sum of even random numbers: {sum}")
