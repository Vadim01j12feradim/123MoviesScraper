class Video:
    def __init__(self):
        self.Id = 0
        self.UrlVideo = ""
        self.Duration = ""
        self.Release = ""
        self.Score = ""
        self.Description = ""
        self.Name = ""
        self.Img = ""
        self.Episode = ""
        self.Genre =[]
        self.Actor =[]
        self.Director =[]
        self.Country =[]

class Movie:
    def __init__(self):
        self.Id = 0
        self.IdVideo = 0
        self.Img = ""
        self.Quality = ""

class Serie:
    def __init__(self):
        self.Id = 0
        self.Eps = 0
        self.Name = ""
        self.Img = ""
        self.Videos =[]

class Genre:
    def __init__(self):
        self.Id = 0
        self.Name = ""

class Actor:
    def __init__(self):
        self.Id = 0
        self.Name = ""

class Director:
    def __init__(self):
        self.Id = 0
        self.Name = ""

class Country:
    def __init__(self):
        self.Id = 0
        self.Name = ""

class SerieVideo:
    def __init__(self):
        self.Id = 0
        self.IdSerie = 0
        self.IdVideo = 0
    

class VideoActor:
    def __init__(self):
        self.Id = 0
        self.IdVideo = 0
        self.IdActor = 0

class VideoCountry:
    def __init__(self):	 	
        self.Id = 0
        self.IdVideo = 0
        self.IdCountry = 0

class VideoDirector:
    def __init__(self):	 	
        self.Id = 0
        self.IdVideo = 0
        self.IdDirector = 0

class VideoGenre:
    def __init__(self):	 	
        self.Id = 0
        self.IdVideo = 0
        self.IdGenre = 0


