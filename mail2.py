#!/usr/bin/env python3
#coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'abc@126.com';
#receivers = '2276939579@qq.com';
receivers = '227699579@qq.com';

message = """From: From Michael Yu <le_wan@126.com>
To: To Finch(By le wan 2016/03/22/12:53) 227699579@qq.com
Subject: SMTP e-mail for a test. This email write by Python. This is a test e-mail message.
"""

for i in range(3):
    try:
        smtpObj = smtplib.SMTP('smtp.126.com')
        smtpObj.login("abc@126.com", "123")
        smtpObj.sendmail(sender, receivers, message)
        print "Successfully sent email"
    except smtplib.SMTPException:
        print "Error: unable to send email"
