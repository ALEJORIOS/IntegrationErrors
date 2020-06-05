import pandas as pd

class Organize:
    
    def __init__(self):
        self.catched = []
        self.users = []
        self.OrderHeader = []
        self.DocumentID = []
        self.Requester = []
        self.Date = []
        self.Response = []
        self.document = pd.read_excel('C:/Users/luisr/Desktop/Documentos importantes/IntegrationErrors/Documents/errors.xlsx')
        self.orders = len(self.document['Document'])
        print("Orders count: "+str(self.orders))
        
        for order in range(self.orders):
            self.OrderHeader.append((self.document['Document'][order].split())[-1])
            self.DocumentID.append(self.document['Document ID'][order])
            self.Requester.append(self.document['Requester'][order])
            self.Date.append(self.document['PO Created Date'][order])
            self.Response.append(self.document['Response Messages'][order].split('\n'))
    
    def analyze(self):
        errors = open('C:/Users/luisr/Desktop/Documentos importantes/IntegrationErrors/Errors.txt','r')
        self.lines = []
        self.errorsCounter = 0
        for line in errors:
            self.lines.append(line.replace('\n',''))
            self.errorsCounter+=1
        for error in range(self.errorsCounter):
            self.catched.append([])
            self.users.append([])
        print(errors.readline())
        for order in range(self.orders):
            for res in range(len(self.Response[order])):
                for error in range(self.errorsCounter):
                    if self.lines[error] in self.Response[order][res]:
                        self.catched[error].append(self.Response[order][res])
                        self.users[error].append('E'+self.OrderHeader[order].zfill(9))
        errors.close()
        print(self.users)

    def callCreators(self):
        self.creators = []
        document = pd.read_excel('C:/Users/luisr/Desktop/Documentos importantes/IntegrationErrors/Documents/requisition.xlsx')
        print(document['PO Number'][0])
        for error in range(self.errorsCounter):
            self.creators.append([])
        for error in range(self.errorsCounter):
            for iterator in range(len(self.users[error])):
                order = self.users[error][iterator]
                add = document['Created By'][self.users[error].index(order)]
                self.creators[error].append(add)
            
        print(self.creators)

    def getMail(self):
        print("Hello wowrld!")
        
