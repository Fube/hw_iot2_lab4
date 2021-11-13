from inspect import getmembers
from db.DBManager import instance as db

class Entity(object):
    def __init__(self, __table__):
        self.__table__ = __table__


    def __call__(self, clazz: type):
        members = getmembers(clazz)[0][1] # [0][1] -> __annotations__
        fields = list(members.keys())

        def save(self):
            if not self.__changed__:
                return
            return "Saving..."
        
        def get_all(cls):
            return "Getting all..."

        get_all_m = classmethod(get_all)

        fields_to_set = {
            "__changed__": False,
            'save': save,
            'get_all': get_all_m,
        }

        for field in fields:
            backer = f"__{field}__"
            fields_to_set[backer] = None

            def setter(self, value):
                self.__changed__ = True
                fields_to_set[backer] = value

            fields_to_set[field] = property(lambda self: self.__dict__[backer], setter)

        to_return = type(clazz.__name__, (), fields_to_set)


        return to_return

