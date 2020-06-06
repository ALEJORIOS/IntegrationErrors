import imaplib
import email
import DownloadAttachments
import analyzeDocuments
import pandas

server = "imap.gmail.com"
user = "luisrios.lar@gmail.com"
password = "939030e99"
outputdir = "C:/Users/luisr/Desktop/Documentos importantes/IntegrationErrors/Documents"

connection = [server,user,password,outputdir]
DownloadAttachments.FetchEmail(connection)
Document = analyzeDocuments.Organize()
Document.analyze()
Document.callCreators()
Document.getMail()