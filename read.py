import imaplib
import base64
import os
import email

email_user = 'luisrios.lar@gmail.com'
email_pass = '939030e99'
mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
mail.login(email_user, email_pass)
mail.select('Inbox')
type, data = mail.search(None, '(SUBJECT "EI")')
idlist = data[0].split()

for num in idlist:
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    print('From: '+email_message['from'])
    print('body: '+email_message['to'])