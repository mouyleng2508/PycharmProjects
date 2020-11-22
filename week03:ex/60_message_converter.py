import codecs
def message_converter(string):
    converted = ''
    for i in string:
        converted += hex(ord(i))[2:].upper()
    return converted

print(message_converter("Hello"))
