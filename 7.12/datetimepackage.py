import datetime
def print_next_day():
    print(datetime.date.today()+datetime.timedelta(1))
print_next_day()