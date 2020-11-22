import string
alpha1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alpha2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

def encode(strEnc):
     return strEnc.translate(str.maketrans(alpha1, alpha2))
def decode(strEnc):
    return strEnc.translate(str.maketrans(alpha2, alpha1))

def start():
    print("""
Press 1 to encode
Press 2 to decode """)
    choice = int(input())
    if(choice == "1"):
        string = str(input("Enter the string to encode: "))
        print("The decoded text is: "+encode(string))
    else:
        string = str(input("Enter the string to decode: "))
        print("The decoded text is: "+decode(string))

start()

cont = str(input("\nDo you want to continue? [Y/N]\n"))
if (cont == "Y" or "y"):
    start()
else:
    exit()