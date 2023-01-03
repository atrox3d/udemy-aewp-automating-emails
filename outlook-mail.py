import smtplib
import os

from secret import outlook_mail as om
from secret import mail_recipients as mr

sender = om.USER
receiver = mr.GMAIL
subject = 'Hello hello'
body= """
hello from outlook
"""
message = f"Subject: {subject}\n{body}"

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(om.USER, om.PASSWORD)
server.sendmail(om.USER, mr.GMAIL, message)
server.quit()
