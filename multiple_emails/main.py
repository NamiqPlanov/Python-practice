import smtplib as s
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('namiqplanov44@gmail.com','245planov123')
subject = "test msg"
body = 'Hello friend'
msg = "subject:{}\n\n{}".format(subject,body)
listadd = ['planovnamiq27@gmail.com','ayxanplanov@gmail.com']
ob.sendmail('namiqplanov44@gmail.com',listadd,msg)
print('send email')
ob.quit()