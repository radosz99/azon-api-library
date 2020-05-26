import requests
import json
import time
from . import bibtex_classes
from requests.exceptions import HTTPError


class Entry:
    """Klasa reprezentujaca podstawowe atrybuty zasobu."""
    def __init__(self, pk, title, entry_type, entry_type_id, partner,
                 scientific_domain, authors, co_creators, attachments_number,
                 highlight='', file_result=''):
        self.pk = pk
        self.title = title
        self.entry_type = entry_type
        self.entry_type_id = entry_type_id
        self.partner = partner
        self.scientific_domain = scientific_domain
        self.authors = []
        for i in range(len(authors)):
            author = [authors[i]['pk'], authors[i]['first_name'],
                      authors[i]['last_name']]
            self.authors.append(author)

        self.co_creators = []
        for i in range(len(co_creators)):
            co_creator = [co_creators[i]['pk'], co_creators[i]['full_name']]
            self.authors.append(co_creator)

        self.attachments_number = attachments_number
        self.highlight = highlight
        self.file_result = file_result

    def __repr__(self):
        author = ''
        if(len(self.authors) > 0):
            author = self.authors[0][1] + " " + self.authors[0][2]
        return f'Tytuł - {self.title}\nId - {self.pk}\nAutor - {author}\
                \nTyp - {self.entry_type}\nPartner - {self.partner}\n'


def get_author_entries(author_pk, api_key):
    """Wysyla zapytanie o zasoby autora, nastepnie konwertuje je na format JSON,
    wydobywa wlasciwa wartosc, ktora nastepnie jest konwertowana na obiekty
    klasy Entry."""
    try:
        response = requests.get("https://api.e-science.pl/api/\azon/authors\
            /entries/"+str(author_pk)+"/", headers={'X-Api-Key': api_key})
        response.raise_for_status()
        json_data = response.json()
        results = json_data['results']
        entries_list = []
        for item in results:
            entries_list.append(Entry(**item))
        return entries_list

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')


def get_author_entries_by_page(author_pk, api_key, page):
    """Wysyla zapytanie o zasoby autora na danej stronie, nastepnie
    konwertuje je na format JSON, wydobywa wlasciwa wartosc, ktora
    nastepnie jest konwertowana na obiekty klasy Entry."""
    try:
        response = requests.get("https://api.e-science.pl/api/azon/authors/\
            entries/" + str(author_pk) + "/?limit = 100&offset = " +
            str(page) + "00", headers={'X-Api-Key': api_key})
        response.raise_for_status()
        json_data = response.json()
        results = json_data['results']
        entries_list = []
        for item in results:
            entries_list.append(Entry(**item))
        return entries_list

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')


def get_entries_by_page(api_key, page):
    """Wysyla zapytanie o zasoby na danej stronie, nastepnie
    konwertuje je na format JSON, wydobywa wlasciwa wartosc, ktora
    nastepnie jest konwertowana na obiekty klasy Entry."""
    try:
        _page = str(page)
        response = requests.get(r"""https://api.e-science.pl/api/azon/entry/filter/\
                                ?limit\=100&offset=""" +
                                _page + "00", headers={'X-Api-Key': api_key})
        response.raise_for_status()
        json_data = response.json()
        results = json_data['results']
        entries_list = []
        for item in results:
            entries_list.append(Entry(**item))
        return entries_list

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')


def get_entries_details(entries_list, api_key):
    """Wysyla zapytanie o detale poszczegolnych zasobow z listy, w zaleznosci od
    entry_type_id konwertuje je na odpowiedni obiekt, ktory nastepnie
    umieszczany jest na liscie."""
    entries_details = []
    for entry in entries_list:
        time.sleep(1)
        pk = entry.pk
        entry_type = entry.entry_type_id
        if(entry_type == 'e'):
            continue
        try:
            response = requests.get("https://api.e-science.pl/api/azon\
                /entry/"+str(pk)+"/", headers={'X-Api-Key': api_key})
            response.raise_for_status()
            json_data = response.json()
            switcher = {
                '1': get_book,  # book 47674
                '2': get_article,  # article 24052
                '4': get_phdthesis,  # dyplomowa 14813
                '6': get_photo,
                '7': get_misc,  # inny dokument misc 48245
                '10': get_techreport,  # chemiczny 6188
                '14': get_video,
                '15': get_misc,  # inny dokument misc 48245
                '17': get_misc,  # inny dokument misc 48245
                '18': get_magazine,  # czasopismo 33638
                '24': get_misc  # inny dokument misc 48245
            }
            item = switcher[entry_type](json_data)
            entries_details.append(item)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except KeyError as key_err:
            print(f'KeyError occurred: {key_err}')
    return entries_details


