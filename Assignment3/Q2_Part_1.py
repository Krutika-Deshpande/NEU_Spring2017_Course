
# coding: utf-8

# Q2_PART ONE:
#     
# 1.Use 'employee_compensation' data set.
# 2.Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.
# 3.Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value.
# 4.Display a few rows of the output use df.head().
# 

# In[1]:

import pandas as pd   # importing the required Libraries
from pandas import DataFrame


# In[28]:

#Reading data from the csv file 
df = pd.read_csv('\\Users\\kruts\\DataAnalysis4Python_Spring17\\Assignments\\Assignment 3\\Data\\employee_compensation.csv')


# In[33]:

# Calculating the average compensation for different departments within a organization and sorting them by maximum value.
DF_compensation = df.groupby(['Organization Group', 'Department'])['Total Compensation'].mean().reset_index().sort_values(["Organization Group","Total Compensation"],ascending=[True,False])
DF_compensation.set_index('Organization Group',inplace = True)
print(DF_compensation.head())


# In[35]:

DF_compensation.to_csv('Q2_Part_1.csv') #Generating csv for the above result

