'''
This Flask web application serves as an anime information portal, allowing users to search for and retrieve information about various anime titles. 
It utilizes an AnimeAPI class to fetch data from an external source and display it on the web pages. 
The application supports searching for anime titles based on genre, number of episodes, score, and specific ranges of scores or episodes. 
Additionally, it retrieves specific information about an anime title, such as its score, number of episodes, synopsis, and genres. 
The application contains multiple routes to handle the different search functionalities and display the results on corresponding HTML templates.
'''

import flask
from flask import render_template, request
import json
import sys
from api import AnimeAPI

app = flask.Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/home/')
def homepage():
    '''    
    Renders the homepage (index.html) of the web application
    '''
    return render_template('index.html')

@app.route('/about/')
def aboutpage():
    '''
    Renders the about page (about.html) of the web application.
    '''
    return render_template('about.html')
 
@app.route('/data/')
def datapage():
    '''
    Renders the data page (datapage.html) of the web application.
    '''
    return render_template('datapage.html')

@app.route('/AnimefromGenre', methods=['GET', 'POST'])
def search_from_genre():
    '''
    Handles search requests for anime titles based on genre. Retrieves the genre from the submitted
    form, fetches the anime titles from the AnimeAPI, and renders the results on results.html.
    '''
    try:
        genre_for_anime = ''
        anime_from_genre = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            genre_for_anime = request.form['AnimefromGenre']
            animeTitles = animeAPI.getTitleofAnimefromGenre(genre_for_anime)
            if not animeTitles:
                raise ValueError ("Invalid Query")
            anime_from_genre = ', '.join(animeTitles)
            return render_template('results.html', genre_for_anime = genre_for_anime, anime_from_genre = anime_from_genre)
        else:
            raise ValueError("Invalid Query")
    except ValueError:
        return render_template('error.html')

@app.route('/AnimefromNumEps', methods=['GET', 'POST'])
def search_from_num_of_eps():
    '''
    Handles search requests for anime titles based on the number of episodes. Retrieves the desired
    number of episodes from the submitted form, fetches the anime titles from the AnimeAPI, and
    renders the results on results.html.
    '''
    try:
        num_eps_for_anime = ''
        anime_from_num_eps = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            num_eps_for_anime = request.form['AnimefromNumEps']
            animeTitles = animeAPI.getTitleofAnimefromNumberOfepisodes(num_eps_for_anime)
            if not animeTitles:
                raise ValueError ("Invalid Query")
            anime_from_num_eps = ', '.join(animeTitles)
            return render_template('results.html', num_eps_for_anime = num_eps_for_anime, anime_from_num_eps = anime_from_num_eps)
        else:
            raise ValueError("Invalid Query")
    except ValueError:
        return render_template('error.html')


@app.route('/AnimefromScore', methods=['GET', 'POST'])
def search_from_score():
    '''
    Handles search requests for anime titles based on score. Retrieves the desired score from the
    submitted form, fetches the anime titles from the AnimeAPI, and renders the results on
    results.html.
    '''
    try:

        score_for_anime = ''
        anime_from_score = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            score_for_anime = request.form['AnimefromScore']
            animeTitles = animeAPI.getTitleofAnimefromScore(score_for_anime)
            if not animeTitles:
                raise ValueError ("invalid query")
            anime_from_score = ', '.join(animeTitles)
            return render_template('results.html', score_for_anime = score_for_anime, anime_from_score = anime_from_score)
        else:
            raise ValueError ("Invalid Query")
    except ValueError:
        return render_template('error.html')


@app.route('/AnimefromNumEpsRange', methods=['GET', 'POST'])
def search_from_num_of_eps_range():
    '''
    Handles search requests for anime titles based on a range of the number of episodes. Retrieves
    the desired range from the submitted form, fetches the anime titles from the AnimeAPI, and
    renders the results on results.html.
    '''
    try:
        num_of_eps_range_for_anime = ''
        anime_from_num_of_eps_range = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            num_of_eps_range_for_anime = request.form['AnimefromNumEpsRange']
            animeTitles = animeAPI.getTitleofAnimefromNumberOfepisodesRange(num_of_eps_range_for_anime)
            if not animeTitles:
                raise ValueError ("Invalid Query")
            anime_from_num_of_eps_range = ', '.join(animeTitles)
            return render_template('results.html', num_of_eps_range_for_anime = num_of_eps_range_for_anime, anime_from_num_of_eps_range = anime_from_num_of_eps_range)
        else:
            raise ValueError("Invalid Query")
    except ValueError:
        return render_template('error.html')


