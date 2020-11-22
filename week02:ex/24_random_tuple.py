import random
def random_tuple(number):
    tuple = ()
    sum = 0
    for x in range(1, number+1):
        rand = random.randint(0, 100)
        print(f"Random number {x}: {rand}")
        tuple = tuple + (rand,)
        sum += rand
    return f"\n{tuple} \n{sum}"
a = random_tuple(5)
print(a)
