string = input("Input a string")
print(["The string is empty.", string.upper()][len(string) > 0])