age = int(input("Input your age: "))
if age>0:
    if age >=18:
        print("You are eligible to vote")
    else:
        print("You aren't adult yet... Sorry can't vote")
else:
    print("Age must be a positive digit")