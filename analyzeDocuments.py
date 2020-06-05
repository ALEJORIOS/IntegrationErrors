import pandas as pd

class Organize:
    
    def __init__(self):
        self.catched = []
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
        for order in range(self.orders):
            for error in range(len(self.Response[order])):
                #if str(self.Response[order][error]).find("t") != -1:
                if "Enter a tax code" in self.Response[order][error]:
                    self.catched.append(self.OrderHeader[order])
            
        print(self.catched)
