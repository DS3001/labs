import pandas as pd
import requests
import streamlit as st
import urllib.request
import json

url = 'https://wizard-world-api.herokuapp.com/' # Location of the API
query = 'Houses' # The query
response = urllib.request.urlopen(url+query)
response_bytes = response.read()

data = json.loads(response_bytes) # Convert response to json
df = pd.DataFrame.from_dict(data)

houses = {}

for field in data:
    traits = []
    for trait in field['traits']:
        traits.append(trait['name'])
    houses[field['name']] = traits


for house in houses:
    print(houses[house])


st.set_page_config(page_title="Hogwarts Houses and Traits")
st.markdown("<h1 style='text-align: center; color: #9c27b0;'>Hogwarts Houses and Their Traits</h1>", unsafe_allow_html=True)

for house in houses:
    st.subheader(f"{house} Traits")
    for trait in houses[house]:
        st.write(f"- {trait}")
    st.write("---")
