from inspect import getmembers
from typing import Tuple
from db.DBManager import instance as db
from db.DButil import DBUtil
from utils.IsDBNative import is_db_native

class Entity(object):
    def __init__(self, __table__):
        self.__table__ = __table__


    def __call__(self, clazz: type):
        members = getmembers(clazz)[0][1] # [0][1] -> __annotations__
        fields = list(members.keys())

        def save(self):
            if not self.__changed__:
                return

            values = dict()

            for field in fields:
                attr = getattr(self, field)
                if is_db_native(attr):
                    print(f"{field} was db native")
                    values[field] = attr
                else:
                    print(f"{field} was not db native")
                    print(attr.__dict__)

            
            db.execute(DBUtil.insert(self.__table__, values))
        

        def back_to_entity(obj, row: dict):
            for field in fields:
                setattr(obj, field, row[field])
            return obj                


        def get_all(cls):
            ret = []
            raw = db.query(DBUtil.select_all(self.__table__))
            for row in raw:
                obj = cls()
                ret.append(back_to_entity(obj, row))
            obj.__changed__ = False # It has not changed, it has been retrieved from db

            return ret

        
        def get_by_id(cls, id):
            raw = db.query(DBUtil.select_by_id(self.__table__, id))
            obj = cls()
            back_to_entity(obj, raw[0])
            obj.__changed__ = False

            return obj
                    

        get_all_m = classmethod(get_all)
        get_by_id_m = classmethod(get_by_id)
                
        def init_factory(table_name):
            def init(self):
                self.__changed__ = False
                self.__managed__ = True
                self.__table__ = table_name
            return init

        def get_factory(field):
            def _get(self):
                return getattr(self, field)
            return _get
        
        def set_factory(field):
            def _set(self, value):
                self.__changed__ = True
                setattr(self, field, value)
            return _set

        fields_to_set = {
            "__init__": init_factory(self.__table__),
            'save': save,
            'get_all': get_all_m,
            'get_by_id': get_by_id_m,
        }

        for field in fields:
            backer = f"__{field}__"
        
            fields_to_set[field] = property(get_factory(backer), set_factory(backer))

        to_return = type(clazz.__name__, (), fields_to_set)


        return to_return

