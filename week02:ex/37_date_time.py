from datetime import datetime
def date_time():
    return now.strftime('%Y-%m-%d %H:%M:%S')

now = datetime.now()
a = date_time()
print(a)
