from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'namiqplanov44@gmail.com'
email_password = ''
email_receiver = 'ayxanplanov@gmail.com'
subject = 'sir hemse sirdi '
body = 'hello bro how are you?'
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em['Body'] = body
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
