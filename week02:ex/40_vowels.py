def vowels(string):
    lowers = ""
    upper = ""
    for x in string:
        if x in vowel:
            lowers += x
        else:
            upper += x

    vowel_lower = lowers.lower()
    count = len(vowel_lower)
    concatenate_upper = upper.replace(" ", "").upper()
    return f"{count} \n{vowel_lower} \n{concatenate_upper}"

vowel = 'aAeEiIOoUu'
a = vowels("what is that ?")
print(a)
