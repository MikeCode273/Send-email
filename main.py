import smtplib
my_email = "qwamefenteng@gamial.com"
my_password = "abcd@1234"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user=my_email,password=my_password)

connection.sendmail(from_addr=my_email, to_addrs="mickeyfent3@gmail.com", msg="Hello")
connection.close()