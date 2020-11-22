def search_in_tuple(tuples, search_num):
    if search_num in tuples:
        index = tuples.index(search_num)
        return f"Element found at Index: {index}"
    else:
        return "Element not found in the tuple"

a = search_in_tuple((20, 15, 10, 30), 10)
print(a)
