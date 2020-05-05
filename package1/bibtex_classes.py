class Book:
    def __init__(self,pk,authors, title, publisher, year, volume='', series='', address='',edition='',month='',note='',key='',isbn=''):
        self.pk=pk
        self.authors=[]
        for i in range (len(authors)):
            author = authors[i]['author']
            self.authors.append(author)
        self.authors_string=''
        for i in range (len(self.authors)):
            self.authors_string+=self.authors[i]
            if(i!=len(self.authors)-1):
                self.authors_string+=', '
        self.title=title
        self.publisher=publisher
        self.year=year
        self.volume=volume
        self.series=series
        self.address=address
        self.edition=edition
        self.month=month
        self.note=note
        self.key=key
        self.isbn=isbn

    def __repr__(self):
        return f'Autor - {self.authors_string}\nTytuł - {self.title}\npublisher - {self.publisher}\nyear - {self.year}\nisbn - {self.isbn}\n'

    def get_bibtex(self):
        bib=f'@book{{{self.pk},\n  author =\t"{self.authors_string}",\n  title =\t"{self.title}",\n  publisher =\t"{self.publisher}",\n  year =\t{self.year},'
        if(self.volume!='' and self.volume!=None):
            bib+=f'\n  volume =\t"{self.volume}",'
        if(self.series!='' and self.series!=None):
            bib+=f'\n  series =\t"{self.series}",'
        if(self.address!='' and self.address!=None):
            bib+=f'\n  address =\t"{self.address}",'
        if(self.edition!='' and self.edition!=None):
            bib+=f'\n  edition =\t"{self.edition}",'
        if(self.month!='' and self.month!=None):
            bib+=f'\n  month =\t{self.month},'
        if(self.note!='' and self.note!=None):
            bib+=f'\n  note =\t"{self.note}",'
        if(self.key!='' and self.key!=None):
            bib+=f'\n  key =\t"{self.key}",'
        if(self.isbn!='' and self.isbn!=None):
            bib+=f'\n  isbn =\t"{self.isbn}",'
        bib=bib[0:len(bib)-1]+'\n}'
        return bib


class Article:
    def __init__(self,pk,authors, title, journal, year, number='', pages='',note='',issn=''):
        self.pk=pk
        self.authors=[]
        for i in range (len(authors)):
            author = authors[i]['author']
            self.authors.append(author)
        self.authors_string=''
        for i in range (len(self.authors)):
            self.authors_string+=self.authors[i]
            if(i!=len(self.authors)-1):
                self.authors_string+=', '
        self.title=title
        self.journal=journal
        self.year=year
        self.number=number
        self.pages=pages
        self.note=note
        self.issn=issn

    def __repr__(self):
        return f'Autor - {self.authors_string}\nTytuł - {self.title}\njournal - {self.journal}\nyear - {self.year}\nissn - {self.issn}\n'

    def get_bibtex(self):
        bib=f'@article{{{self.pk},\n  author =\t"{self.authors_string}",\n  title =\t"{self.title}",\n  journal =\t"{self.journal}",\n  year =\t{self.year},'
        if(self.pages!='' and self.pages!=None):
            bib+=f'\n  pages =\t{self.pages},'
        if(self.number!='' and self.number!=None):
            bib+=f'\n  number =\t"{self.number}",'
        if(self.note!='' and self.note!=None):
            bib+=f'\n  note =\t"{self.note}",'
        if(self.issn!='' and self.issn!=None):
            bib+=f'\n  issn =\t"{self.issn}",'
        bib=bib[0:len(bib)-1]+'\n}'
        return bib    

