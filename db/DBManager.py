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
        columns = cursor.description 
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()] # Frankly, this is copied from stackoverflow. Sorry.
        return result

    def execute(self, query, do_after=None):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        if do_after:
            do_after(cursor)

instance = DBManager()
    