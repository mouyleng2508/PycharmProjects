string = input("Enter a string: ")
print(["The string is empty.", string.swapcase()][len(string) > 0])
