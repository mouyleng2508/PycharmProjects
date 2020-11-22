# print("Hello May!")
# print("o----")
# print(" ||||")
# print("*" * 10)

#variable
# price = 10
# rating = 4.9
# name = 'Momo'
# is_published = True
# print(price)

#exercise
# full_name = 'John Smith'
# age = 20
# is_new = True

#get_input
# name = input("What is your name: ")
# print("Hi " +name)

#exercise
# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# print(name + " likes " + color)

#type_conversion
# birth_year = input("Birth year: ")
# age = 2020 - int(birth_year)
# print(age)

#exercise
# weight_lbs = input("Enter your weight in lbs: ")
# weight_kg = int(weight_lbs) * 0.453592
# print(weight_kg)

#string
# course = "Python for Beginners"
# print(course[0])
# print(course[-2])
# print(course[0:5])
# print(course[1:])
# print(course[:6])

#formattd_string
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)

#string_method
# course = "Python for Beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course)
# print(course.find('O'))
# print(course.replace('Beginner', 'Absolute Beginner'))
# print('Python' in course)

#Arithmetic_Operations
# print(10 / 3)  #3.33333333...
# print(10 // 3) #3
# print(10 % 3)  #1
# print(10 ** 3) #1000 (power in Python)

# x = 10
# x += 3  # x = x + 3
# x -+ 3  # x = x - 3

#Operator_Precedence
# x = (10 + 3) * 2 ** 2
# print(x)
# parenthesis
# exponentiation 2 ** 3
# multiplication or division
# addition or substraction

#Maths_Function
# import math
#
# math.ceil(2.9)  #3
# math.floor(2.9) #2
# x = 2.9
# print(round(x)) #3
# print(abs(-2.9)) #2.9

#If_Statement
# is_hot = True
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# else:
#     print("It's a cold day")
#     print("Wear warm clothes")
# print("Enjoy your day")

#exercise
# house_price = 1000000
# is_buyer_good_credit = True
# if is_buyer_good_credit:
#     down_price = 0.1 * house_price
# else:
#     down_price = 0.2 * house_price
# print(f"Down Price: ${down_price}")

#Logical Operator
# has_high_income = True
# has_good_credit = True
# if has_high_income and has_good_credit:
#     print("Eligible for loan")

#Comparison_Operator
# temp = 30
# if temp != 30 :
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

#exercise
# name = "Momo"
# if len(name) <3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50 :
#     print("Name must be a maximum of 50 characters")
# else:
#     print("Name looks good")

#exercise
# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

#While_Loop
# i = 1
# while i <= 5:
#     print("*" *i)
#     i = i +1
# print("Done")

#Guessing_Game
# guess_count = 1
# secret = 9
# while guess_count <=3 :
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret:
#         print("You won")
#         break
# else:
#     print("You failed")

#Car_Game
# commmand = ""
# started = False
# while True:
#     commmand = input("> ").lower()
#     if commmand == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started... Ready to Go")
#     elif commmand == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car Stopped")
#     elif commmand == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif commmand == "quit":
#         break
#     else:
#         print("Sorry I don't understand")

#For_Loop
# for item in 'Python':
#     print(item)

# for item in ['Momo', 'Leng', 'Momoleng']:
#     print(item)

# for i in range(10):
#     print(i)

# for i in range (5,10):
#     print(i)

# for i in range(5,10,2): #2 is the step
#     print(i)

#exercise
# prices = [10, 20, 30]
# sum = 0
# for i in prices:
#     sum += i   #sum = sum + i
# print(f"Total: {sum}")

#Nested_Loop
# for i in range(4):
#     for j in range(3):
#         print(f'({i}, {j})')

#Exercise
# num = [5, 2, 5, 2, 2]
# for i in num:
#     out = ""
#     for j in range(i):
#         out += 'x' #out = out + 'x'
#     print(out)

#List
# names = ['Jelly', 'Pancake', 'Kit Kat', 'M&M', 'Ice-Cream', 'Pizza']
# # print(names[1])
# # print(names[-2])
# # print(names[2:]) #start from index 2

#Exercise Largest Number in a list
# list = [2,4,6,1,9,3,8]
# max = list[0]
# for i in list:
#     if i > max:
#         max = i
# print(max)

#2D_List
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)

#List_Methods
# num = [5, 3, 8, 1, 3, 9]
# num.append(6) #add 6 at the end of the list
# num.insert(1,10) #1 is the index
# num.remove(5) #remove 5 from list
# num.clear() #remove all items
# num.pop() #remove number at the end of the list
# print(num)

# print(num.index(2)) #show the index of element in the list
# print(2 in num) #in Operator return boolean value
# print(num.count(3))

#sort in list
# num.sort() #sort the list in ascending order
# num.reverse() #sort the list in descending order
# print(num)

# num1 = num.copy() #copy the existing list whether it's update or sth no effect
# num.append(10)
# print(num1)

#exercise
# list = [1, 4, 2, 8, 3, 3, 4, 1, 5]
# unique = []
# for i in list:
#     if i not in unique:
#         unique.append(i)
# print(unique)

#tuples
# num = (1, 2, 3)
# print(num[0])

#Unpacking : work both tuple and list
# coordinate = (1, 2, 3)
# x, y, z = coordinate
# print(y)

#Dictionaries : no duplicate key
# customer = {
#     "name" : "Momoleng",
#     "age" : 19,
#     "is_verified" : True
# }
# customer["name"] = "Mouyleng"
# customer["birthdate"] = "Aug 25 2000"
# print(customer.get(("name")))
# print(customer.get(("birthdate")))

#exercise
# phone = input("Phone: ")
# numbers = {
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four"
# }
# out = ""
# for i in phone:
#     out += numbers.get(i, "!") + " "
# print(out)

#Emoji_Convertee :)
# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "☺️",
#     ":(": "🥺",
#     ":3": "😘"
# }
# out = ""
# for word in words:
#     out += emojis.get(word, word) + " "
# print(out)

#Function
# def greet():
#     print("Hello There!")
#     print("Hi :)")
#
#
# print("Start!")
# greet()
# print("Finish!")

#Parameters
def greet(first_name,last_name):
    print(f"Hello {first_name} {last_name}!")
    print("Hi :)")


print("Start!")
greet("Momo", "Leng")

print("Finish!")
