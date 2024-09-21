import pandas as pd
import requests
import streamlit as st
import urllib.request
import json

url = 'https://www.saferproducts.gov/RestWebServices/' # Location of the API
query = 'Recall?format=json&ProductType=Exercise' # The query
response = urllib.request.urlopen(url+query)
response_bytes = response.read()
data = json.loads(response_bytes) # Convert response to json

# Conduct analysis:
df = pd.DataFrame.from_dict(data)
temp = df['RemedyOptions']
clean_values = []
for i in range(len(temp)):
    if len(temp[i])>0:
        values = []
        for j in range(len(temp[i])):
            values.append(temp[i][j]['Option'] )
        clean_values.append(values)
    else:
        clean_values.append('')
df['remedy'] = clean_values
remedy_counts = df['remedy'].value_counts()
# Create streamlit output:
st.title('Remedy Statistics')
# Create bar chart displaying data
st.bar_chart(remedy_counts)
