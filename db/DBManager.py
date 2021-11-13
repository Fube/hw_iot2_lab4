class DBManager():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="pwd",
            database="test"
        )

    def die(self):
        self.conn.close()