from . import api_handler


entries = api_handler.get_author_entries(3)

details = api_handler.get_entries_details(entries)

for item in details:
    print(item.get_bibtex())


with open("bibtex.bib", "a") as myfile:
    for item in details:
        myfile.write(item.get_bibtex()+'\n')
