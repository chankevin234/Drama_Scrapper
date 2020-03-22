import requests
import json
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia' #url
page = requests.get(URL).text #page object

soup = BeautifulSoup(requests.get(URL).text, 'html.parser') #instantiate bsoup object

results = soup.find(id='ResultsContainer')
#print(results.prettify()) 

#select items in <selection> within 

job_elems = results.find_all('section', class_='card-content')
python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
print(len(python_jobs))

def job_elements_extractor(job_elems):
    for job_elem in job_elems:
        #print(job_items, end='\n'*2) --> print all bsoup objects
        title_elem = job_elem.find('h2', class_='title') #job_title elements
        company_elem = job_elem.find('div', class_='company')
        location_elem = job_elem.find('div', class_='location')

        if None in (title_elem, company_elem, location_elem):
            continue

        # print(title_elem.text.strip())
        # print(company_elem.text.strip()) 
        # print(location_elem.text.strip())
        # print()
        return True

def job_elements_python_extractor(python_jobs):
    for py_job in python_jobs:
        py_links = py_job.find('a')['href']
        print(py_job.text.strip()) 
        print(f"Apply here: {py_links}\n")
        return py_links
        
if __name__ == "__main__":
    filtered_jobs = job_elements_extractor(job_elems)
    filtered_python_jobs = job_elements_python_extractor(python_jobs)
    