def read_file(Name):
    if Name == "name.txt":
        Names = open(Name, "r")

        return Names.read()

        Names.close()
    else:
        return "Invalid FILENAME"

print(read_file("name.txt"))
