from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
import datetime
import time


class prepare:
    #autentication[0] -> origin
    #autentication[1] -> password
    #autentication[2] -> destin
    

    def __init__(self, autentication, orders, errors):

        self.documents = []
        self.text = []

        self.now = datetime.datetime.now()
        self.secondsNow = time.time()
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

        prepare.send2sender(self, autentication, orders, errors)


    def send(self, destin):
        self.server.sendmail(self.msg['From'], destin, str(self.msg))
        del self.msg
        #self.server.quit()
        print ("successfully sent emails")

    def send2sender(self, autentication, orders, errors):
        self.sender = 'luisrios.lar@gmail.com'
        for mail in range(len(errors)):
            self.msg = MIMEMultipart()
            self.msg['From'] = autentication[0]
            self.msg['Subject'] = "Errores de integración (Borrador)"
            self.server.login(self.msg['From'], self.password)
            self.message = self.text[mail]
            self.message = self.message + '\n\n'
            for order in range(len(orders[mail])):
                self.message = self.message + orders[mail][order]+'\t'+errors[mail][order]+'\n'
            self.toSender = "Estos son los errores de integración que se enviaran a los usuarios: \n"+"\n".join(autentication[2][mail]) + "\n\nCon el siguiente mensaje:\n\n"+ self.message + "\n\nDe no haber respuesta a este correo, el mensaje será enviado automáticamente a las " +str(self.now.hour)+":"+str(self.now.minute+10)  
            self.msg.attach(MIMEText(self.toSender, 'plain'))
            self.server.sendmail(self.msg['From'],self.sender,str(self.msg))
            print("Mensajes enviados correctamente al remitente")
        del self.msg
        send_time = datetime.datetime(self.now.year,self.now.month,self.now.day,self.now.hour,self.now.minute+10,0)
        time.sleep(send_time.timestamp() - time.time())

        for mail in range(len(errors)):
            self.msg = MIMEMultipart()
            self.msg['From'] = autentication[0]
            self.message = self.text[mail]
            self.message = self.message + '\n\n'
            for order in range(len(orders[mail])):
                self.message = self.message + orders[mail][order]+'\t'+errors[mail][order]+'\n'
            self.msg.attach(MIMEText(self.message, 'plain'))
            self.msg['To'] = ", ".join(autentication[2][mail])
            self.msg['Subject'] = "Error de integración en orden de compra"
            prepare.send(self, autentication[2][mail])

            