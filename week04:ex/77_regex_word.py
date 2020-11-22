import re
def regex_word(integer, string):
    if integer < 0 or integer == 0:
        return ""
    else:
        remove_str = re.compile(r'\W*\b\w{1,3}\b\s')
        return remove_str.sub(' ', string)
print(regex_word(3, "My name is Pidor"))
