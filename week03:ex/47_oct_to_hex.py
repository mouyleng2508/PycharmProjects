def oct_to_hex(octal):
    octal = str(octal)
    for x in octal:
        if int(x) in oct:
            print(end='')
        else:
            return "This is not an octal number"
            exit()

    decimal = int(octal, 8)
    hexa = hex(decimal)[2:].upper()
    return hexa

oct = [0, 1, 2, 3, 4, 5, 6, 7]
print(oct_to_hex(1271))
