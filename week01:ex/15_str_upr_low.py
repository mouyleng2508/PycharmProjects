string = input("Enter a string: ")
print(["The String is empty.",
       string[:len(string) // 2].upper() +
       string[len(string) // 2:].lower()]
      [len(string) > 0])
