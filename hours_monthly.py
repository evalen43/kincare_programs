from optparse import Values
from weakref import ReferenceType
#import openpyxl
import pandas as pd
num=input("Input 1 or 2 for Period1 or Period2: ")
if num == 1:
    per1=4
    print("You selected a Summary for Period1")
else: 
    per1=14
    print("You selected a Summary for Period2")

txt_files=open('clients_august.txt',"r")
files=txt_files.read().splitlines()
#print(files)
provider=[]
clients=[]
df=pd.read_excel(files[0],sheet_name='summary',header=None,usecols='A:N')
row=df.loc[1:1]
provider=df.loc[1:1].values.flatten().tolist()
provider[0]='Clients'

for file in files:
    df=pd.read_excel(file,sheet_name='summary',header=None,usecols='A:N')
    client=df.loc[per1:per1].values.flatten().tolist()
    clients.append(client)
df2=pd.DataFrame(data=clients,columns=provider) 

df3=df2.dropna(how='all',axis=1,inplace=False) 
print (df3)
hours_provider=df3.sum(axis=0,numeric_only=True)
#hours_clients=df2.sum(axis=1,numeric_only=True)
pd.options.display.float_format='{:.2f}'.format
#print(provider)

print(hours_provider)
#print(hours_clients)
# for client in clients:    
#     print(client)
# for j in range(2,14):
#     hours=0.
#     for i in range(len(clients)):
#         hours +=clients[i][j]
#     if (provider[j] ==' ') or (hours==0.0) :
#         continue 
#     else:   
#         print((provider[j]+"\t"+f"{hours:.2f}").expandtabs(15))
        
            

