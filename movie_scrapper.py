# Group 7 : Arjun Venugopal Nair, Neethu Rajendran, Jees Jose, Rahul Somanathan
# IMDB Scraping using BeautifulSoup
# imports 
# beautifulSoup library used for web scrapping 

from bs4 import BeautifulSoup
# Library for using api request
import requests

# function to get movie details with 
# parameter movie name
def getMovieDetails(movieName):
    # base url of imdb
    baseUrl = 'https://www.imdb.com'

    # search query with movie name
    searchQuery = '/search/title?title='+'+'.join(movieName.strip().split(' '))

    # getting the webpage with movie details
    html = requests.get(baseUrl + searchQuery +'&title_type=feature')
    bs = BeautifulSoup(html.text, 'html.parser')
    

    # Getting the movie from list
    title = bs.find('h3', {'class': 'lister-item-header'})

    # if no title 
    if title is None:
        return None
    
    # getting movie link
    Link = baseUrl + title.a.attrs['href']
    
    # adding movie details
    movie = {}
    
    # Gets the page with movie details
 
    html = requests.get(Link)
    soup = BeautifulSoup(html.text, 'html.parser')
    movie['name'] = soup.find('h1', {'data-testid': 'hero-title-block__title'}).text
    movie['year'] = soup.find('span', {'class':'sc-8c396aa2-2 itZqyK'}).text
    movie['director'] = soup.find('a', {'class':'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'}).text
    movie['description'] = soup.find('span', {'data-testid': 'plot-xl'}).text

    return movie


# the main function

if __name__ == "__main__":
    movieName = input('Enter the movie name to fetch details: \n')
    movie = getMovieDetails(movieName)

    # If movie not found
    if movie is None:
        print('Movie not found')
        quit()
    
    # Movie Detail Output
    print('\n\n-----------------------------------------')
    print('Movie name: ', movie['name'])
    print('Release Date: ', movie['year'])
    print('Director: ', movie['director'])
    print('Description:' , movie['description'])
    print('-----------------------------------------')

