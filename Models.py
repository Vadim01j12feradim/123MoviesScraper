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

