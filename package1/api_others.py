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
