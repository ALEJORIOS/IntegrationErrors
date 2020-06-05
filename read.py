import imaplib
import email
import DownloadAttachments

server = "imap.gmail.com"
user = "luisrios.lar@gmail.com"
password = "939030e99"
outputdir = "C:/Users/luisr/Desktop/Documentos importantes/IntegrationErrors/Documents"

connection = [server,user,password,outputdir]
DownloadAttachments.FetchEmail(connection)