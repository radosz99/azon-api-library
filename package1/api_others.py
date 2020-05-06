import requests
from requests.exceptions import HTTPError

def get_programming_languages(api_key):
    try:
        response = requests.get("https://api.e-science.pl/api/azon//programminglanguages/", headers={'X-Api-Key': api_key})
        response.raise_for_status()
        json_data  = response.json()
        results = json_data['results']
        lang_list=[]
        for item in results:
            lang_list.append(item['name'])
        return lang_list

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

class ResearchCenters:
    def __init__(self,_id, name, number, director, tel, email, webpage):
        self.id=_id
        self.name=name
        self.number=number
        self.director=director
        self.tel=tel
        self.email=email
        self.webpage=webpage

    def __repr__(self):
        return f'Id - {self.id}\nNazwa - {self.name}\nNumer - {self.number}\nDyrektor - {self.director}\nTelefon - {self.tel}\nE-mail - {self.email}\nStrona - {self.webpage}\n'

def get_pwr_reseach_centres(api_key):
    try:
        response = requests.get("https://api.e-science.pl/api/azon/databases/pwr_research_centers/", headers={'X-Api-Key': api_key})
        response.raise_for_status()
        json_data  = response.json()
        results = json_data['results']
        rc_list=[]
        for item in results:
            info={}
            info['_id']=item['id']
            info['name']=item['name']
            info['number']=item['number']
            info['director']=item['director']
            info['tel']=item['tel']
            info['email']=item['email']
            info['webpage']=item['webpage']
            rc_list.append(ResearchCenters(**info))
        return rc_list

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
