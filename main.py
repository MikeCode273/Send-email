# import smtplib
# my_email = "qwamefenteng@gamial.com"
# my_password = "abcd@1234"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#  connection.starttls()
#  connection.login(user=my_email,password=my_password)
#
#  connection.sendmail(from_addr=my_email, to_addrs="mickeyfent3@gmail.com", msg="Hello")
#


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
hour = now.hour
day_of_week = now.weekday()

print(day_of_week,month,year, hour)

date_of_birth = dt.datetime(year= 2004, month= 3, day= 27, hour= 12)

print(date_of_birth)