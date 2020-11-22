def xor_operation(hexa1, hexa2):
    decimal1 = int(hexa1, 16)
    decimal2 = int(hexa2, 16)

    binary1 = bin(decimal1)[2:]
    binary2 = bin(decimal2)[2:]

    andOperation = decimal1 ^ decimal2

    print(f"{binary1}\n{binary2}", end='\n\n')
    print(f"  {bin(andOperation)[2:]}", end='')

    return ''

print(xor_operation("33", "3D"))
