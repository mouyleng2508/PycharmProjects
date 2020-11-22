def list_merge_sort(list):
    if len(list) < 2:
        return list
    result = []
    mid = int(len(list) / 2)
    y = list_merge_sort(list[:mid])
    z = list_merge_sort(list[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    return result

a = list_merge_sort([50, 75, 60, 55, 60, 98, 50, 23])
print(a)
