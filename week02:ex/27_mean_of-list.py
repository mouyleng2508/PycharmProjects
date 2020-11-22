def mean_of_list(lists):
    average = sum(lists) / len(lists)
    return average

avg = mean_of_list([50, 10, 62, 32])
print(round(avg, 2))
