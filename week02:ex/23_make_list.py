import json
def make_list(a, b, c):
    list = []
    new_list = list.append(a)
    new_list = list.append(b)
    new_list = list.append(c)
    return json.dumps(list)

a = make_list(21, "Hello", 45)
print(a)
