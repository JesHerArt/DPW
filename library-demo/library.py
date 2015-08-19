class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []
        #TODO:
        #have an array to hold the movie information (all of them)
        #some way to add to that array of movies
        #generate a list of the movies
        #calculate the time span between movies
    
    def add_movie(self, m):
        self.__movie_list.append(m)
        #print m.title
        #<Movie Data Object>
    
    def compile_list(self):
        output = ""
        for movie in self.__movie_list: #for each movie in the movie array
            output += "Title: " + movie.title + ' (' + str(movie.year) + ') Directed by: ' + movie.director + '<br />'
        return output
    
    def calc_time_span(self):
        #calculate the time in between movies
        #years
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)
        
        #sort years from low to high
        years.sort()
        
        #subtract the low year from the high year
        num = len(years) - 1
        span = years[num] - years[0] #last number - first number
        
        #return the span of time
        return 'The span between films entered is ' + str(span)

class MovieData(object): #Data Object
    def __init__(self):
        self.title = ''
        self.__year = 0 #check for valid year
        self.director = ''
    
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, y):
        if y > 2015: #if the date is not valid
            print "Error, invalid date!"
            self.__year = 2015
        else:
            self.__year = y