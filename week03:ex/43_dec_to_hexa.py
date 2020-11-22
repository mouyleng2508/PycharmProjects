# First:
# def dec_to_hex(decimal):
#     return hex(decimal)[2:].upper()
#
# print(dec_to_hex(1500))


# Second:
# def dec_to_hex(decimal):
#     hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
#     reverse = ""
#     while decimal > 0:
#         remainder = decimal % 16
#         decimal -= remainder
#         decimal //= 16
#         reverse += str(hexa[remainder])
#
#     print(reverse[::-1].upper())
#
#     return ''
# print(dec_to_hex(1500))
