import requests
import json
from requests.exceptions import HTTPError

class Entry:
    def __init__(self,pk,title,entry_type, entry_type_id, partner, scientific_domain, authors, co_creators, attachments_number):
        self.pk=pk
        self.title=title
        self.entry_type =entry_type
        self.entry_type_id=entry_type_id
        self.partner=partner
        self.scientific_domain=scientific_domain
        self.authors=[]
        for i in range (len(authors)):
            author = [authors[i]['pk'],authors[i]['first_name'],authors[i]['last_name'] ]
            self.authors.append(author)

        self.co_creators=[]
        for i in range (len(co_creators)):
            co_creator = [co_creators[i]['pk'],co_creators[i]['full_name']]
            self.authors.append(co_creator)

        self.attachments_number=attachments_number

    @classmethod
    def get_from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<Entry {self.title} number {self.pk} type {self.entry_type}>'



def say_hello2():
    try:
        response = requests.get("https://api.e-science.pl/api/azon/authors/entries/3/", headers={'X-Api-Key': 'JhHl8LOiMRCg3EFWnRcEpxdXmz1VJDYOc0fEhtBY'})
        response.raise_for_status()
        json_data  = response.json()
        results = json_data['results']
        entries_list=[]
        for item in results:
            entries_list.append(Entry(**item))
        print(entries_list)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        print('Success!')
    
    
if __name__ == "__main__":
    say_hello2()

