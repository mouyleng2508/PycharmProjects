import re
def regex_alpha(string):
    reg = re.sub("[a-zA-Z0-9]", '', string)
    if len(reg) == 0:
        return True
    else:
        return False

print(regex_alpha("abc123"))
print(regex_alpha("AAA123"))
print(regex_alpha("abc123!"))
print(regex_alpha(""))
