from . import api_handler
from . import api_others
api_key='JhHl8LOiMRCg3EFWnRcEpxdXmz1VJDYOc0fEhtBY'

#entries = api_handler.get_author_entries_by_page(2871,api_key,10)
#entries = api_handler.get_entries_by_page(api_key,100)
#etails = api_handler.get_entries_details(entries,api_key)

entries = api_others.get_pwr_reseach_centres(api_key)
for detail in entries:
    print(detail)
# for item in details:
#     print(item.get_bibtex())


# with open("bibtex.bib", "a") as myfile:
#     for item in details:
#         myfile.write(item.get_bibtex()+'\n')
