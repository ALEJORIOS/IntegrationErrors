from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys

class prepare:
    #autentication[0] -> origin
    #autentication[1] -> password
    #autentication[2] -> destin

    def __init__(self, autentication, orders, errors):

        self.documents = []
        self.text = []
        
        self.password = autentication[1]
        
        self.server = smtplib.SMTP('smtp.gmail.com')
        self.server.starttls()
        

        for mail in range(len(errors)):
            self.documents.append([])
            self.text.append([])

        for mail in range(len(errors)):
            self.documents[mail] = open('C:/Users/luisr/Desktop/Documentos importantes/IntegrationErrors/Body/Body-'+str(mail)+'.txt', encoding="utf-8").read()
        
        for mail in range(len(errors)):
            for line in self.documents[mail]:
                self.text[mail].append(line)
        
        for mail in range(len(errors)):
            self.text[mail] = "".join(self.text[mail])

        for mail in range(len(errors)):
            self.msg = MIMEMultipart()
            self.msg['From'] = autentication[0]
            self.msg['Subject'] = "Proof of your love"
            self.server.login(self.msg['From'], self.password)
            self.message = self.text[mail]
            self.message = self.message + '\n\n'
            for order in range(len(orders[mail])):
                self.message = self.message + orders[mail][order]+'\t'+errors[mail][order]+'\n'
            self.msg.attach(MIMEText(self.message, 'plain'))
            self.msg['To'] = ", ".join(autentication[2][mail])
            
            prepare.send(self, autentication[2][mail])            


    def send(self, destin):
        self.server.sendmail(self.msg['From'], destin, str(self.msg))
        print("////////////////////////////////////////////////")
        print(str(self.msg))
        print("////////////////////////////////////////////////")
        del self.msg
        #self.server.quit()
        print ("successfully sent emails")
