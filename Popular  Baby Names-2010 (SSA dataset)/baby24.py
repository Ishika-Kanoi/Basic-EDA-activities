# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:56:52 2022

@author: hp
"""
"""
Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made 
    available data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip)  
    
1   Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that 
    particular data. 
    
2   Concatenate all the data to form single dataframe 
    using pandas concat method.
    
3   Display the top 5 male and female baby names of 2010.
    
4   Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas groupby method).
    
5   Plot the results of the above activity to show total births 
    by sex and year.
"""
#importng all the necessary libraries
import pandas as pd
import numpy as np
from glob import glob
import re

#1.collecting required data
filenames = glob('*txt')
ssa_list=[]
for file in filenames:
    tempdf= pd.read_csv(file,names = ['names','sex','count'])#create df label names, txt iin csv format
    year = int(re.findall('\d{4}', file)[0])#year int
    if year>2010:
        break
    tempdf['year']= year
    ssa_list.append(tempdf)
    
    
#2.concatenate the data frames
new_df = pd.concat(ssa_list,ignore_index=True,axis = 0)

#3.display top 5 names of 2010: Male and Female
year2010 = new_df[new_df['year'] == 2010]

malefilter = year2010[year2010['sex']=='M']

femalefilter = year2010[year2010['sex']=='F']

    #using sort to count frequency of names for year 2010
count_of_Fnames = femalefilter.sort_values('count',ignore_index = True , ascending = False)
count_of_Mnames = malefilter.sort_values('count', ignore_index=True, ascending = False)

print(count_of_Mnames['names'][0:5])
print(count_of_Fnames['names'][0:5])

#4.calculate sum of births column by sex as the total number in the year.
grouped = new_df.groupby(['year','sex']).agg({'count': ['sum']})

print(grouped)
#contains aggregated cont

#5.how many female and how many male names
grouped.plot(kind='bar')

grouped[0:10].plot(kind='bar')
