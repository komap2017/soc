from email.mime.text import MIMEText


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    message = MIMEText('\n {}'.format(message).encode('utf-8'), _charset='utf-8')
    print(message)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")


if __name__ == '__main__':
    send_email('nikitosgrigorenko2011@gmail.com', 'Zcegthybrbnf2011', 'nikitosgrigorenko2011@gmail.com', 'test', 'testing')