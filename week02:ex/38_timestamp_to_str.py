import datetime
def timestamp_to_str(timestamp):
    if type(timestamp) == str or type(timestamp) == int:
        t_Stamp = datetime.datetime.fromtimestamp(timestamp)
        return t_Stamp.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return "Your timestamp is not valid."
a = timestamp_to_str(1623646780)
print(a)
