def bin_to_oct(binary):
    binary = str(binary)
    for x in binary:
        if int(x) in bin:
            print(end='')
        else:
            return "This is not binary number"
            exit()

    decimal = int(binary, 2)
    octal = oct(decimal)[2:].upper()
    return octal.lower()

bin = [0, 1]
print(bin_to_oct(11001101))
