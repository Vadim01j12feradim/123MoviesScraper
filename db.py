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
    def insertVideo(self, data):
        
        return self.insertAndGetId(self.insert_Video_Query, data)
        
    def insertAndGetId(self,query, data):
        last_inserted_id = 0
        with mysql.connector.connect(**self.db_config) as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(query, data)
                    conn.commit()
                    print("Data inserted successfully!")

                    last_inserted_id = cursor.lastrowid
                    print(f"Last inserted ID: {last_inserted_id}")
                except Exception as e:
                    conn.rollback()
                    print(f"Error: {e}")
        return last_inserted_id