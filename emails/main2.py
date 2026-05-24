import smtplib
import datetime as dt
import random

EMAIL = ""
PASSWORD = "" 
SMTP_SERVER = ''
SMTP_PORT = 587
DESTINATION = ''

TODAY_WEEKDAY = dt.datetime.now().weekday()
DAY_TO_SEND = 0 # monday = 0

if TODAY_WEEKDAY == DAY_TO_SEND:
   with open('quotes.txt') as file:
      quotes = file.readlines()
      quote = random.choice(quotes).strip().encode('ascii', 'ignore')
      with smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT) as connection:
         connection.starttls()
         connection.login(user=EMAIL, password=PASSWORD)

         message = f"Subject:Your Monday Quote\n\n{quote.decode('utf-8', 'ignore')}"
         connection.sendmail(from_addr=EMAIL, to_addrs=DESTINATION, msg=message)
         print('email sent')