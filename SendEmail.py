from email.message import EmailMessage
import smtplib
from datetime import datetime
from XCHtoUSD import XCHtoUSD

f = open("Gmail.apikey", "r")
lines = f.readlines()
f.close()
gMailUserName = lines[0].strip()
passWord = lines[1].strip()


def send_email(recipient, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = gMailUserName
    msg["To"] = recipient
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(gMailUserName, passWord)
    server.send_message(msg)
    server.quit()


converter = XCHtoUSD()
xchPrice = converter.getUSDtoRUB()
date = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
body = "XCH Price as of " + date + " is: " + str(xchPrice) + " USD"
print(body)

f = open("EmailList.lst","r")
emails = f.readlines()
f.close()
for email in emails:
    email.strip()
    send_email(email, subject="Today's XCH Price", body=body)
    print("Sent Email to: " + email)
