
# coding: utf-8

# Q1_Part one:
# 
# 1.Use ‘vehicle_collisions’ data set.
# 2.For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City.
# 3.Display a few rows of the output use df.head().
# 4.Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)
# 

# In[115]:

from pandas import DataFrame
import pandas as pd
import numpy as np
import datetime
import calendar


# In[116]:

# Reading data from the csv file and creating a dataframe.
Vehicles_Collision = pd.read_csv('\\Users\\kruts\\DataAnalysis4Python_Spring17\\Assignments\\Assignment 3\\Data\\vehicle_collisions.csv')
df = DataFrame(Vehicles_Collision)


# In[117]:

df['DATE'] = pd.to_datetime(df['DATE'])  #converting date to a dateformat
df['MONTH'] = df['DATE'].dt.month#fetching month from the date and creating a column 'MONTH'
df['MONTH'] = df['MONTH'].apply(lambda x: calendar.month_abbr[x])
df = df[(df['DATE'] > '2015-12-31') & (df['DATE'] < '2017-01-01')]  #fetching date for the year 2016.


# In[131]:

#creating new DataFrame, used group by for geting collisions of Manhattan for each month in the year 2016.
Frame_Collisions = DataFrame()
Frame_Collisions['MANHATTAN'] = df[df['BOROUGH']=='MANHATTAN'].groupby(['MONTH'],sort = False)['UNIQUE KEY'].count()
Frame_Collisions['NYC'] = df.groupby(['MONTH'],)['UNIQUE KEY'].count()
Frame_Collisions['PERCENTAGE']= Frame_Collisions['MANHATTAN']/Frame_Collisions['NYC']
Frame_Collisions.head(13).reset_index()


# In[132]:

Frame_Collisions.to_csv('Q1_part1.csv')  #Generated a csv for the above result.

