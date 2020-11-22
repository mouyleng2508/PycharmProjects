import os
def delete_file(file):
    file = os.path.exists()
    while True:
        inputs = input(f"Are you sure you want to delete {file}?[Y/N]")
        if inputs != "Y" or inputs != "y" or inputs != "N" or inputs != "n":
            return "Invalid Option"
            continue
        else:
            if os.remove(file):
                return 1
            else:
                return 0

print(delete_file("demofile2.txt"))
