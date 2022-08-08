from optparse import Values
from weakref import ReferenceType
#import openpyxl
import pandas as pd

files=('Z:\shared\WEEK FILES\Desmond Silkwood\SuperBill_Desmond_July-August.xlsm', \
    'Z:\shared\WEEK FILES\Jaivardhan Sankhala\SuperBill_Jaivardhan_July-August.xlsm', \
    'Z:\shared\WEEK FILES\James Frodsham\SuperBill_James_July-August.xlsm', \
    'Z:\shared\WEEK FILES\Lucas Abiy\SuperBill_Lucas_July-August.xlsm', \
    'Z:\shared\WEEK FILES\Maria Orlando\SuperBill_Maria_July-August.xlsm', \
    'Z:\shared\WEEK FILES\Srimayee Yada\SuperBill_Srimayee_July-August.xlsm' )
provider=[]
clients=[]
df=pd.read_excel(files[0],sheet_name='summary',header=None,usecols='A:N')
row=df.loc[1:1]
provider=df.loc[1:1].values.flatten().tolist()
provider[0]='Names'
#print(provider)
#print(df.head(4))
#provider_hours=[]
for file in files:
    df=pd.read_excel(file,sheet_name='summary',header=None,usecols='A:N')
    client=df.loc[14:14].values.flatten().tolist()
    clients.append(client)
df2=pd.DataFrame(clients) 
print (df2)   
# for client in clients:    
#     print(client)
for j in range(2,14):
    hours=0.
    for i in range(len(clients)):
        hours +=clients[i][j]
    if (provider[j] ==' ') or (hours==0.0) :
        continue 
    else:   
        print((provider[j]+"\t"+f"{hours:.2f}").expandtabs(15))
        
            

