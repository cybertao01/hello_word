#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
my_sender='****@****.com'   # sender's account
my_pass = '*****'           # sender's password
my_user='*****@**.com'      # receiver's address 
def mail():
    ret=True
    try:
        msg=MIMEText('Email Content','plain','utf-8')
        msg['From']=formataddr(["Cybertao",my_sender])  # sender's name
        msg['To']=formataddr(["Cybertao",my_user])      # receiver's name
        msg['Subject']="Python sending Email"           # Subject
 
        server=smtplib.SMTP_SSL("smtp.***.com", 994)  # SMTP Server， port 994
        server.login(my_sender, my_pass)  
        server.sendmail(my_sender,[my_user,],msg.as_string()) 
        server.quit()  
    except Exception:  
        ret=False
    return ret
 
ret=mail()
if ret:
    print("OK!")
else:
    print("Error!")