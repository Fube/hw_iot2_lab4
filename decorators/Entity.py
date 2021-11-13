from inspect import getmembers
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
                # if not '__managed__' in attr.__dict__:
                if is_db_native(attr):
                    print(f"{field} was db native")
                    values[field] = attr
            
            db.execute(DBUtil.insert(self.__table__, values))
        
        def get_all(cls):
            return "Getting all..."

        get_all_m = classmethod(get_all)

        fields_to_set = {
            "__table__": self.__table__,
            "__managed__": True,
            "__changed__": False,
            'save': save,
            'get_all': get_all_m,
        }

        def get_factory(field):
            def _get(self):
                return getattr(self, field)
            return _get
        
        def set_factory(field):
            def _set(self, value):
                self.__changed__ = True
                setattr(self, field, value)
            return _set

        for field in fields:
            backer = f"__{field}__"
        
            fields_to_set[field] = property(get_factory(backer), set_factory(backer))

        to_return = type(clazz.__name__, (), fields_to_set)


        return to_return

