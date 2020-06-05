import pandas as pd

class Analyze:
    
    def __init__(self):
        OrderHeader = []
        self.document = pd.read_excel('C:/Users/luisr/Desktop/Documentos importantes/IntegrationErrors/Documents/errors.xlsx')
        orders = len(self.document['Document'])
        print("Orders count: "+str(orders))
        #print(" ".split(self.document['Document'][0]))
        for order in range(orders):
            OrderHeader.append((self.document['Document'][order].split())[-1])
        print(OrderHeader)