import mysql.connector

class DBManager():
    conn: mysql.connector.connection.MySQLConnection
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="pwd",
            database="test"
        )

    def die(self):
        self.conn.close()

    def query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def execute(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()

instance = DBManager()
    