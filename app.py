import requests
import bs4
import csv
import time
import math
import json

counter = 1
last_page_not_reached = True
age_dictionary = {age:0 for (age) in range(121)}

#  Get total number of pages estimate
url = 'https://koronavirus.gov.hu/elhunytak'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
largest_death_id_element = soup.select('td.views-field-field-elhunytak-sorszam')
largest_death_id = math.ceil(float(largest_death_id_element[0].getText().strip()))
estimated_number_of_pages = int(largest_death_id / 50)

print('Program execution may take a few minutes.')
print('Program will close automatically when the csv and JSON file are ready.')
print('Loading...')
time.sleep(5)

# Parse each page and collect the ages of deaths.
while last_page_not_reached:
  url = f'https://koronavirus.gov.hu/elhunytak?page={counter}'
  res = requests.get(url)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  age_list = soup.select('td.views-field-field-elhunytak-kor')
  for age in age_list:
    formatted_age = int(age.getText().strip())
    age_dictionary[formatted_age] += 1
  print(f'{counter} pages parsed already of about {estimated_number_of_pages}.')
  # Check if last page has been reached
  if not (soup.find('li', class_='pager-last')):
    last_page_not_reached = False
  counter += 1

# Create cvs file of findings.
field_names = ['age', 'frequency']
with open('covid_deaths.csv', 'w') as f:
  writer = csv.writer(f, delimiter=';', lineterminator = '\n')
  writer.writerow(field_names)
  for row in age_dictionary.items():
    writer.writerow(row)

# Create JSON file of findings.
list_of_objects = [{'age': key, 'deaths': value} for key, value in age_dictionary.items()]
covid_deaths_object = {"agegroup": list_of_objects}

with open('covid_deaths.json', 'w') as f:
  json.dump(covid_deaths_object, f, indent=2)