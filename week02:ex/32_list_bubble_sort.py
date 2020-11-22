def list_bubble_sort(list):
    for x in range(len(list) - 1):
        for y in range(0, len(list) - 1):
            if list[y] > list[y+1]:
                tmp = list[y]
                list[y] = list[y+1]
                list[y+1] = tmp
    return list
a = list_bubble_sort([50, 75, 60, 55, 98, 23])
print(a)
