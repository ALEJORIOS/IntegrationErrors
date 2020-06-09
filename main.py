import imaplib
import email
import DownloadAttachments
import analyzeDocuments
import sendMails
import pandas

server = "imap.gmail.com"
user = "luisrios.lar@gmail.com"
password = "939030e99"
outputdir = "C:/Users/luisr/Desktop/Documentos importantes/IntegrationErrors/Documents"

connection = [server,user,password,outputdir]
DownloadAttachments.FetchEmail(connection)
Document = analyzeDocuments.Organize()
orders, errors = Document.analyze()
Document.callCreators()
destin = Document.getMail()
sendMails.prepare([user,password,destin], orders, errors)
