import requests
import csv
import os

# define the API endpoint and the output file path
api_url = "https://api.census.gov/data/2014/acs/acs5/pums?get=PWGTP,WGTP,AGEP,SEX,ENG,LANP12&ucgid=0400000US36"
# api_url = "https://api.census.gov/data/2014/acs/acs5/pums?get=PWGTP,WGTP,AGEP,ENG,NATIVITY,NOP,LANP12,LNGI,LANX,LNGI_RC1,SEX&ucgid=0400000US36&recode+LNGI_RC1=%7B%22b%22:%22LNGI%22,%22d%22:%5B%5B%220%22,%221%22,%222%22%5D%5D%7D"
data_dir = os.path.join('..', 'data')
if not os.path.exists(data_dir):       
    data_dir = os.path.join('.', 'data')  # Folder to extract to; if script is started from made-wise2425 folder, do directly into "data"
output_file_path = os.path.join(data_dir, "ACS_PUMS.csv")

# Make the API request and parse the response as JSON
response = requests.get(api_url)
data = response.json()

# Save the data to a CSV file
with open(output_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Data saved to {output_file_path}")