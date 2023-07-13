import random

class Films:
    def __init__(self,title,year_of_production,genre):
        self.title=title
        self.year_of_production=year_of_production
        self.genre=genre
        #Variable
        self.views=0

    def __str__(self):
        return f'{self.title} {self.year_of_production}'
    def __repr__(self):
        return f'{self.title} {self.year_of_production}'
    def play(self):
        self.views+=1


class TV_Series(Films):
    def __init__(self,episode,sezon,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.episode=episode
        self.sezon=sezon
    def __str__(self):
        return f'{self.title} S0{self.sezon}E0{self.episode}'
    def play(self):
        self.views+=1
    

list_of_movies =[]  
list_of_series=[]

film_1=Films(title="Piraci z Bałytku",year_of_production="2005",genre="przygodowy")
film_2=Films(title="Brudny Harold",year_of_production="1994",genre="akcji")
film_3=Films(title="16 w sobotę",year_of_production="1994",genre="horror")
serial_1=TV_Series(title="House of Postcards",year_of_production="2010",genre="obyczajowy",episode="1",sezon="1")
serial_2=TV_Series(title="House of Postcards",year_of_production="2010",genre="obyczajowy",episode="2",sezon="1")
serial_3=TV_Series(title="Breaking Good",year_of_production="2008",genre="komedia",episode="1",sezon="1")
serial_4=TV_Series(title="Breaking Good",year_of_production="2008",genre="komedia",episode="2",sezon="1")
serial_5=TV_Series(title="Breaking Good",year_of_production="2008",genre="komedia",episode="3",sezon="1")
list_of_films=[film_1,film_2,film_3,serial_1,serial_2,serial_3,serial_4,serial_5]


def get_movies(lista):
    for item in lista:
        if not isinstance(item,TV_Series):
            list_of_movies.append(item)
    sorted(list_of_movies,key=lambda movie: movie.title)
    return list_of_movies

def get_series(lista):
    for item in lista:
        if isinstance(item,TV_Series):
            list_of_series.append(item)
    sorted(list_of_series,key=lambda series: series.title)
    return list_of_series

def search(lista):
    film=""
    film=input("Podaj tytuł filmu, o którym potrzebujesz więcej szczegółów: ")
    for item in lista:
        if film == item.title:
            return f'{item.title} S0{item.sezon} E0{item.episode} rok produkcji: {item.year_of_production} gatunek: {item.genre}'
    return f'Nie ma takiego filmu w bazie :('

def generate_views(lista):
    los=random.randrange(0, len(lista))
    lista[los].views=random.randrange(1, 100) 
    print(lista[los].views)

def x10_gen_views(lista):
    for _ in range (10):
        generate_views(lista)

def top_titles(lista):
    how_many=int(input("Podaj o ilu najpopularniejszych filmach bądź serialach chcesz informację: "))
    type_of_film=int(input("""
    Jeżeli chcesz o filmach wybież - 1
    , jeżeli o serialach wybież - 2
    : """))

    list=[]
    if type_of_film == 1:
        list=get_movies(lista)
    elif type_of_film == 2:
        list=get_series(lista)
    else:
        print("Nie ma takiego numeru :(")

    list=sorted(list,key=lambda film: film.views,reverse=True)
    for i in range(how_many):
        print(f'{list[i]}, Ilość wyświetleń:{list[i].views}')
    


print(search(list_of_films))
generate_views(list_of_films)
x10_gen_views(list_of_films)
top_titles(list_of_films)