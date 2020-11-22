def bin_to_dex(binary):
    y = 0
    decimal = 0
    binary = str(binary)
    for x in binary:
        if int(x) in bin:
            print(end='')
        else:
            return "This is not a binary number"

    while int(binary) > 0:
        n = int(binary) % 10
        binary = int(binary) // 10
        decimal = decimal + (2 ** y) * n
        y += 1
    print(decimal, end='')

    return ''

bin = [0, 1]
print(bin_to_dex(110011))
