import json
def fun_split(str):
    split = str.split()
    lists = json.dumps(split)
    if len(str) == 0:
        return lists
    else:
        return lists
a = fun_split("Hello world welcome to Python")
print(a)
