def list_count(lists):
   new_list = ""
   total = 0
   for x in list(set(lists)):
       new_list += str(x) + " " + str(lists.count(x)) + ","
       total += lists.count(x)
   return f"{new_list}\nTOTAL: {total}"

a = list_count(["a", "b", "b", "c", "c", "c", "c", "d", "d", "e", "e", "e"])
print(a)
