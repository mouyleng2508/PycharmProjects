def slice_list(lists, slice_number):
    return lists[slice_number:-slice_number]

slices = slice_list([50, 10, 62, 32, 64, 78, 90], 2)
print(slices)
