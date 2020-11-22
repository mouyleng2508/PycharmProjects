def milli_to_hours(milliseconds):
    return round((milliseconds / (1000 * 60 * 60)) % 24)

a = milli_to_hours(10800000)
print(a)
