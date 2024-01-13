# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:58:08 2024

@author: ishuy
"""

import pandas as pd

#adding transaction.csv file
data = pd.read_csv('transaction.csv')
#telling that';' is used for separating columns
data = pd.read_csv('transaction.csv', sep=';')

# Data Cleaning starts

#using .info() method to extract summary of the data
data.info()

# Defining variables 
CostPerItem = 11.73 
SellingPricePerItem = 21.11 
NumberofItemsPurchased = 6 

# Mathematical Operations for arranging the Data
ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem 
CostPerTransaction = NumberofItemsPurchased*CostPerItem 
SellingPricePerTransaction = NumberofItemsPurchased*SellingPricePerItem 

#CostPerTransaction Column Calculation 
# f(x)>> CostPerTransaction = CostPerltem * NumberofltemsPurchases 
# variable = dataframePcolumn_namel 
CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased 
#adding a new column to a dataframe 
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased'] 

#Sales per Transaction 
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost
data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# (Sales - Cost)/Cost 
data ['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] )/data['CostPerTransaction']
  
data ['Markup'] = ( data['ProfitperTransaction'] )/data['CostPerTransaction']

#Rounding Marking
roundmarkup = round(data['Markup'], 2)
data['Markup'] = round(data['Markup'], 2)

#Combining data fields
# Assuming 'Day', 'Month', and 'Year' are columns in your DataFrame 'data'
day = data['Day'].astype(str)
month = data['Month'].astype(str)
year = data['Year'].astype(str)

my_date = day + '-' + month + '-' + year
#adding new column for date
data['date'] = my_date

#using.head method to verify addon of column - date
data.head()

#spliiting client keywords

#new var = column.str.split('sep' , expand = True) 
split_col = data['ClientKeywords'].str.split(',' , expand=True) 

#creating new columns for the split columns in Client Keywords 

data['ClientAge'] = split_col[0]
data['ClienType'] = split_col[1]
data['LengthofContract'] = split_col[2] 

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

#using the lower function to change item to lowercasse
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')
#checking season addon
data.iloc[-5:]

#dropping columns
# df = df.drop('columnname', axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

#EExporting into csv

data.to_csv('ValueInc_Cleaned.csv', index = False)
