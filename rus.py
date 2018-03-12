#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Send email via smtp_host."""
import smtplib
from email.mime.text import MIMEText
from email.header    import Header


def send_mail(message, login='nikitosgrigorenko2011@gmail.com', password='Zcegthybrbnf2011'):
    ####smtp_host = 'smtp.live.com'        # microsoft
    smtp_host = 'smtp.gmail.com'       # google
    ####smtp_host = 'smtp.mail.yahoo.com'  # yahoo
    #login = 'nikitosgrigorenko2011@gmail.com'
    #password = 'Zcegthybrbnf2011'
    recipients_emails = [login]
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = Header('soc', 'utf-8')
    msg['From'] = login
    msg['To'] = ", ".join(recipients_emails)

    s = smtplib.SMTP(smtp_host, 587, timeout=10)
    #s.set_debuglevel(1)
    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg['From'], recipients_emails, msg.as_string())
    finally:
        s.quit()


if __name__ == '__main__':
    send_mail('Тестирование')