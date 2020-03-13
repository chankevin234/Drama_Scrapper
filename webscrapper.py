import requests
import json
from bs4 import BeautifulSoup

URL = 'https://ca.indeed.com/jobs?q=software+developer&l=Toronto%2C+ON' #url
page = requests.get(URL).text #page object

soup = BeautifulSoup(requests.get(URL).text, 'html.parser') #instantiate bsoup object

results = soup.find(id='ResultsContainer')
#print(results.prettify()) 

#select items in <selection> within 

job_elems = results.find_all('section', class_='card-content')

def jobExtractor(job_elems):
    for job_elem in job_elems:
        #print(job_items, end='\n'*2) --> print all bsoup objects
        title_elem = job_elem.find('h2', class_='title') #job_title elements
        company_elem = job_elem.find('div', class_='company')
        location_elem = job_elem.find('div', class_='location')

        print(title_elem.text)
        print(company_elem.text) 
        print(location_elem.text)
        print()

if __name__ == "__main__":
    jobExtractor()