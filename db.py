import mysql.connector

class Sql:
    def __init__(self):
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
            SELECT Id FROM Video WHERE UrlVideo =  %(UrlVideo)s AND Name = %(Name)s AND Duration = %(Duration)s
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
        return self.insertAndGetId(self.select_Video_Query, self.insert_Video_Query, data)
    
    def insertGenre(self, data):
        return self.insertAndGetId(self.select_Genre_Query, self.insert_Genre_Query, data)
    
    def insertActor(self, data):
        return self.insertAndGetId(self.select_Actor_Query, self.insert_Actor_Query, data)
    
    def insertDirector(self, data):
        return self.insertAndGetId(self.select_Director_Query, self.insert_Director_Query, data)
    
    def insertCountry(self, data):
        return self.insertAndGetId(self.select_Country_Query, self.insert_Country_Query, data)
    
    def insertAndGetId(self,select_query, insert_query, data):
        last_inserted_id = 0
        with mysql.connector.connect(**self.db_config) as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(select_query, data)
                    existing_record = cursor.fetchone()

                    if existing_record:
                        last_inserted_id = existing_record[0]
                    else:
                        cursor.execute(insert_query, data)
                        last_inserted_id = cursor.lastrowid
                    conn.commit()

                except Exception as e:
                    conn.rollback()
                    print(f"Error: {e}")
        return last_inserted_id