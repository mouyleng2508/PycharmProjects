string = input("Input a text: ")

print(["The string is empty.",
       string[:len(string) // 2] + "\n" + string[len(string) // 2:]]
      [len(string) > 0])




