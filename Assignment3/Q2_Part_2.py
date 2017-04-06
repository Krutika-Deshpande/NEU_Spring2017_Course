
# coding: utf-8

# Q2_Part Two:
#     
# 1.Use 'employee_compensation' data set.
# 2.Find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# 3.For each job family these people are associated with (job family refers to ’Job Family' column), calculate what is the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column (Percent_total_benefit) which has the percentage value.
# 4.Display the top 5 job families according to Percent_total_benefit using df.head().
# 5.Write the output (jobs and Percent_total_benefit) to a csv.
# 

# In[1]:

import pandas as pd # importing the required Libraries
from pandas import DataFrame


# In[44]:

#Reading data from the csv file 
frame= pd.read_csv('\\Users\\kruts\\DataAnalysis4Python_Spring17\\Assignments\\Assignment 3\\Data\\employee_compensation.csv')


# In[45]:

df1 = DataFrame(frame) #created a dataframe to fetch employees with overtime 5 % more than the salaries
df1['Employee Identifier'] = df1['Employee Identifier'].where(df1['Overtime']>((5/100)*df1['Salaries']))
df1 = df1.dropna()  # eliminating the NaN values


# In[52]:

#Creating an empty DataFrame 
DF_Result = DataFrame() 
#Calculating average benefits for Job Family with overtime 5% more than salaries
DF_Result['Total Benefits'] = df1.groupby(['Job Family'])['Total Benefits'].mean() 
#Calculating average compensation for Job Familywith overtime 5% more than salaries
DF_Result['Total Compensation'] = df1.groupby(['Job Family'])['Total Compensation'].mean()
#Calculating the percentage of total benefits over total compensation for each Job Family
DF_Result['Percent_Total_Benefits'] = (DF_Result['Total Benefits']/DF_Result['Total Compensation']) * 100
#Displaying the top 5 Job Families based on the highest percent_total_benefits
DF_Result.sort_values('Percent_Total_Benefits',ascending = False)[0:5]
print(DF_Result.head())


# In[53]:

DF_Result.to_csv('Q2_Part_2.csv')

