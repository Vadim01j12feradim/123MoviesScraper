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
            INSERT INTO Video (UrlVideo, Duration, ReleaseDate, Score, Description, Name, Img)
            VALUES (%(UrlVideo)s, %(Duration)s, %(ReleaseDate)s, %(Score)s, %(Description)s, %(Name)s, %(Img)s)
        """
        self.select_Video_Query = """
            SELECT Id FROM Video WHERE Img =  %(Img)s AND Name = %(Name)s AND Duration = %(Duration)s AND ReleaseDate = %(ReleaseDate)s 
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
    def insertVideo(self, data):

        date_string = f"{data.Release}-01-01"
        date_object = datetime.strptime(date_string, "%Y-%m-%d")

        dataS = {
            'Img': data.UrlVideo,
            'Name': data.Name,
            'Duration': data.Duration,
            'ReleaseDate': date_object
        }

        dataI = {
            'UrlVideo': data.UrlVideo,
            'Duration': data.Duration,
            'ReleaseDate': date_object,
            'Score': data.Score,
            'Description': data.Description,
            'Name': data.Name,
            'Img': data.Img,
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