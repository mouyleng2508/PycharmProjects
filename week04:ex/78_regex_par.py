import re
def regex_par(string):
    no_par = re.sub("\\(.*?\\)", "", string)
    return no_par

print(regex_par("(hello) Welcome to KIT (Kirirom Institute of Technology)!"))
print(regex_par("((not ok)) )ok( )))(not_ok)(((ok"))
