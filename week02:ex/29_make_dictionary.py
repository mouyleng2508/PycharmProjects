def make_dictionary(list_integers, tuple_strings):
    dic = dict(zip(list_integers, tuple_strings))
    return dic

dictionary = make_dictionary([50,  10, 62], ("Borey", "Thirak", "Dane"))
print(dictionary)

