# covid-deaths-in-hungary
Small Python webscraping program to calculate Covid deaths in Hungary

As the Hungarian government is notoriously secretive about Covid statistics, I created a simple program which parses the official Covid page and creates a csv file detailing the number of deaths per age.
The data on the official page is paginated and spans over 400+ pages, therefore this small project is a nice leap towards greater transparency.
Source of data: https://koronavirus.gov.hu/elhunytak

How to use:
Clone repository
Run: pip install -r requirements.txt in your shell
Run application. It may take minutes until the program finishes.
CVS is generated with latest covid death data.