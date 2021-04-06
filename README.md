# Covid Deaths in Hungary
Small Python webscraping program to extract Covid deaths in Hungary.

## Background
As the Hungarian government is notoriously secretive about Covid statistics, I created a simple program which parses the official Covid page and creates a csv file detailing the number of deaths per age.
The data on the official page is paginated and spans over 400+ pages, therefore this small project is a nice leap towards greater transparency.
Source of data: https://koronavirus.gov.hu/elhunytak

## Usage
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required modules.

```bash
pip install -r requirements.txt 
```

Run app.py

Execution may take a few minutes.

A csv file will be generated with one column for the age group and another for the number of deaths.
Also, a JSON file will be generated.
