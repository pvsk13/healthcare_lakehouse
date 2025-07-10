import requests
import pandas as pd

URL = "https://data.cms.gov/provider-data/api/1/datastore/query/xubh-q36u/0"

response = requests.get(URL)
data = response.json()

df = pd.json_normalize(data['results'])

df.to_csv("../data/raw/hospital_data.csv", index=False)

print("Raw healthcare data saved")