def get_book(json_data):
    """Konwertuje odpowiedz w formacie JSON na slownik, na podstawie
    ktorego tworzony obiekt klasy Book."""
    info = {}
    item = json_data['item']
    info['authors'] = json_data['authors']
    info['title'] = json_data['title']
    info['year'] = item['publish_time']
    info['publisher'] = item['publisher']
    info['isbn'] = item['isbn']
    info['note'] = json_data['comments']
    info['address'] = item['publish_place']
    info['edition'] = item['numeration']
    info['series'] = item['series_name']
    info['pk'] = json_data['pk']
    book = bibtex_classes.Book(**info)
    return book


def get_article(json_data):
    """Konwertuje odpowiedz w formacie JSON na slownik, na podstawie
    ktorego tworzony obiekt klasy Article."""
    info = {}
    article = None
    item = json_data['item']
    info['authors'] = json_data['authors']
    info['title'] = json_data['title']
    info['year'] = item['publish_time']
    info['pk'] = json_data['pk']
    info['note'] = json_data['comments']
    info['issn'] = item['issn']
    info['pages'] = str(item['page_from'])+'-'+str(item['page_to'])
    if(item['numeration'] is not None):  # inbook
        info['publisher'] = item['publisher']
        info['address'] = item['publish_place']
        article = bibtex_classes.InBook(**info)
    else:  # article
        info['number'] = item['numeration']
        info['journal'] = item['source_title']
        article = bibtex_classes.Article(**info)
    return article


def get_phdthesis(json_data):
    """Konwertuje odpowiedz w formacie JSON na slownik, na podstawie
    ktorego tworzony obiekt klasy Phdthesis."""
    info = {}
    item = json_data['item']
    info['authors'] = json_data['authors']
    info['title'] = json_data['title']
    info['year'] = item['creation_time']
    info['pk'] = json_data['pk']
    info['note'] = json_data['comments']
    info['address'] = item['creation_place']
    info['school'] = json_data['partner']
    phdthesis = bibtex_classes.Phdthesis(**info)
    return phdthesis


def get_misc(json_data):
    """Konwertuje odpowiedz w formacie JSON na slownik, na podstawie
    ktorego tworzony obiekt klasy Misc."""
    info = {}
    info['authors'] = json_data['authors']
    info['title'] = json_data['title']
    info['_type'] = json_data['entry_type']
    info['note'] = json_data['abstract']
    info['pk'] = json_data['pk']
    misc = bibtex_classes.Misc(**info)
    return misc


def get_techreport(json_data):
    """Konwertuje odpowiedz w formacie JSON na slownik, na podstawie
    ktorego tworzony obiekt klasy Techreport."""
    info = {}
    item = json_data['item']
    info['authors'] = json_data['authors']
    info['title'] = json_data['title']
    info['year'] = item['creation_time']
    info['pk'] = json_data['pk']
    info['note'] = json_data['comments']
    info['partner'] = json_data['partner']
    techreport = bibtex_classes.Techreport(**info)
    return techreport


def get_magazine(json_data):
    """Konwertuje odpowiedz w formacie JSON na slownik, na podstawie
    ktorego tworzony obiekt klasy Magazine."""
    info = {}
    item = json_data['item']
    info['authors'] = json_data['authors']
    info['creators'] = json_data['co_creators']
    info['title'] = json_data['title']
    info['year'] = item['publish_time']
    info['_type'] = json_data['abstract']
    info['pk'] = json_data['pk']
    info['note'] = json_data['comments']
    info['number'] = item['numeration']
    info['address'] = item['publish_place']
    info['pages'] = item['number_of_pages']
    magazine = bibtex_classes.Magazine(**info)
    return magazine


def get_photo(json_data):
    """Konwertuje odpowiedz w formacie JSON na slownik, na podstawie
    ktorego tworzony obiekt klasy Misc."""
    info = {}
    item = json_data['item']
    info['authors'] = json_data['authors']
    info['pk'] = json_data['pk']
    info['title'] = json_data['title']
    info['_type'] = json_data['entry_type']
    info['year'] = item['creation_time']
    info['note'] = json_data['abstract']
    info['series'] = item['series_name']
    info['address'] = item['creation_place']
    info['number'] = item['numeration']
    photo = bibtex_classes.Misc(**info)
    return photo


def get_video(json_data):
    """Konwertuje odpowiedz w formacie JSON na slownik, na podstawie
    ktorego tworzony obiekt klasy Misc."""
    info = {}
    item = json_data['item']
    info['authors'] = json_data['authors']
    info['creators'] = json_data['co_creators']
    info['pk'] = json_data['pk']
    info['title'] = json_data['title']
    info['_type'] = json_data['entry_type']
    info['year'] = item['creation_time']
    info['publisher'] = item['publisher']
    info['note'] = json_data['abstract']
    info['address'] = item['creation_place']
    info['number'] = item['numeration']
    video = bibtex_classes.Misc(**info)
    return video
