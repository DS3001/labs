import urllib.request
import json
url= 'https://www.saferproducts.gov/RestWebServices/'
query= 'Recall?format=json&ProductType=Phone'
response= urllib.request.urlopen(url+query)
response_bytes= response.read()
data= json.loads(response_bytes)
response.close()

print(data)

