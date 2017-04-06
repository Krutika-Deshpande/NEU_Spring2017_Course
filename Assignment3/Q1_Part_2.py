
# coding: utf-8

# Q1_Part Two:
# 
# 1.Use ‘vehicle_collisions’ data set.
# 2.For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
# 3.Display a few rows of the output use df.head().
# 4.Generate a csv output with five columns ('borough', 'one-vehicle', 'two-vehicles', 'three-vehicles', 'more-vehicles')
# 

# In[3]:

from pandas import Series, DataFrame #importing all the required libraries
import pandas as pd
import numpy as np


# In[44]:

# Reading data from the csv file and creating a dataframe.
vehicle_collisions = pd.read_csv('\\Users\\kruts\\DataAnalysis4Python_Spring17\\Assignments\\Assignment 3\\Data\\vehicle_collisions.csv')
df = DataFrame(vehicle_collisions)


# In[58]:

#Counting Vehicle  1 type , 2 Type , 3 type and 4 Type across the Borough
df1 = df.groupby(['BOROUGH'],sort = False)['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE'].count().reset_index()
df1.head()


# In[64]:

DF_Vehcile_Involved = DataFrame() #creating an empty dataframe

DF_Vehcile_Involved['BOROUGH'] = df1['BOROUGH']  # copying Borough column to the new dataframe
DF_Vehcile_Involved['One_Vehicle_Involved'] = df1['VEHICLE 1 TYPE'] - df1['VEHICLE 2 TYPE'] #count of one Vehicle involved
DF_Vehcile_Involved['Two_Vehicles_Involved'] = df1['VEHICLE 2 TYPE'] - df1['VEHICLE 3 TYPE'] #count of two Vehicles involved
DF_Vehcile_Involved['Three_Vehicles_Involved'] = df1['VEHICLE 3 TYPE'] - df1['VEHICLE 4 TYPE'] # count of three Vehicles involved
DF_Vehcile_Involved['More_Vehicle_Involved'] = df1['VEHICLE 4 TYPE'] #count of more Vehicles involved
DF_Vehcile_Involved.set_index('BOROUGH', inplace = True)
print(DF_Vehcile_Involved.head())


# In[65]:

DF_Vehcile_Involved.to_csv('Q1_Part2.csv') #Generating csv for the above result

