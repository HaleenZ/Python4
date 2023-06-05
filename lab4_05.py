import datetime

start_date = datetime.datetime.strptime('28/02/2000', '%d/%m/%Y').date()
end_date = datetime.datetime.strptime('28/02/2001', '%d/%m/%Y').date()

days_between = (end_date - start_date).days

print("Days between the two dates:", days_between)
