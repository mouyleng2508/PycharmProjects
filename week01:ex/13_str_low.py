string = input("Input a string")
print(["The string is empty.", string.lower()][len(string) > 0])