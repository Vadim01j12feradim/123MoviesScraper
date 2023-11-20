import mysql.connector
from datetime import datetime

class Sql:
    def __init__(self):
        self.imgMovieSrcTemp = ""
        self.db_config = {
            'host': 'localhost',
            'user': 'Username',
            'password': 'Password',
            'database': '123Movies',
        }
        self.insert_Video_Query = """
            INSERT INTO Video (UrlVideo, Duration, ReleaseDate, Score, Description, Name, Img, Episode)
            VALUES (%(UrlVideo)s, %(Duration)s, %(ReleaseDate)s, %(Score)s, %(Description)s, %(Name)s, %(Img)s, %(Episode)s)
        """
        self.select_Video_Query = """
            SELECT Id FROM Video WHERE Img =  %(Img)s AND Name = %(Name)s AND Duration = %(Duration)s AND ReleaseDate = %(ReleaseDate)s AND Episode = %(Episode)s
        """
        self.insert_Serie_Query = """
            INSERT INTO Serie (Eps, Name, Img)
            VALUES (%(Eps)s, %(Name)s, %(Img)s)
        """
        self.select_Serie_Query = """
            SELECT Id FROM Serie WHERE Eps =  %(Eps)s AND Name = %(Name)s AND Img = %(Img)s
        """

        self.insert_Genre_Query = """
            INSERT INTO Genre (Name) VALUES (%(Name)s)
        """
        self.select_Genre_Query = """
            SELECT Id FROM Genre WHERE Name = %(Name)s
        """
        self.select_Actor_Query = """
            SELECT Id FROM Actor WHERE Name = %(Name)s
        """
        self.insert_Actor_Query ="""
            INSERT INTO Actor (Name) VALUES (%(Name)s)
        """
        self.select_Director_Query = """
            SELECT Id FROM Director WHERE Name = %(Name)s
        """
        self.insert_Director_Query ="""
            INSERT INTO Director (Name) VALUES (%(Name)s)
        """
        self.select_Country_Query = """
            SELECT Id FROM Country WHERE Name = %(Name)s
        """
        self.insert_Country_Query = """
            INSERT INTO Country (Name) VALUES (%(Name)s)
        """

        self.insert_Movie_Query = """
            INSERT INTO Movie (IdVideo, Img, Quality)
            VALUES (%(IdVideo)s, %(Img)s, %(Quality)s)
        """
        self.select_Movie_Query = """
            SELECT Id FROM Movie WHERE IdVideo =  %(IdVideo)s AND Img = %(Img)s AND Quality = %(Quality)s
        """

        self.select_SerieVideo_Query = """
            SELECT Id FROM SerieVideo WHERE IdSerie =  %(IdSerie)s AND IdVideo = %(IdVideo)s
        """
        self.insert_SerieVideo_Query = """
            INSERT INTO SerieVideo (IdSerie, IdVideo)
            VALUES (%(IdSerie)s, %(IdVideo)s)
        """
        self.select_VideoActor_Query = """
            SELECT Id FROM VideoActor WHERE IdVideo =  %(IdVideo)s AND IdActor = %(IdActor)s
        """
        self.insert_VideoActor_Query = """
            INSERT INTO VideoActor (IdVideo, IdActor)
            VALUES (%(IdVideo)s, %(IdActor)s)
        """
        self.select_VideoCountry_Query = """
            SELECT Id FROM VideoCountry WHERE IdVideo =  %(IdVideo)s AND IdCountry = %(IdCountry)s
        """
        self.insert_VideoCountry_Query = """
            INSERT INTO VideoCountry (IdVideo, IdCountry)
            VALUES (%(IdVideo)s, %(IdCountry)s)
        """
        self.select_VideoDirector_Query = """
            SELECT Id FROM VideoDirector WHERE IdVideo =  %(IdVideo)s AND IdDirector = %(IdDirector)s
        """
        self.insert_VideoDirector_Query = """
            INSERT INTO VideoDirector (IdVideo, IdDirector)
            VALUES (%(IdVideo)s, %(IdDirector)s)
        """
        self.select_VideoGenre_Query = """
            SELECT Id FROM VideoGenre WHERE IdVideo =  %(IdVideo)s AND IdGenre = %(IdGenre)s
        """
        self.insert_VideoGenre_Query = """
            INSERT INTO VideoGenre (IdVideo, IdGenre)
            VALUES (%(IdVideo)s, %(IdGenre)s)
        """

        self.select_VideoCountry_Query = """
            SELECT Id FROM VideoCountry WHERE IdVideo =  %(IdVideo)s AND IdCountry = %(IdCountry)s
        """
        self.insert_VideoCountry_Query = """
            INSERT INTO VideoCountry (IdVideo, IdCountry)
            VALUES (%(IdVideo)s, %(IdCountry)s)
        """

    

    def insertVideoGenre(self, data):
        data = {
            'IdVideo': data.IdVideo,
            'IdGenre': data.IdGenre
        }
        return self.insertAndGetId(self.select_VideoGenre_Query, self.insert_VideoGenre_Query, data, data)
    
    def insertVideoDirector(self, data):
        data = {
            'IdVideo': data.IdVideo,
            'IdDirector': data.IdDirector
        }
        return self.insertAndGetId(self.select_VideoDirector_Query, self.insert_VideoDirector_Query, data, data)
    
    def insertVideoCountry(self, data):
        data = {
            'IdVideo': data.IdVideo,
            'IdCountry': data.IdCountry
        }
        return self.insertAndGetId(self.select_VideoCountry_Query, self.insert_VideoCountry_Query, data, data)
    

    def insertVideoActor(self, data):
        data = {
            'IdVideo': data.IdVideo,
            'IdActor': data.IdActor
        }
        return self.insertAndGetId(self.select_VideoActor_Query, self.insert_VideoActor_Query, data, data)
    
    def insertSerieVideo(self, data):
        data = {
            'IdSerie': data.IdSerie,
            'IdVideo': data.IdVideo
        }
        return self.insertAndGetId(self.select_SerieVideo_Query, self.insert_SerieVideo_Query, data, data)
    

    def insertMovie(self, data):
        data = {
            'IdVideo': data.IdVideo,
            'Img': data.Img,
            'Quality': data.Quality
        }
        return self.insertAndGetId(self.select_Movie_Query, self.insert_Movie_Query, data, data)
    
    def insertVideo(self, data):

        date_string = f"{data.Release}-01-01"
        date_object = datetime.strptime(date_string, "%Y-%m-%d")

        dataS = {
            'Img': data.UrlVideo,
            'Name': data.Name,
            'Duration': data.Duration,
            'ReleaseDate': date_object,
            'Episode': data.Episode
        }

        dataI = {
            'UrlVideo': data.UrlVideo,
            'Duration': data.Duration,
            'ReleaseDate': date_object,
            'Score': data.Score,
            'Description': data.Description,
            'Name': data.Name,
            'Img': data.Img,
            'Episode': data.Episode
        }

        return self.insertAndGetId(self.select_Video_Query, self.insert_Video_Query, dataS, dataI)
    
    def insertGenre(self, data):
        data = {
            'Name': data.Name
        }
        return self.insertAndGetId(self.select_Genre_Query, self.insert_Genre_Query, data, data)
    
    def insertActor(self, data):
        data = {
            'Name': data.Name
        }
        return self.insertAndGetId(self.select_Actor_Query, self.insert_Actor_Query, data, data)
    
    def insertDirector(self, data):
        data = {
            'Name': data.Name
        }
        return self.insertAndGetId(self.select_Director_Query, self.insert_Director_Query, data, data)
    
    def insertCountry(self, data):
        data = {
            'Name': data.Name
        }
        return self.insertAndGetId(self.select_Country_Query, self.insert_Country_Query, data, data)
    
    def insertSerie(self, data):
        data = {
            'Eps': data.Eps,
            'Name': data.Name,
            'Img': data.Img
        }
        return self.insertAndGetId(self.select_Serie_Query, self.insert_Serie_Query, data, data)
    
    def insertAndGetId(self,select_query, insert_query, dataS, dataI):
        last_inserted_id = 0
        with mysql.connector.connect(**self.db_config) as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(select_query, dataS)
                    existing_record = cursor.fetchone()

                    if existing_record:
                        last_inserted_id = existing_record[0]
                    else:
                        cursor.execute(insert_query, dataI)
                        last_inserted_id = cursor.lastrowid
                    conn.commit()

                except Exception as e:
                    conn.rollback()
                    print(f"Error: {e}")
        return last_inserted_id