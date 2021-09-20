# python_networking_scripts

## Python Phishing script 
I created a phishing script that sends out email with images attached 

## Libraries 

```
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

```
These are the libraries needed for this script 

## Importing other files 
I stored the password , the text , image , and list of emails in other files , I will open them useing the open command in python.

```
with open ( "password.txt",'r') as file : 
    password = file.read()

with open ( 'email_list.txt','r') as file : 
    email = file.read()

with open ('text.txt','r') as file :
    text=file.read()


file = 'index.png'
image = open (file,'rb')
```
the image needs addtional code for it to be send

```
p=MIMEBase('application','octet-stream')
p.set_payload(image.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment ; filename = {file}')

```
##Start server 
Now we just need to start up the server 

```
server = smtplib.SMTP('smtp.gmail.com',25)
server.starttls()
server.ehlo()
server.login('quickpython123@gmail.com',password)

```

##Message
After we have successfully login to our account , we would need to add addtional information such as where it is coming from , where it is going , and the subject

```
msg=MIMEMultipart()
msg['From'] = 'Bank of America'
msg['To'] = email 
msg['Subject'] = 'Unclaimed stimulus'
msg.attach(p)
msg.attach(MIMEText(text,'plain'))

```

##Fire Away 
We are ready to send it 

```
server.sendmail('quickpython123',email.split(','),msg.as_string())

```



