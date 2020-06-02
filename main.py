from email.parser import BytesParser, Parser
from smtplib import *
from email.mime.text import MIMEText
import poplib
import argparse
import email

m = poplib.POP3_SSL('pop.gmail.com',995)
m.user('luisrios.lar@gmail.com')
m.pass_('939030e99')
numero = len(m.list()[1])
la = []
print("Número total de mensajes: "+str(numero))
for i in range (10):
    print ("Mensaje numero "+str(i+1))
    print ("--------------------")
    response, headerLines, bytes = m.retr(i+1)
mensaje=''.join(str(headerLines))
p = Parser()
email = p.parsestr(mensaje)
#email = p.parsestr(mensaje)
print ("From: "+email["From"])
print ("To: "+email["To"])
print ("Subject: "+email["Subject"])