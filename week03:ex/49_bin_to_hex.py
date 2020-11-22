def bin_to_hex(binary):
    binary = str(binary)
    for x in binary:
        if int(x) in bin:
            print(end='')
        else:
            return "This is not a binary number"
            exit()

    decimal = int(binary, 2)
    hexa = hex(decimal)[2:].upper()
    return hexa.lower()

bin = [0, 1]
print(bin_to_hex(11001101))
