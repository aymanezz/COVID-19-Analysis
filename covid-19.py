

import pandas as pd
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as olt


data = pd.read_csv('covid19.csv')



grouped = data.groupby("Date",sort = False)['State/UnionTerritory','ConfirmedIndianNational','ConfirmedForeignNational','Cured','Deaths'].sum().reset_index()
grouped


grouped['sum'] = grouped.iloc[:,1:].sum(axis=1)
grouped



grouped.plot(kind = 'line',x = 'Date',y='sum')



specific_dayes = grouped.iloc[34:,:]
specific_dayes


list_ = specific_dayes.values.tolist()
list_

list2 =[]

for i in range(17):
    list2.append( (list_[i+1][5]-list_[i][5])/list_[i+1][5])
   

#list2
r = sum(list2)/len(list2)

P_o = 31
t = 26
P_t = P_o*(math.exp(r*t))
print(P_t)

