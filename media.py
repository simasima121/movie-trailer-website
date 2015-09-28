#title
#storyline
#poster_image
#trailer_youtube

import webbrowser

class Movie():
    """ This class provides a way to store movie related info"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    ## initialize the class and set movie_title etc equal to self.var   
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title 
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    ## show_trailer file takes argument of self and uses webbrowser to open the youtube trailer    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
