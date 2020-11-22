def list_unique(list):
    new_list = []
    for x in list:
        if x not in new_list:
            new_list.append(x)
    return new_list

a = list_unique([50, 60, 25, 65, 25, 60])
print(a)
