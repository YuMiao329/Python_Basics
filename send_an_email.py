import smtplib

# simple mail transport library

sender = "yumiao0557@gmail.com"
receiver = "yum068@ucsd.edu"
password = "My3970151!"
subject = "Python email test"
body = "I wrote an email! :D"

# triple quote could separate multiple line of text
message = f"""From: Snoop Dogg{sender}
To: Nicholas Python Test{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
# transport layer security

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")
