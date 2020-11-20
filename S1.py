import smtplib,ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


print("Checking....\n")
with open('./auth.txt','r') as f: #Replce with the file containes your email and password
    mail = f.readlines()[0]
    f.seek(0)
    pas = f.readlines()[1]
    f.close()

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(mail, pas)
server.connect('smtp.gmail.com',465)
server.ehlo()
server.login(mail, pas)

print('Sending The Email.....\n')
mesg = MIMEMultipart()
mesg['From'] = 'The sender Name' #Replace
mesg['To'] = 'The Recipient Name or Email'#Replace
mesg['Subject'] = 'Your Subject'#Replace

with open('./msg.txt','r') as f: #Replace with the file containes your message
    message = f.read()

mesg.attach(MIMEText(message, 'plain'))

fileN = 'goku.png'#Replace
attach = open(fileN, 'rb')

payload = MIMEBase('application','octet-stream')
payload.set_payload(attach.read())

encoders.encode_base64(payload)
payload.add_header('Content-Disposition',f"attachment; filename={fileN}")
mesg.attach(payload)

txt = mesg.as_string()
server.sendmail(mail, 'mike505brown@gmail.com' , txt)

print("Your Email has been sent Successfuly.")
