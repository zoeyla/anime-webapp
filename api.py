import psycopg2

import psqlConfig as config

class AnimeAPI:

    def __init__(self):

        ''' Connects to the anime database using credentials from psqlConfig '''
        try:
            ''' Attempts to connect to datbase using credentials '''
            connection = psycopg2.connect (

                database=config.database, 
                user=config.user, 
                password=config.password, 
                host="localhost"

                )

            self.connection  = connection

        except Exception as e:

            ''' If connection fails, prints error and exits connection '''

            print("connection error: ", e)
            exit()


    def getTitleofAnimefromGenre(self, genres):

        ''' Returns a list of anime as a string based on the genre inputted from the user '''

        try:
            ''' Creates a cursor to use'''
            cursor = self.connection.cursor()

            ''' Query '''
            query = "SELECT title FROM anime WHERE "

            conditions = []
            for genre in genres:
                conditions.append("genre LIKE %s") #appends a string to the conditions list that specifies a LIKE condition for the current genre
            query += " AND ".join(conditions) #concatenates the LIKE conditions in the conditions list using the AND operator, and appends them to the query string.
            values = tuple(f"%{genre}%" for genre in genres) #creates a tuple of values that will replace the %s placeholders in the query string

            ''' Executes Query and retrieves all the rows from the result set at once '''
            cursor.execute(query, values)
            result = cursor.fetchall()
            return [title[0] for title in result] 
        
        except Exception as e:
            ''' If query fails to excute, error message is printed '''

            print ("Something went wrong when executing the query: ", e)
            return None


    def getTitleofAnimefromNumberOfepisodes(self, episodes):

        ''' Returns a list of anime as a string based on the number of episodes inputted from the user '''

        try:
            ''' Creates a cursor to use'''
            cursor = self.connection.cursor()

            ''' Query '''
            query = "SELECT title FROM anime WHERE episodes=%s;"

            ''' Executes Query '''
            cursor.execute(query, (int(episodes),))
            result = cursor.fetchall()
            return [title[0] for title in result] 
                
        except Exception as e:
            ''' If query fails to excute, error message is printed '''

            print ("Something went wrong when executing the query: ", e)
            return None

    def getTitleofAnimefromNumberOfepisodesRange(self, episodes_range):
        ''' Returns a list of anime as a string based on the number of episodes inputted from the user '''

        try:
            ''' Creates a cursor to use'''
            cursor = self.connection.cursor()

            ''' Query '''
            query = "SELECT title FROM anime WHERE episodes BETWEEN %s AND %s;"
            
            episodes = episodes_range.split(',')
            if len(episodes) != 2:
                raise ValueError('Invalid episodes range format. Please enter two numbers separated by a comma.')
            episode1, episode2 = [int(episode.strip()) for episode in episodes]

            ''' Executes Query '''
            cursor.execute(query, (episode1, episode2))
            result = cursor.fetchall()
            return [title[0] for title in result] 
            
        except Exception as e:
            ''' If query fails to execute, error message is printed '''
            print ("Something went wrong when executing the query: ", e)
            return None


    def getTitleofAnimefromScore(self, score):

        ''' Returns a list of anime as a string based on the score inputted from the user '''

        try:
            ''' Creates a cursor to use'''
            cursor = self.connection.cursor()

            ''' Query '''
            query = "SELECT title FROM anime WHERE score=%s;"

            ''' Executes Query '''
            cursor.execute(query, (score,))
            result = cursor.fetchall()
            return [title[0] for title in result] 
        
        except Exception as e:
            ''' If query fails to excute, error message is printed '''

            print ("Something went wrong when executing the query: ", e)
            return None

    def getTitleofAnimefromScoreRange(self, score_range):
        ''' Returns a list of anime as a string based on the score inputted from the user '''

        try:
            ''' Creates a cursor to use'''
            cursor = self.connection.cursor()

            ''' Query '''
            query = "SELECT title FROM anime WHERE score BETWEEN %s AND %s;"

            scores = score_range.split(',')
            if len(scores) != 2:
                raise ValueError('Invalid score range format. Please enter two scores separated by a comma.')
            score1, score2 = [float(score.strip()) for score in scores]

            ''' Executes Query '''
            cursor.execute(query, (score1, score2))
            result = cursor.fetchall()
            return [title[0] for title in result] 
            
        except Exception as e:
            ''' If query fails to execute, error message is printed '''
            print ("Something went wrong when executing the query: ", e)
            return None

    def getSynopsis(self, title):

        ''' Returns the synopsis of the anime inputted from the user'''

        try:
            ''' Creates a cursor to use'''
            cursor = self.connection.cursor()

            ''' Query '''
            query = "SELECT synopsis FROM anime WHERE title ILIKE %s"

            ''' Executes Query '''
            cursor.execute(query, (title,))
            return cursor.fetchone()
            
        except Exception as e:
            ''' If query fails to excute, error message is printed '''

            print ("Something went wrong when executing the query: ", e)
            return None

    def getGenre(self, title):

        ''' Returns the genre of the anime inputted from the user'''

        try:
            ''' Creates a cursor to use'''
            cursor = self.connection.cursor()

            ''' Query '''
            query = "SELECT genre FROM anime WHERE title ILIKE %s"

            ''' Executes Query '''
            cursor.execute(query, (title,))
            return cursor.fetchone()
            
        except Exception as e:
            ''' If query fails to excute, error message is printed '''

            print ("Something went wrong when executing the query: ", e)
            return None

    def getScoreofAnime(self, title):

        ''' Returns the score of the anime inputted from the user'''

        try:
            ''' Creates a cursor to use'''
            cursor = self.connection.cursor()

            ''' Query '''
            query = "SELECT score FROM anime WHERE title ILIKE %s"

            ''' Executes Query '''
            cursor.execute(query, (title,))
            return cursor.fetchone()
            
        except Exception as e:
            ''' If query fails to excute, error message is printed '''

            print ("Something went wrong when executing the query: ", e)
            return None

    def getNumberofEpisodes(self, title):

        ''' Returns the number of episodes of the anime inputted from the user'''

        try:
            ''' Creates a cursor to use'''
            cursor = self.connection.cursor()

            ''' Query '''
            query = "SELECT episodes FROM anime WHERE title ILIKE %s;"

            ''' Executes Query '''
            cursor.execute(query, ('%' + title + '%',))
            return cursor.fetchone()
        
        except Exception as e:

            ''' If query fails to excute, error message is printed '''

            print("Something went wrong when executing the query: ", e)
            return None
