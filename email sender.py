import smtplib

to = input("Enter the mail of reciept:\n")
content = input("Type the Content for mail:\n")

def SendEmail(to, content):
    server = smtplib.SMTP("smt.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('sihle.lucingo@younglings.africa','1234')
    server.sendmail('sihle.lucingo@younglings.africa', to, content)
    server.close()
    
SendEmail(to, content)

