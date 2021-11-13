class DBUtil():
    @staticmethod
    def insert(table: str, data: object) -> str:
        sql = "insert into %s set " % table
        for key in data:
            sql += "%s='%s'," % (key, data[key])
        sql = sql[:-1]
        return sql

    @staticmethod
    def select_all(table: str) -> str:
        return "select * from %s" % table
    
    @staticmethod
    def select_by_id(table: str, id: int) -> str:
        return "select * from %s where id=%d" % (table, id)

    @staticmethod
    def get_all_where(table: str, data: dict) -> str:
        sql = "select * from %s where " % table
        for key in data:
            sql += "%s='%s' and " % (key, data[key])
        sql = sql[:-4]
        return sql
