import imaplib
import email

class FetchEmail:

    def __init__(self,connection):
        self.server = connection[0]
        self.user = connection[1]
        self.password = connection[2]
        self.outputdir = connection[3]
        self.m = imaplib.IMAP4_SSL(self.server)
        self.m.login(self.user, self.password)
        self.m.select('Inbox')
        
        typ, data = self.m.search(None,  '(SUBJECT "EI")')
        idlist = data[0].split()
        last = idlist[-1]
        #Download attachments
        resp, data = self.m.fetch(last, "(BODY.PEEK[])")
        email_body = data[0][1].decode()
        
        mail = email.message_from_string(email_body)
        if mail.get_content_maintype() != 'multipart':
            return
        for part in mail.walk():
            if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
                open(self.outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))
