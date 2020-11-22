# First:
# def dec_to_oct(decimal):
#     return oct(decimal)[2:]
#
# print(dec_to_oct(98))


# Second:
# def dec_to_oct(decimal):
#     octal = [0] *100
#     x = 0
#     while decimal != 0:
#         octal[x] = decimal % 8
#         decimal = int(decimal/8)
#         x += 1
#
#     for y in range(x-1, -1, -1):
#         print(octal[y], end='')
#
#     return ''
# print(dec_to_oct(98))
