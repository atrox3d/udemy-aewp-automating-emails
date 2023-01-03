import yagmail

from secret import google_app_password as gap


sender = gap.USER
receiver = input('mail recipient: ')
subject = 'test from yagmail'
body = """
This is a test message from yagmail
"""
attachment = 'requirements.txt'

yag = yagmail.SMTP(user=gap.USER, password=gap.PASSWORD)
yag.send(to=receiver, subject=subject, contents=body, attachments=attachment)
print(f'email sent to {receiver}')
