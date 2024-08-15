# import smtplib
# my_email = "qwamefenteng@gamial.com"
# my_password = "abcd@1234"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
#
# connection.login(user=my_email,password=my_password)
#
# connection.sendmail(from_addr=my_email, to_addrs="mickeyfent3@gmail.com", msg="Hello")
# connection.close()


import datetime as dt

now = dt.datetime.now()

month = now.month
year = now.year
hour = now.time()
day = now.weekday()

date_of_birth = dt.datetime(day= 13, month=3, year=2004, hour=12)

print(date_of_birth)