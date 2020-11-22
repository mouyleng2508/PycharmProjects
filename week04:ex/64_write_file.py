def write_file(filename, content):
    while True:
        inputs = input("Are you sure you want to replace<FILENAME>[Y/N] ")
        if input == 'Y' or input == 'y':
            f = open(filename, "a")
            f.write(content)
            f.close()
            return 1
        elif input == 'N' or input == 'n':
            return 0
        else:
            return "Invalid Option"
print(write_file("name.txt", "There're so many names in this file!"))
