def dict_values(names):
    for key, value in names.items():
        print(key, ':', *value)
        print("*******")
    return ""
dictionary = dict_values({120: ("Visal","Borey","Sovann"), 130: ("Huot","Mouyleng","Pidor"), 140: ("Nary","Misora","Masaaki")})
print(dictionary)
