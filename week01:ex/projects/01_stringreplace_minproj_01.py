# def start():
#     paragraph_string = input("Please input a paragraph: \n")
#     search_string = input("Please input a Search String: \n")
#     counts = paragraph_string.count(search_string.islower())
#     print(f"There are {counts} occurences.")
#
# start()

# while True:
#     choice1 = str(input("Do you want to replace the text[Y/N]?\n"))
#     if choice1 == 'Y' or 'y' or 'N' or 'n':
#         if choice1 == 'N' or 'n':
#             choice2 = str(input("Oh! you don't like to replace, Do you want to check again [Y/n]?"))
#             if choice2 == 'Y' or 'y':
#                 start()
#             else:
#                 exit()
#         elif choice1 == 'Y' or 'y':
#
#     else:
#         print('"Please give proper input"')

# import re
# text = input("Text: ")
# search = re.findall("[a-zA-Z]", text)
# print(search)

import re
paragraph_string = input("Please input a paragraph: \n")
search_string = input("Please input a Search String: \n")
counts = paragraph_string.count(search_string)

#counts = re.findall('[a-zA-Z]\S',paragraph_string)
print(f"There are {counts} occurences.")