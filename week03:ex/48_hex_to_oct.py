def hex_to_oct(hexa):
    for x in hexa:
        if x in hexaDec:
            print(end='')
        else:
            return "This is not a hexa-decimal number"
            exit()

    decimal = int(hexa, 16)
    octal = oct(decimal)[2:]
    return octal

hexaDec = 'ABCDEFabcdef123456789'
print(hex_to_oct("2b9"))
