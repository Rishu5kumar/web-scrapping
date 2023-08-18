import requests
import sys

from bs4 import BeautifulSoup


pypi_url = 'https://pypi.org/search/'
req = requests.get(pypi_url)
if not req.status_code in (200, 201, 202):
    print('Error')
    sys.exit(0)

soap = BeautifulSoup(req.text, 'html.parser')
div = soap.find("div", {"id": "accordion-Topic"})
child_div = div.find('div', {'class': 'checkbox-tree'})
ul = child_div.find('ul')

topics = []


for li in ul.findChildren('li', recursive=False):
   topic = li.find('label').get_text()
   topics.append(topic)

for pos, val in enumerate(topics):
    print(f'{pos+1}: {val}')

print("ENter topic name to get list of sub-topics")
user_topic = input("Topic Name: ")
print(user_topic)

if not user_topic in topics:
    print("Wrong topic name. Select from the list above")
    sys.exit(0)

pos = topics.index(user_topic)
sub_topics = []
for li in ul.findAll('li'):
    if li.findAll('label', recursive=False)[0].get_text() == user_topic:
        for cul in li.findAll('ul', recursive=False):
            for cli in cul.findAll('li', recursive=False):
                tpc = cli.find('label').get_text()
                sub_topics.append(tpc)

print(f"Child topics for topic {user_topic}")
for pos, val in enumerate(sub_topics):
    print(f'{pos+1}: {val}')

