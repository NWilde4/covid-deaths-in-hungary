import requests
import bs4
import csv
import time

counter = 1
last_page_not_reached = True
age_dictionary = {age:0 for (age) in range(121)}

print('Program execution may take a few minutes.')
print('Program will close automatically when the csv file is ready.')
print('Loading...')
time.sleep(5)

while last_page_not_reached:
  url = f'https://koronavirus.gov.hu/elhunytak?page={counter}'
  res = requests.get(url)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  age_list = soup.select('td.views-field-field-elhunytak-kor')
  for age in age_list:
    formatted_age = int(age.getText().strip())
    age_dictionary[formatted_age] += 1
  print(f'{counter} pages parsed already.')
  # Check if last page has been reached
  if not (soup.find('li', class_='pager-last')):
    last_page_not_reached = False
  counter += 1


field_names = ['age', 'frequency']
with open('covid_deaths.csv', 'w') as f:
  writer = csv.writer(f, delimiter=';', lineterminator = '\n')
  writer.writerow(field_names)
  for row in age_dictionary.items():
    writer.writerow(row)