@app.route('/AnimefromScoreRange', methods=['GET', 'POST'])
def search_from_score_range():
    '''
    Handles search requests for anime titles based on a range of scores. Retrieves the desired score
    range from the submitted form, fetches the anime titles from the AnimeAPI, and renders the
    results on results.html.
    '''
    try:
        range_of_score_for_anime = ''
        anime_from_score_range = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            range_of_score_for_anime = request.form['AnimefromScoreRange']
            animeTitles = animeAPI.getTitleofAnimefromScoreRange(range_of_score_for_anime)
            if not animeTitles:
                raise ValueError ("invalid Query")
            anime_from_score_range = ', '.join(animeTitles)
            return render_template('results.html', range_of_score_for_anime=range_of_score_for_anime, anime_from_score_range = anime_from_score_range)
        else:
            raise ValueError ("Invalid Query")
    except ValueError:
        return render_template('error.html')



@app.route('/ScorefromAnime', methods=['GET', 'POST'])
def search_for_score():
    '''
    Handles requests to retrieve the score of a specific anime title. Retrieves the title from the
    submitted form, fetches the score from the AnimeAPI, and renders the result on results.html.
    '''
    try:

        title_for_score = ''
        score_from_title = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            title_for_score = request.form['ScorefromAnime']
            scoreS = animeAPI.getScoreofAnime(title_for_score)
            if not scoreS:
                raise ValueError("Invalid query")
            score_from_title = scoreS[0]
            return render_template('results.html', title_for_score = title_for_score, score_from_title = score_from_title)
        else:
            raise ValueError("Invalid Query")
    except ValueError:
        return render_template('error.html')

@app.route('/NumEpsfromAnime', methods=['GET', 'POST'])
def search_for_num_of_eps():
    '''
    Handles requests to retrieve the number of episodes of a specific anime title. Retrieves the
    title from the submitted form, fetches the number of episodes from the AnimeAPI, and renders
    the result on results.html.
    '''
    try:

        title_for_numEps = ''
        numEps_from_title = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            title_for_numEps = request.form['NumEpsfromAnime']
            numOfEpisodesS = animeAPI.getNumberofEpisodes(title_for_numEps)
            if not numOfEpisodesS:
                raise ValueError("Invalid query")
            numEps_from_title = numOfEpisodesS[0]
            return render_template('results.html', title_for_numEps = title_for_numEps, numEps_from_title = numEps_from_title)
        else:
            raise ValueError("Invalid query")
    except ValueError:
        return render_template('error.html')

@app.route('/SynopsisfromAnime', methods=['GET', 'POST'])
def search_for_synopsis():
    '''
    Handles requests to retrieve the synopsis of a specific anime title. Retrieves the title from
    the submitted form, fetches the synopsis from the AnimeAPI, and renders the result on results.html.
    '''
    try:
        title_for_synopsis = ''
        synopsis_from_title = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            title_for_synopsis = request.form['SynopsisfromAnime']
            synopsisS = animeAPI.getSynopsis(title_for_synopsis)
            if not synopsisS:
                raise ValueError("Invalid query")
            synopsis_from_title = synopsisS[0]
            return render_template('results.html', title_for_synopsis = title_for_synopsis, synopsis_from_title = synopsis_from_title)
        else:
            raise ValueError("Invalid query")
    except ValueError:
        return render_template('error.html')

        
@app.route('/GenresfromAnime', methods=['GET', 'POST'])
def search_for_genre():
    '''
    Handles requests to retrieve the genres of a specific anime title. Retrieves the title from the
    submitted form, fetches the genres from the AnimeAPI, and renders the result on results.html.
    '''
    try:

        title_for_genre = ''
        genre_from_title = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            title_for_genre = request.form['GenresfromAnime']
            genreS = animeAPI.getGenre(title_for_genre)
            if not genreS:
                raise ValueError("Invalid Query")
            genre_from_title = genreS[0]
            return render_template('results.html', title_for_genre = title_for_genre, genre_from_title = genre_from_title)
        else:
            raise ValueError("Invalid Query")
    except ValueError:
        return render_template('error.html')

'''
Execute the Flask web application by running 'python3 localhost [port]' in the terminal, where [port] is a valid port number.
This script checks for proper command-line arguments, and if valid, starts the Flask development server with the specified host and port.
'''
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()
    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host = host, port = port, debug = True)

