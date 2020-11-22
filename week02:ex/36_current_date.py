import datetime
def current_date():
    return datetime.date.today().strftime('%Y-%m-%d')

a = current_date()
print(a)
