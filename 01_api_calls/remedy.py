import pandas as pd
import requests
import streamlit as st

import urllib.request
import json
import numpy as np
import matplotlib as plt
import pandas as pd

url= 'https://www.saferproducts.gov/RestWebServices/'
query= 'Recall?format=json&ProductType=Phone&Manufacturer=Samsung'
response= urllib.request.urlopen(url+query)
response_bytes= response.read()
data= json.loads(response_bytes)
response.close()

df= pd.DataFrame.from_dict(data)

temp = df['RemedyOptions']
clean_values = []
for i in range(len(temp)):
    if len(temp[i])>0:
        values = []
        for j in range(len(temp[i])):
            values.append(temp[i][j]['Option'] )  ## The keys in the dictionary are the most variable, thus focus making a code that works for keys in current dataframe
        clean_values.append(values)
    else:
        clean_values.append('')
df['RemedyOptions'] = clean_values

def clean_values(x, y):  ## Takes two attributes, x: the variable, y: the key
  clean_values= []
  for i in range(len(x)):
    if len(x[i])>0:
        values = []
        for j in range(len(x[i])):
          if y== 'Name':
            values.append(x[i][j]['Name'] )
          if y== 'Country':
            values.append(x[i][j]['Country'] )
          if y== 'URL':
            values.append(x[i][j]['URL'] )
          if y== 'Option':
            values.append(x[i][j]['Option'] )
        clean_values.append(values)
    else:
        clean_values.append('')
  return clean_values


prods= df['Products']
y= 'Name'
df['Products']= clean_values(prods, y)


dist= df['Distributors']
y= 'Name'
df['Distributors']= clean_values(dist, y)


manc= df['ManufacturerCountries']
y= 'Country'
df['ManufacturerCountries']= clean_values(manc, y)


haz= df['Hazards']
y= 'Name'
df['Hazards']= clean_values(haz, y)


incon= df['Inconjunctions']
y= 'URL'
df['Inconjunctions']= clean_values(incon, y)

manuf= df['Manufacturers']
y= 'Name'
df['Manufacturers']= clean_values(manuf, y)


remedy= df['Remedies']
y= 'Name'
df['Remedies']= clean_values(remedy, y)


ret= df['Retailers']
y= 'Name'
df['Retailers']= clean_values(ret, y)

# Create streamlit output:
remedy_counts = df['Remedies'].value_counts()
st.title('Example Stats: Remedy')
st.write('remedy_counts')
