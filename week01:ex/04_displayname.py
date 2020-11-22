name = input("Enter your name:")
display = int(input("Enter number of times to display:"))
print(len(name) == 0 and "No name entered" or name)
for i in range(display):
    print(name)
