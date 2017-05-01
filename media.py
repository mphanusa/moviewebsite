import webbrowser

class Movie():
    """ Class blueprint to provide information related to favorite movies """
    VALID_RATINGS = [ "G", "PG-13", "PG", "R" ]

    # Note: trailer_youtube_url name cannot be changed since it's used
    # in other modules.
    
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer):
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    
    
        
