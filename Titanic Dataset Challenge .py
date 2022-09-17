# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:56:39 2022

@author: hp
"""
"""
Dataset : Titanic CSV

Problem Statement : 
    It's a real-world data containig the details of titanic
    ships passengers list.'
    
Import the dataset "titanic.csv"

Answer  the following:
   1 How many people survived the disaster?
   2 How many people died?
   3 Calculate the survival rates as proportions (%)
   4 males that survived vs males that passed away
   5 Females that survived vs Females that passed away_
   6 Does age play a role in survival?
    
"""

import pandas as pd
import matplotlib.pyplot as py

tdf = pd.read_csv('Titanic.csv')

type(tdf)
tdf.head()
tdf.columns

tdf[tdf.isnull().any(axis=1)]

tdf['Survived'].value_counts()
#Answer 1 
people_survived = tdf['Survived'].value_counts()[1]
print(str(people_survived) +" people survived the TITANIC")
#342

tdf['PassengerId'].shape

#Answer 2
people_dead = tdf['Survived'].value_counts()[0]
print(str(people_dead)+" People were killed in TITANIC")


#Answer 3
survivalrate = tdf['Survived'].value_counts(normalize =True)[1]
print(str(survivalrate*100)+ " was the survival rate")
# 38.8 % survival rate

#Answer 4
tdf[(tdf['Sex'] == 'male') & (tdf['Survived'] == 1)]
#109 survived
tdf[(tdf['Sex'] == 'male') & (tdf['Survived'] == 0)]
#468 passed away
tdf[(tdf['Sex'] == 'female') & (tdf['Survived'] == 1)]
#233 females survived
tdf[(tdf['Sex'] == 'female') & (tdf['Survived'] == 0)]
#81 passed away


#Percentages of people who survived and died categorized by Gender

##MALES
male_surv = tdf['Survived'][tdf['Sex']=='male'].value_counts(normalize = True)[1]
print(str(round(male_surv*100,2))+"% males survived the TITANIC")

male_dead = tdf['Survived'][tdf['Sex']=='male'].value_counts(normalize = True)[0]
print(str(round(male_dead*100,2))+"% males died ")


##FEMALES
female_dead = tdf['Survived'][tdf['Sex']=='female'].value_counts(normalize = True)[0]
print(str(round(female_dead*100,2))+"% females died ")

female_surv = tdf['Survived'][tdf['Sex']=='female'].value_counts(normalize=True)[1]
print(str(round(female_surv*100,2))+"% females survived the titanic")


labels = ["female_dead" , "female_surv", "male_dead" , "male_surv"]
sizes = [female_dead , female_surv, male_dead , male_surv]
explode = [0,0.1,0,0.1]
plt.pie(sizes, labels=labels, explode=explode)

#Answer 5 
def filter_data(value):
    if 0 <= value <= 18:
        return 1
    else:
        return 0 

tdf['child'] = tdf['Age'].apply(filter_data)
#new column created

tdf['child'].value_counts()
c = tdf['Survived'][tdf['child']==1].value_counts(normalize = True)[1]
c
print("The number of children survived" + str(round(c*100,2)))

