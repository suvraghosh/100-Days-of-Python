# To run this code automatically we can use pythonanywhere where we can use cloud to store and run the python code.

import smtplib
from datetime import datetime
import pandas
import random

MY_EMAIL = "ghoshsuvra982@gmail.com"
MY_PASSWORD = "ghoshsuvra7"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

for today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP() as connections:
        connections.starttls()
        connections.login(MY_EMAIL, MY_PASSWORD)
        connections.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
                             msg=f"Subject:Happy Birthday!\n\n{contents}")
