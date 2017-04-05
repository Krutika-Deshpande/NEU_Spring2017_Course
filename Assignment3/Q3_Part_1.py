
# coding: utf-8

# In[2]:

import pandas as pd  #importing the required Libraries
import numpy as np
from pandas import DataFrame


# In[5]:

#Reading data from csv
frame = pd.read_csv('\\Users\\kruts\\DataAnalysis4Python_Spring17\\Assignments\\Assignment 3\\Data\\cricket_matches.csv')
df1= DataFrame(frame)


# In[6]:

# Fetching teams which hosted the game and were also winners
df1 = df1[df1['home']==(df1['winner'])]
# Fetching the score from innings1_ runs or innings2_runs based on the innings win
df1['score'] = df1['innings1_runs'].where(df1['home'] == df1['innings1'], df1['innings2_runs'])
DF_Result = DataFrame()
#Calculating the average score of each team
DF_Result['avg_score'] = df1.groupby('home')['score'].mean()
DF_Result.reset_index().head()


# In[22]:

DF_Result.to_csv('Q3_Part_1.csv') #Generating csv to store the above result

