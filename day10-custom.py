import smtplib
import os

host = "smtp.gmail.com"
port = 587
username = "xxxx@gmail.com"
password = "xxxxx"
from_email = username
to_list = ["a09087680373@gmail.com"]


"""
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

email_conn = SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
try:
    email_conn.login(username, password)
    email_conn.sendmail(from_email,to_list,"This is another me.")
except:
    print("error occured")

email_conn.quit()

"""

path = os.path.dirname(__file__)

upper_path = os.path.dirname(os.path.dirname(__file__))
print(upper_path)

apple = "good"

class Buy():
    def buy_it(input):
        input_str = str(input)
        ans = apple + input_str

        return ans

print (Buy.buy_it(" stuff"))
