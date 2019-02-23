# Extracting content from IMDB
from requests import get
from bs4 import BeautifulSoup
from tqdm import tqdm

url = 'https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

# Requisition for text
answer = get(url)

# html in text format
soup = BeautifulSoup(answer.text, 'html.parser')

# TAG list for movies
movies = soup.find_all('div', class_ = 'lister-item mode-advanced')

# Container movie
first_movie = movies[0]

# First Title
first_title = first_movie.h3.a.text

# First Year
first_year = first_movie.h3.find('span', class_ = 'lister-item-year').text

# IMDB Score
first_score_imdb = float(first_movie.strong.text)

# Votos
first_vote = first_movie.find('span', attrs = {'name':'nv'})['data-value']

names = []
years = []
imdbs = []
votes = []

# Extracting content for each movie
for movie in movies:

        # Name
        name = movie.h3.a.text
        names.append(name)

        # Year
        year = movie.h3.find('span', class_ = 'lister-item-year').text
        years.append(year)

        # IMDB
        imdb = float(movie.strong.text)
        imdbs.append(imdb)


        # Votes
        vote = movie.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))

