string = input("Input a string: ")

first = string[:len(string) // 2]
second = string[len(string) // 2:]

print(["The string is empty.",
        first[::-1]+second]
        [len(string) > 0])
