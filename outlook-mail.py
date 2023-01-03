import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from secret import outlook_mail as om
from secret import mail_recipients as mr

sender = om.USER
receiver = mr.GMAIL
subject = 'Hello hello'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'html message'

body = """
<h1>hello from outlook</h1>
"""
mimetext = MIMEText(body, 'html')
message.attach(mimetext)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(om.USER, om.PASSWORD)
print(message.as_string())
server.sendmail(om.USER, mr.GMAIL, message.as_string())
server.quit()
