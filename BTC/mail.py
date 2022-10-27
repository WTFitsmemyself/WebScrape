import smtplib
gmail_user = 'myrad.noori@gmail.com'
gmail_password = 'znfWAwuA3AEnLG5w'
sent_from = gmail_user
to = ['itshosyn@gmail.com']
subject = 'Hello From Python'
body = 'This is a message from Python'
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print("Email sent successfully!")
except Exception as ex:
    print("Something went wrong….", ex)
