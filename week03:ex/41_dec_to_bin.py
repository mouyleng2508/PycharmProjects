# First:
# def dec_to_bin(decimal):
#     return bin(decimal)[2:]
#
# print(dec_to_bin(50))


# Second:
def dec_to_bin(decimal):
    binary = []
    while decimal > 0:
        value = int(decimal % 2)
        decimal = int(decimal / 2)
        binary.append(value)

    binary.reverse()
    for x in binary:
        print(x, end='')
    return ''
print(dec_to_bin(50))
