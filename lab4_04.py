import datetime

date_string = '16/06/2015'
date_object = datetime.datetime.strptime(date_string, '%d/%m/%Y')

week_number = date_object.strftime('%U')

print("Week number:", week_number)
