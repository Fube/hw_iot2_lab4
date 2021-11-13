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

    @staticmethod
    def select_all(table: str) -> str:
        return "select * from %s" % table
    
    @staticmethod
    def select_by_id(table: str, id: int) -> str:
        return "select * from %s where id=%d" % (table, id)
