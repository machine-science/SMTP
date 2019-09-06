import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
d = datetime.now().today().strftime("%b%d%y_%H:%M")

s = smtplib.SMTP(host='smtp-mail.outlook.com',port=587)
myAdd = "My email"
s.starttls()
s.login(myAdd, 'MyPWD')

msg = MIMEMultipart()

message = "Hey I have attached a file on "+str(d)

msg['From'] = myAdd
msg['To'] = 'receiverAdd'
msg['Subject'] = 'Test Email'

msg.attach(MIMEText(message, 'plain'))

s.send_message(msg)

del msg

s.quit()
