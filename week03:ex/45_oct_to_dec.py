def oct_to_dec(octal):
    decimal = 0
    base = 1
    octal = str(octal)
    for x in octal:
        if int(x) in oct:
            print(end='')
        else:
            return "This is not an octal number"
            exit()

    while octal:
        last = int(octal) % 10
        octal = int(int(octal) / 10)

        decimal += last * base
        base = base * 8

    return decimal

oct = [0, 1, 2, 3, 4, 5, 6, 7]
print(oct_to_dec(750))
