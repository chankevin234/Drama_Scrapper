import requests
import pprint

URL = 'https://ca.indeed.com/jobs?q=software+developer&l=Toronto%2C+ON'
page = requests.get(URL)
pp = pprint.PrettyPrinter(indent=4)

print(page)
print(pp)
