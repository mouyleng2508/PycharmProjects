def list_selection_sort(list):
    for x in range(len(list) - 1):
        min = x
        for y in range(x+1, len(list)):
            if list[y] < list[min]:
                min = y

        if min != x:
            tmp = list[x]
            list[x] = list[min]
            list[min] = tmp

    return list
a = list_selection_sort([50, 75, 60, 55, 98, 23])
print(a)
