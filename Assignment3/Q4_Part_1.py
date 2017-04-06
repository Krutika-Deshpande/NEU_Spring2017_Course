
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
from pandas import DataFrame


# In[103]:

frame = pd.read_csv('\\Users\\kruts\\DataAnalysis4Python_Spring17\\Assignments\\Assignment 3\\Data\\movies_awards.csv')


# In[104]:

#Creating a dataframe with only Awards
df= DataFrame(frame, columns = ['Awards'])
#Eliminating columns with value 'NaN'
df = df.dropna() 


# In[110]:

# Fetching the wins and nominations from the awards column
df['Awards_won']= df['Awards'].str.extract('(\d+) win',expand = True)
df['Awards_nominated']  = df['Awards'].str.extract('(\d+) nomination',expand = True)
df['Prime_Awards_won']  = df['Awards'].str.extract('Won (\d+) Primetime',expand = True)
df['Prime_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) PrimeTime',expand = True)
df['Bafta_Awards_won']  = df['Awards'].str.extract('Won (\d+) BAFTA',expand = True)
df['Bafta_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) BAFTA',expand = True)
df['Oscar_Awards_won']  = df['Awards'].str.extract('Won (\d+) Oscar',expand = True)
df['Oscar_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) Oscar',expand = True)
df['GoldenGlobe_Awards_won']  = df['Awards'].str.extract('Won (\d+) Golden Globe',expand = True)
df['GoldenGlobe_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) Golden Globe',expand = True)


# In[111]:

df = df.fillna(0)
df


# In[115]:

# Converting objects to int
df['Awards_won'] = df['Awards_won'].astype(str).astype(int)
df['Awards_nominated'] =df['Awards_nominated'].astype(str).astype(int) 
df['Prime_Awards_won'] = df['Prime_Awards_won'].astype(str).astype(int)
df['Prime_Awards_nominated']=df['Prime_Awards_nominated'].astype(str).astype(int)
df['Bafta_Awards_won']=df['Bafta_Awards_won'].astype(str).astype(int) 
df['Bafta_Awards_nominated']=df['Bafta_Awards_nominated'].astype(str).astype(int)
df['Oscar_Awards_won']=df['Oscar_Awards_won'].astype(str).astype(int) 
df['Oscar_Awards_nominated']=df['Oscar_Awards_nominated'].astype(str).astype(int)
df['GoldenGlobe_Awards_won']=df['GoldenGlobe_Awards_won'].astype(str).astype(int)
df['GoldenGlobe_Awards_nominated']=df['GoldenGlobe_Awards_nominated'].astype(str).astype(int)


# In[79]:

df['Awards_won'] = df['Awards_won']+df['Prime_Awards_won']+df['Bafta_Awards_won']+df['Oscar_Awards_won']+df['GoldenGlobe_Awards_won']
df['Awards_nominated']=df['Awards_nominated']+df['Prime_Awards_nominated']+df['Bafta_Awards_nominated']+df['Oscar_Awards_nominated']+df['GoldenGlobe_Awards_nominated']


# In[113]:

print(df.head())


# In[114]:

df.to_csv('Q4_Part_1.csv') #Generating csv for the above result