class InBook:
    def __init__(self,pk,authors, title, pages, publisher, year, address='',note='', issn=''):
        self.pk=pk
        self.authors=[]
        for i in range (len(authors)):
            author = authors[i]['author']
            self.authors.append(author)
        self.authors_string=''
        for i in range (len(self.authors)):
            self.authors_string+=self.authors[i]
            if(i!=len(self.authors)-1):
                self.authors_string+=', '
        self.title=title
        self.pages=pages
        self.publisher=publisher
        self.year=year
        self.address=address
        self.note=note
        self.issn=issn

    def __repr__(self):
        return f'Autor - {self.authors_string}\nTytuł - {self.title}\npages - {self.pages}\nyear - {self.year}\npublisher - {self.publisher}\n'

    def get_bibtex(self):
        bib=f'@inbook{{{self.pk},\n  author =\t"{self.authors_string}",\n  title =\t"{self.title}",\n  publisher =\t"{self.publisher}",\n  pages =\t{self.pages},\n  year =\t{self.year},'
        if(self.address!='' and self.address!=None):
            bib+=f'\n  address =\t"{self.address}",'
        if(self.note!='' and self.note!=None):
            bib+=f'\n  note =\t"{self.note}",'
        if(self.issn!='' and self.issn!=None):
            bib+=f'\n  issn =\t"{self.issn}",'
        bib=bib[0:len(bib)-1]+'\n}'
        return bib

class Misc:
    def __init__(self,pk,authors='', title='', note='', _type=''):
        self.pk=pk
        self.authors=[]
        for i in range (len(authors)):
            author = authors[i]['author']
            self.authors.append(author)
        self.authors_string=''
        for i in range (len(self.authors)):
            self.authors_string+=self.authors[i]
            if(i!=len(self.authors)-1):
                self.authors_string+=', '
        self.title=title
        self.note=note
        self.type=_type

    def get_bibtex(self):
        bib=f'@misc{{{self.pk},'
        if(self.authors!='' and self.authors!=None):
            bib+=f'\n  authors =\t"{self.authors}",'
        if(self.title!='' and self.title!=None):
            bib+=f'\n  title =\t"{self.title}",'
        if(self.type!='' and self.type!=None):
            bib+=f'\n  type =\t"{self.type}",'
        if(self.note!='' and self.note!=None):
            bib+=f'\n  note =\t"{self.note}",'
        bib=bib[0:len(bib)-1]+'\n}'
        return bib

class Techreport:
    def __init__(self,pk,authors, title, partner, year, address='',note=''):
        self.pk=pk
        self.authors=[]
        for i in range (len(authors)):
            author = authors[i]['author']
            self.authors.append(author)
        self.authors_string=''
        for i in range (len(self.authors)):
            self.authors_string+=self.authors[i]
            if(i!=len(self.authors)-1):
                self.authors_string+=', '
        self.title=title
        self.partner=partner
        self.year=year
        self.address=address
        self.note=note

    def get_bibtex(self):
        bib=f'@techreport{{{self.pk},\n  author =\t"{self.authors_string}",\n  title =\t"{self.title}",\n  institution =\t"{self.partner}",\n  year =\t{self.year},'
        if(self.address!='' and self.address!=None):
            bib+=f'\n  address =\t"{self.address}",'
        if(self.note!='' and self.note!=None):
            bib+=f'\n  note =\t"{self.note}",'
        bib=bib[0:len(bib)-1]+'\n}'
        return bib 

class Phdthesis :
    def __init__(self,pk,authors, title, school, year, address='',note=''):
        self.pk=pk
        self.authors=[]
        for i in range (len(authors)):
            author = authors[i]['author']
            self.authors.append(author)
        self.authors_string=''
        for i in range (len(self.authors)):
            self.authors_string+=self.authors[i]
            if(i!=len(self.authors)-1):
                self.authors_string+=', '
        self.title=title
        self.school=school
        self.year=year
        self.address=address
        self.note=note

    def get_bibtex(self):
        bib=f'@phdthesis{{{self.pk},\n  author =\t"{self.authors_string}",\n  title =\t"{self.title}",\n  school =\t"{self.school}",\n  year =\t{self.year},'
        if(self.address!='' and self.address!=None):
            bib+=f'\n  address =\t"{self.address}",'
        if(self.note!='' and self.note!=None):
            bib+=f'\n  note =\t"{self.note}",'
        bib=bib[0:len(bib)-1]+'\n}'
        return bib 