def hex_to_dec(hexa):
    for x in hexa:
        if x in hexaDec:
            print(end='')
        else:
            return "This is not a hexa-decimal number"
            exit()

    decimal = int(hexa, 16)
    return decimal

hexaDec = 'ABCDEFabcdef123456789'
print(hex_to_dec("BA1"))
