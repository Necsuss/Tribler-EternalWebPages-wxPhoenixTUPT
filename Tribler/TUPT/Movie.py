class Movie(object):
    """ Class that contains metadata of a movie in a object.
    Supported keys:
        title
        releaseYear
        director
    """
    
    dictionary = {}
    
    def __init__(self):
        self.dictionary = {}