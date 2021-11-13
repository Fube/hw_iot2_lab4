class DBUtil():
    @staticmethod
    def insert(table: str, data: object) -> str:
        sql = "insert into %s set " % table
        for key in data:
            sql += "%s='%s'," % (key, data[key])
        sql = sql[:-1]
        return sql

    @staticmethod
    def get_identity():
        return "select @@IDENTITY"