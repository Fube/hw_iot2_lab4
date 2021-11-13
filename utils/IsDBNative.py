from datetime import datetime, date

def is_db_native(var):
    return isinstance(var, (str, int, float, bool, date, datetime))
