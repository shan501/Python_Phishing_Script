# python networking scripts -- 1 -- mailing client
#github testing

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

with open ( "password.txt",'r') as file : 
    password = file.read()

with open ( 'email_list.txt','r') as file : 
    email = file.read()

with open ('text.txt','r') as file :
    text=file.read()


file = 'index.png'
image = open (file,'rb')
p=MIMEBase('application','octet-stream')
p.set_payload(image.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment ; filename = {file}')

server = smtplib.SMTP('smtp.gmail.com',25)
server.starttls()
server.ehlo()
server.login('quickpython123@gmail.com',password)

msg=MIMEMultipart()
msg['From'] = 'Bank of America'
msg['To'] = email 
msg['Subject'] = 'Unclaimed stimulus'
msg.attach(p)
msg.attach(MIMEText(text,'plain'))

message = msg.as_string()

server.sendmail('quickpython123',email.split(','),msg.as_string())



